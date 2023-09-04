# Source: https://www.donskytech.com/using-infrared-ir-sensor-with-raspberry-pi/

import RPi.GPIO as GPIO
import time

# declare the sensor and led pin
sensorPin = 23
ledPin = 26

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

try:
    while True:
        if GPIO.input(sensorPin):
            # If no object is near
            GPIO.output(ledPin, False)
            while GPIO.input(sensorPin):
                time.sleep(0.2)
        else:
            # If an object is detected
            GPIO.output(ledPin, True)
            print("Object Detected")
except KeyboardInterrupt:
    GPIO.cleanup()
