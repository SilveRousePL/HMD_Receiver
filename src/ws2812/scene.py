from abc import ABC, abstractmethod
import threading

class Scene(ABC):
    @abstractmethod
    def do(self, step, led_count):
        return [(0, 0, 0)] * led_count

    def test(self, led_count, frame_time, step_size):
        import time
        step = 0
        while True:
            time_started = time.perf_counter()
            colors = self.do(step, led_count)
            while time.perf_counter() - time_started < frame_time:
                time.sleep(0.05)
            print(colors)
            step += step_size
