import threading
import time

class Worker(threading.Thread):
    def __init__(self, interval, callback):
        super().__init__()
        self.interval = interval
        self.callback = callback
        self.state = threading.Event()

    def run(self):
        while not self.state.is_set():
            self.callback()
            self.state.wait(self.interval)

    def stop(self):
        self.state.set()
        self.join()

def simpleTask():
    print("Sensor Read")

if __name__ == "__main__":
    worker = Worker(1,simpleTask)
    worker.start()
    time.sleep(10)
    worker.stop()

    print("Program sonlanıyor")