import threading

class SceneExecutor:
    def __init__(self):
        self.thread_running = False
        self.thread = threading.Thread(target=self.thread_func)
        self.led_count = None
        self.scene = None
        self.neopixel = None

    def thread_func(self):
        step = 0
        while self.thread_running:
            colors = self.scene.do(step, self.led_count)
            self.neopixel.show()
            step += 1

    def start(self, neopixel, led_count):
        self.neopixel = neopixel
        self.led_count = led_count
        self.thread_running = True
        self.thread.start()

    def stop(self):
        self.thread_running = False

    def wait_for_stop(self):
        self.thread.join()
