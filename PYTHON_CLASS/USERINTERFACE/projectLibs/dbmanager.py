import sqlite3
import os

class Database:
    def __init__(self, db_file):
        """
        Initialize the Database connection.

        :param db_file: Path to the SQLite database file.
        """
        self.db_file = db_file
        
        #self.initialize(db_file)
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table()
        self.insert_sample_data()  # Insert sample data for testing
        
    def create_table(self):
        """
        Create the recipes table if it doesn't already exist.
        """
        print("create table func called...")
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            co2 TEXT,
            ph TEXT,
            su_s TEXT,
            ort_s TEXT,
            nem TEXT,
            ec TEXT
        )
        ''')
        self.connection.commit()
        print("Table created or already exists.")

    def insert_sample_data(self):
        """
        Insert sample data into the recipes table for testing.
        """
        print("Inserting sample data...")
        self.cursor.execute('''
        INSERT INTO recipes (name, co2, ph, su_s, ort_s, nem, ec)
        VALUES ('Salatalık', '400', '7.0', '20', '25', '50', '1.2')
        ''')
        self.cursor.execute('''
        INSERT INTO recipes (name, co2, ph, su_s, ort_s, nem, ec)
        VALUES ('Marul', '800', '5.8', '36', '45', '89', '2.8')
        ''')
        self.cursor.execute('''
        INSERT INTO recipes (name, co2, ph, su_s, ort_s, nem, ec)
        VALUES ('Çilek', '1100', '9.4', '53', '17', '98', '3.5')
        ''')
        self.connection.commit()
        print("Sample data inserted.")

    def insert_recipe(self, name, co2, ph, su_s, ort_s, nem, ec):
        """
        Insert a new recipe into the database.

        :param name: Recipe name.
        :param co2: CO2 value.
        :param ph: pH value.
        :param su_s: Su S value.
        :param ort_s: Ort S value.
        :param nem: Nem value.
        :param ec: EC value.
        """
        print("İnsert function called")
        self.cursor.execute('''
        INSERT INTO recipes (name, co2, ph, su_s, ort_s, nem, ec)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, co2, ph, su_s, ort_s, nem, ec))
        self.connection.commit()

    def fetch_recipes(self):
        """
        Fetch all recipes from the database.

        :return: A dictionary where keys are recipe names and values are tuples of recipe data.
        """
        print("fetch function called")
        self.cursor.execute('SELECT name, co2, ph, su_s, ort_s, nem, ec FROM recipes')
        recipes = self.cursor.fetchall()
        print("Fetched recipes from DB:", recipes)  # Debugging statement
        return {name: (co2, ph, su_s, ort_s, nem, ec) for (name, co2, ph, su_s, ort_s, nem, ec) in recipes}

    def close(self):
        """
        Close the database connection.
        """
        self.connection.close()

    @classmethod
    def initialize(cls, db_file):
        """
        Initialize the database by creating it and inserting initial data if it doesn't exist.

        :param db_file: Path to the SQLite database file.
        """
        print("İnit db func called...")
        if not os.path.exists(db_file):
            # Create the database and insert initial data
            db = cls(db_file)  # Create the Database object
            db.insert_recipe("Salatalik", "300", "6.0", "22.0", "24.0", "50", "1.5")
            db.insert_recipe("Marul", "400", "5.5", "21.0", "23.0", "55", "1.8")
            db.insert_recipe("Çilek", "350", "5.8", "23.0", "25.0", "60", "1.7")
            db.insert_recipe("Domates", "500", "6.2", "20.0", "22.0", "65", "2.0")
            db.close()
        else:
            print("Database exists, proceeding...")

if __name__ == "__main__":
    # Path to the database file
    db_file = 'recipes.db'

    # Initialize the database
    Database.initialize(db_file)