# Source: https://medium.com/propelland/raspberry-pi-tutorial-on-using-a-usb-camera-to-display-and-record-videos-with-python-a41c6938f89f

# Import libraries
import cv2
from videoCapture import VideoCaptureAsync
import time

# Set width and height of video
videoWidth = 1280
videoHeight = 720

# Initiate video capture object
capture = VideoCaptureAsync(src = 0, width = videoWidth, height = videoHeight)

# Initiate codec for Video recording object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

def recordVideo(duration):

    #start video capture
    capture.start()
    timeEnd = time.time() + duration

    frames = 0

    # Create an array to hold frames from capture
    images = []

    # Capture video for the defined duration
    while time.time() <= timeEnd:

        newFrame = capture.read()
        frames += 1
        images.append(newFrame)

        # Create a full screen video display
        cv2.namedWindow('image', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        if frames == 0 or frames % 5 == 0:
            
            frame = cv2.flip(frame, 180)            
            cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):

            break

    capture.stop()
    cv2.destroyAllWindows()
    
    fps = frames/duration

    print(frames)
    print(fps)
    print(len(images)) 

    out = cv2.VideoWriter('video.avi', fourcc, fps, (videoWidth, videoHeight))

    print("creating video")

    for i in range(len(images)):

        out.write(images[i])

    images = []
