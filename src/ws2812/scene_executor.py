import threading
import time
from ws2812.scenes.WhiteLoading import WhiteLoading

class SceneExecutor:
    def __init__(self):
        self.thread_running = False
        self.thread = None
        self.led_count = None
        self.frame_time = 0.5
        self.step_size = 1
        self.scene = WhiteLoading()
        self.neopixel = None

    def thread_func(self):
        step = 0
        while self.thread_running:
            time_started = time.perf_counter()
            colors = self.scene.do(step, self.led_count)
            for idx, color in enumerate(colors):
                self.neopixel[idx] = color
            while time.perf_counter() - time_started < self.frame_time:
                time.sleep(0.05)
            self.neopixel.show()
            step += self.step_size

    def start(self, neopixel, led_count):
        self.neopixel = neopixel
        self.led_count = led_count
        self.thread = threading.Thread(target=self.thread_func)
        self.thread_running = True
        self.thread.start()

    def stop(self):
        self.thread_running = False

    def wait_for_stop(self):
        self.thread.join()
        self.thread = None
