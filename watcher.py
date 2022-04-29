# DropBox App
# author: Jananni Balaskandan

from watchdog.observers import Observer
import time


class Watcher:
    def __init__(self, directory, handler):
        self.directory = directory
        self.handler = handler
        self.observer = Observer()

    def run(self):
        self.observer.schedule(self.handler, self.directory, recursive=True)
        self.observer.start()
        print("INFO : Client directory being monitored")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
            self.observer.join()
