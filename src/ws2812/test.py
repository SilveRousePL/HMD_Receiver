import time
import board
import sys
from ws2812.lights import Lights
from ws2812.scenes.PoliceLights import PoliceLights
from ws2812.scenes.WhiteLoading import WhiteLoading


def test():
    lights = Lights(board.D18, 10)

    print("WhiteLoading 0.01 4")
    lights.set_scene(WhiteLoading())
    lights.start_scene(0.01, 4)
    time.sleep(5)

    print("PoliceLights 0.5 1")
    lights.set_scene(PoliceLights())
    lights.set_param(0.5, 1)
    time.sleep(5)

    print("PoliceLights 0.1 1")
    lights.set_param(0.1, 1)
    time.sleep(5)

    print("WhiteLoading 0.01 4")
    lights.set_scene(WhiteLoading())
    lights.set_param(0.01, 8)
    time.sleep(5)

    print("Stop!")
    lights.stop_scene()
    lights.scene_executor.wait_for_stop()

    # pixels[0] = (0, 255, 0)
    # pixels[1] = (0, 0, 255)
    # while True:
    #     pixels.fill((255, 255, 255))
    #     pixels.show()
    #     time.sleep(5)
    #     pixels.fill((0, 0, 0))
    #     pixels.show()
    #     time.sleep(5)
