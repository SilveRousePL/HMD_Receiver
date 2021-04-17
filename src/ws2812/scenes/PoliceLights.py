import sys
from ws2812.scene import Scene
import time
import math

class PoliceLights(Scene):
    cBLUE  = (0, 0, 255)
    cRED   = (255, 0, 0)
    cWHITE = (255, 255, 255)
    cOFF   = (0, 0, 0)

    def do(self, step, led_count):
        blue_color = [PoliceLights.cBLUE] * (math.floor(led_count/2) - 1)
        red_color = [PoliceLights.cRED] * (math.floor(led_count/2) - 1)
        if step % 2:
            result = blue_color + 2 * [PoliceLights.cWHITE] + red_color
        else:
            result = red_color + 2 * [PoliceLights.cWHITE] + blue_color
        return result
