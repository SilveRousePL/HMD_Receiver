import neopixel
import threading
from ws2812.scene_executor import SceneExecutor

class Lights:
    def __init__(self, pin, count):
        self.led_count = count
        self.pixels = neopixel.NeoPixel(pin, count, auto_write=False, pixel_order=neopixel.RGB)
        self.scene_executor = SceneExecutor()

    def __del__(self):
        self.scene_executor.stop()
        self.scene_executor.wait_for_stop()
        self.disable_leds()

    def start_scene(self, frame_time, step_size):
        self.set_param(frame_time, step_size)
        self.scene_executor.start(self.pixels, self.led_count)

    def set_scene(self, scene):
        self.scene_executor.scene = scene

    def set_param(self, frame_time, step_size):
        self.scene_executor.frame_time = frame_time
        self.scene_executor.step_size = step_size

    def stop_scene(self):
        self.scene_executor.stop()

    def disable_leds(self):
        self.pixels.fill((0, 0, 0))
        self.pixels.show()

    def set_color_all(self, color):
        self.pixels.fill(color)
        self.pixels.show()

    def set_color(self, diode, color):
        self.pixels[diode] = color
        self.pixels.show()

    def test_leds(self):
        self.pixels.fill((255, 255, 255))
        self.pixels.show()