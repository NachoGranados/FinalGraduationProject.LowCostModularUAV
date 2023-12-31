# Source: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/5

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()

for i in range(5):
    sleep(5)
    camera.capture("image%s.jpg" % i)
    
camera.stop_preview()
