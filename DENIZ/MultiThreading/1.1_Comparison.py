import multiprocessing as mp
import threading
import time as t
import math as m

resultA = []
resultB = []
resultC = []

def hesaplaA(numbers:list)->None:
    for number in numbers:
        resultA.append(m.sqrt(number ** 3))

def hesaplaB(numbers:list)->None:
    for number in numbers:
        resultB.append(m.sqrt(number ** 4))
    

def hesaplaC(numbers:list)->None:
    for number in numbers:
        resultC.append(m.sqrt(number ** 5))

if __name__ == "__main__":
    numbers = list(range(10000000))

    start = t.time()

    hesaplaA(numbers)
    hesaplaB(numbers)
    hesaplaC(numbers)

    end = t.time()

    
    thread1 = threading.Thread(target=hesaplaA, args=(numbers,))
    thread2 = threading.Thread(target=hesaplaB, args=(numbers,))
    thread3 = threading.Thread(target=hesaplaC, args=(numbers,))
    
    startT = t.time()
    thread1.start()
    thread2.start()
    thread3.start()
    endT = t.time()

    thread1.join()
    thread2.join()
    thread3.join()

    p1=mp.Process(target=hesaplaA, args=(numbers,))
    p2=mp.Process(target=hesaplaB, args=(numbers,))
    p3=mp.Process(target=hesaplaC, args=(numbers,))

    startP = t.time()
    p1.start()
    p2.start()
    p3.start()
    endP = t.time()

    print("Doğrusal :", end-start)
    print("Threaded :", endT-startT)
    print("Multiproc:", endP-startP)