# Source: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/6

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()

camera.start_recording("video_MIPI_CSI2_Python.h264")
sleep(5)
camera.stop_recording()

camera.stop_preview()
