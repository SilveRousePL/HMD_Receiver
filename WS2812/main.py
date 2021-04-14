#!/usr/bin/env python3
import time
import neopixel
import board
import sys
import threading
from scenes.PoliceLights import PoliceLights
from scenes.WhiteLoading import WhiteLoading

class Lights:
    def __init__(self, pin, count):
        self.led_count = count
        self.pixels = neopixel.NeoPixel(pin, count, auto_write=False, pixel_order=neopixel.RGB)

    def __del__(self):
        self.scene.stop()
        self.scene.wait_for_stop()
        self.disable_leds()

    def start_scene(self):
        self.scene.start(self.pixels)

    def set_scene(self, scene):
        self.scene = scene

    def stop_scene(self):
        self.scene.stop()

    def disable_leds(self):
        self.pixels.fill((0, 0, 0))
        self.pixels.show()

    def test_leds(self):
        self.pixels.fill((255, 255, 255))
        self.pixels.show()


if __name__ == '__main__':
    lights = Lights(board.D18, 5)
    lights.start_scene()
    print("Test1")
    time.sleep(5)
    print("Test2")
    lights.set_scene(PoliceLights())
    print("Test3")
    time.sleep(5)
    print("Test4")
    lights.set_scene(WhiteLoading())
    print("Test5")
    time.sleep(5)
    print("Test6")
    lights.stop_scene()
    print("Test7")
    #lights.scene.wait_for_stop()

    # pixels[0] = (0, 255, 0)
    # pixels[1] = (0, 0, 255)
    # while True:
    #     pixels.fill((255, 255, 255))
    #     pixels.show()
    #     time.sleep(5)
    #     pixels.fill((0, 0, 0))
    #     pixels.show()
    #     time.sleep(5)
