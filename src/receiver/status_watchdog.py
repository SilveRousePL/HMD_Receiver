import threading
import time

class StatusWatchdog:
    def __init__(self, woof_function, period_sec, refresh_sec):
        self.thread_running = False
        self.thread = threading.Thread(target=self.thread_func)
        self.period_sec = period_sec
        self.refresh_sec = refresh_sec
        self.last_feed = time.time()
        self.woof_function = woof_function

    def thread_func(self):
        while self.thread_running:
            if (time.time() - self.last_feed) > self.period_sec:
                self.woof()
            time.sleep(self.refresh_sec)

    def feed(self):
        self.last_feed = time.time()

    def woof(self):
        self.woof_function()

    def start(self):
        self.thread_running = True
        self.thread.start()

    def stop(self):
        self.thread_running = False

    def wait_for_stop(self):
        self.thread.join()