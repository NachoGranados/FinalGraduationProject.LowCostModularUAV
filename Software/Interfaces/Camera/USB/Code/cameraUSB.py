# Source: https://raspberrypi-guide.github.io/electronics/using-usb-webcams

import cv2

cam = cv2.VideoCapture(0)

ret, image = cam.read()

cv2.imwrite("image_USB_Python.jpg", image)
cam.release()
cv2.destroyAllWindows()
