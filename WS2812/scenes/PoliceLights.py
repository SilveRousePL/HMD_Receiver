import sys
sys.path.append("..")
from scene import Scene
import time

class PoliceLights(Scene):
    def do(self, step, led_count):
        if step % 2:
            self.neopixel.fill((255, 0, 0))
        else:
            self.neopixel.fill((0, 0, 255))
        time.sleep(0.2)
