import threading
import time

def numbers():
    for i in range(10):
        print(i)
        time.sleep(1)
    
def letters():
    for i in "abcdefgh":
        print(i)
        time.sleep(1)

print("Program başladı...")
#Creating

t1 = threading.Thread(target=numbers)
t2 = threading.Thread(target=letters)

t1.start()
t2.start()

for i in "'^+%&/()":
    print(i)
    time.sleep(1)

t1.join()
t2.join()

print("Ana program kapanıyor...")