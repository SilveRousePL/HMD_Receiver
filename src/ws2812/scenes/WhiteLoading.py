import sys
from ws2812.scene import Scene
import time

class WhiteLoading(Scene):
    def do(self, step, led_count):
        iteration = step % 256
        if iteration < 128:
            sub = 255 - iteration
        else:
            sub = iteration
        result = [(sub, sub, sub)] * led_count
        return result
