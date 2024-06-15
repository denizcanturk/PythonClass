# Base class
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        raise NotImplementedError("Subclasses should implement this!")

    def move(self):
        raise NotImplementedError("Subclasses should implement this!")

    def info(self):
        return f"{self.name} is a {self.age}-year-old {self.species}"

# Derived class for Dog
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, species="Dog")
        self.breed = breed

    def speak(self):
        return "Woof!"

    def move(self):
        return "runs on four legs"

    def info(self):
        base_info = super().info()
        return f"{base_info} of breed {self.breed}"

# Derived class for Cat
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, species="Cat")
        self.color = color

    #def speak(self):
    #    return "Meow!"

    def move(self):
        return "sneaks on four legs"

    def info(self):
        base_info = super().info()
        return f"{base_info} with {self.color} fur"

# Derived class for Bird
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age, species="Bird")
        self.wing_span = wing_span

    def speak(self):
        return "Chirp!"

    def move(self):
        return "flies in the sky"

    def info(self):
        base_info = super().info()
        return f"{base_info} with a wingspan of {self.wing_span} cm"

# Example usage
animals = [
    Dog("Buddy", 3, "Golden Retriever"),
    Cat("Whiskers", 2, "black"),
    Bird("Tweety", 1, 25)
]

for animal in animals:
    print(animal.info())
    print(f"{animal.name} says {animal.speak()} and {animal.move()}.\n")
