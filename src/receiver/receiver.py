from collections import deque
import socket
from receiver.status_watchdog import StatusWatchdog
from receiver.sensor_msg import SensorMsg
import board
from ws2812.lights import Lights
from ws2812.scenes.PoliceLights import PoliceLights
from ws2812.scenes.WhiteLoading import WhiteLoading


UDP_IP = ''
UDP_PORT = 4242

last_msgs = deque()
lights = Lights(board.D18, 10)


def motion_action(motion):
    if motion == 1:
        lights.set_scene(PoliceLights())
        lights.start_scene(0.2, 1)
    else:
        lights.stop_scene()
        lights.scene_executor.wait_for_stop()
        lights.disable_leds()


def no_status():
    lights.set_color_all((32, 0, 0))
    print("NO STATUS!")


def status_recovered():
    lights.set_color_all((0, 32, 0))
    print("STATUS RECOVERED!")


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    wd = StatusWatchdog(no_status, 60, 5)
    wd.start()

    while True:
        try:
            data, addr = sock.recvfrom(512)
            msg = SensorMsg.get_obj(data.decode('utf-8'))

            print("JSON: ", data.decode('utf-8')) # DEBUG

            if msg.type == 'motion':
                motion_action(msg.motion)

            wd.feed()

            last_msgs.append(msg)
            if len(last_msgs) > 10:
                last_msgs.popleft()

        except KeyboardInterrupt:
            if sock:
                wd.stop()
                sock.close()
                wd.wait_for_stop()
            break
