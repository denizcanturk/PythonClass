import threading
import time

class PausableWorker:
    def __init__(self):
        self._event = threading.Event()
        self._event.set()  # Start with the event set, so threads don't block initially
        self._stop_event = threading.Event()

    def worker(self):
        while not self._stop_event.is_set():
            self._event.wait()  # Block if the event is not set (i.e., paused)
            # Do some work here
            print("Working...")
            time.sleep(1)

    def pause(self):
        self._event.clear()  # Clear the event to pause the thread

    def resume(self):
        self._event.set()  # Set the event to resume the thread

    def stop(self):
        self._stop_event.set()  # Stop the worker thread
        self._event.set()  # Make sure to release any blocked threads
        self._thread.join()  # Wait for the thread to finish

    def start(self):
        self._thread = threading.Thread(target=self.worker)
        self._thread.start()

# Usage
worker = PausableWorker()
worker.start()
time.sleep(5)  # Let it work for 5 seconds

print("Pausing...")
worker.pause()
time.sleep(5)  # Pause for 5 seconds

print("Resuming...")
worker.resume()
time.sleep(5)  # Let it work for another 5 seconds

print("Stopping...")
worker.stop()
