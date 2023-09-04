# Source: https://www.instructables.com/Sound-Sensor-Raspberry-Pi/

import RPi.GPIO as GPIO
import time

# GPIO set up
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
        if GPIO.input(channel):
                print("Sound Detected!")
        else:
                print("Sound Detected!")
 
# Know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 300)
# Assign function to GPIO PIN, Run function on change
GPIO.add_event_callback(channel, callback)

# Infinite loop
while True:
        time.sleep(1)
