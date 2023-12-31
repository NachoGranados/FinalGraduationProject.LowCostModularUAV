
# Source: https://www.instructables.com/Interfacing-GPS-Module-With-Raspberry-Pi/

import serial
import pynmea2

while True:

	port = "/dev/ttyAMA0"
	ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
	dataout = pynmea2.NMEAStreamReader()
	newdata = ser.readline()

	if newdata[0:6] == b"$GNRMC":

		newmsg = pynmea2.parse(newdata.decode())
		lat = newmsg.latitude
		lng = newmsg.longitude
		gps = "Latitude = " + str(lat) + "and Longitude = " + str(lng)

		print(gps)
