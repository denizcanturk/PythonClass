import threading

class Worker():
    def __init__(self, interval, callback):
        self.interval = interval
        self.callback = callback
        self.thread = threading.Thread(target=self._run)
        self._stop_event = threading.Event()

    def _run(self):
        while not self._stop_event.is_set():
            self.callback()
            self._stop_event.wait(self.interval)

    def start(self):
        self.thread.start()

    def stop(self):
        self._stop_event.set()
        self.thread.join()

if __name__ == "__main__":
    print("This file is not intended for direct use...")