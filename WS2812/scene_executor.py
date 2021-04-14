import threading

class SceneExecutor:
    def __init__(self):
        self.thread_running = False
        self.thread = threading.Thread(target=self.thread_func)
        self.scene = WhiteLoading()
        self.neopixel = None

    def thread_func(self):
        step = 0
        while self.thread_running:
            colors = self.scene.do(step, led_count)
            self.neopixel.show()
            step += 1

    def start(self, neopixel):
        self.neopixel = neopixel
        self.thread_running = True
        self.thread.start()

    def stop(self):
        self.thread_running = False

    def wait_for_stop(self):
        self.thread.join()
