# Source: https://medium.com/propelland/raspberry-pi-tutorial-on-using-a-usb-camera-to-display-and-record-videos-with-python-a41c6938f89f

# Import libraries
from cameraRecord import recordVideo
from multiprocessing import Process

# Set recording duration
recordTime = 20

# Create record thread object
camRecord = Process(target = recordVideo, args = (recordTime, ))

# Thread actions
camRecord.start()
camRecord.join()
camRecord.close()
