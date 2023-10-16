# Source: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/4

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.stop_preview()
