# Source: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/5

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture("image_MIPI_CSI2_Python.jpg")
camera.stop_preview()
