import multiprocessing as mp
import time as t

class Worker(mp.Process):
    def __init__(self, interval, callback):
        super().__init__()
        self.interval = interval
        self.callback = callback
        self._stop_event = mp.Event()

    def run(self):
        while not self._stop_event.is_set():
            self.callback()
            self._stop_event.wait(self.interval)

    def stop(self):
        print("Process' sonlandırılıyor")
        self._stop_event.set()
        self.join()

# Example usage
def example_callback():
    print(f"Callback executed at {t.time()}")

if __name__ == "__main__":
    # Create and start a Worker process
    worker = Worker(interval=2, callback=example_callback)
    worker.start()
    
    # Let it run for a while
    t.sleep(10)
    
    # Stop the worker process
    worker.stop()
