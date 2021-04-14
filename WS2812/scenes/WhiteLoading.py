import sys
sys.path.append("..")
from scene import Scene
import time

class WhiteLoading(Scene):
    def do(self, step, led_count):
        iteration = step % 256
        if iteration < 128:
            sub = 255 - iteration
        else:
            sub = iteration
        self.neopixel.fill((sub, sub, sub))
        time.sleep(0.01)
