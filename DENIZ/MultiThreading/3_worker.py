import threading
import time

class Worker(threading.Thread):
    def __init__(self, interval, callback):
        super().__init__()
        self.interval = interval
        self.callback = callback
        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            self.callback()
            self._stop_event.wait(self.interval)

    def stop(self):
        print("Thread' sonlandırılıyor")
        self._stop_event.set()
        self.join()

def simpleTask():
    print("Sensor Data Read!")

if __name__ == "__main__":
    worker = Worker(1, simpleTask)
    worker.start()
    time.sleep(10)
    worker.stop()
    print("Program sonlandırılıyor")