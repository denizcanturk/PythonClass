import threading
import time

class Worker(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"Thread {self.name} is starting")
        for i in range(10):
            print({self.name}, i)
            time.sleep(1)
        print(f"Thread {self.name} is finishing")

# Create and start 5 threads
threads = []
for i in range(5):
    thread = Worker(f"Worker-{i}")
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have finished")