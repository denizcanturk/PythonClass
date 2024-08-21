import multiprocessing as mp
import threading as tr
import time as t
import math as m

resultA = []
resultB = []
resultC = []



def hesaplaA(numbers:list):
    for i in numbers:
        resultA.append(m.sqrt(i**3))


def hesaplaB(numbers:list):
    for i in numbers:
        resultB.append(m.sqrt(i**4))

def hesaplaC(numbers:list):
    for i in numbers:
        resultC.append(m.sqrt(i**5))

if __name__ == "__main__":

    numbers = list(range(10000000))

    start = t.time()
    hesaplaA(numbers)
    hesaplaB(numbers)
    hesaplaC(numbers)
    end = t.time()

    t1 = tr.Thread(target=hesaplaA, args=(numbers,))
    t2 = tr.Thread(target=hesaplaB, args=(numbers,))
    t3 = tr.Thread(target=hesaplaC, args=(numbers,))

    startT = t.time()
    t1.start()
    t2.start()
    t3.start()
    endT=t.time()

    t1.join()
    t2.join()
    t3.join()


    m1= mp.Process(target=hesaplaA, args=(numbers,))
    m2= mp.Process(target=hesaplaB, args=(numbers,))
    m3= mp.Process(target=hesaplaC, args=(numbers,))

    startP = t.time()
    m1.start()
    m2.start()
    m3.start()
    endP = t.time()

    print("Normal Çalışma Zamanı :", end-start)
    print("Thread Çalışma Zamanı :", endT-startT)
    print("Proces Çalışma Zamanı :", endP-startP) 