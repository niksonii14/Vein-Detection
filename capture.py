import cv2
import time 
from picamera2 import Picamera2
import numpy as np

piCam = Picamera2()
piCam.preview_configuration.main.size=(1280,720) 
piCam.preview_configuration.main.format="RGB888"
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start ()

def capture_image():
    image = piCam.capture_array()
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    filename = "captured_image.jpg"
    cv2.imwrite(filename, gray_image)
    print(f"image saved as (filename]")
          
while True:
    frame=piCam.capture_array()
    gray_frame = cv2.ovtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow("piCam - Grayscale", gray_frame)
    key = cv2.waitKey(1) & 0xFF
    if key ==ord('q'):
        break
    elif key == ord('c'):
        capture_image()

cv2. destroyAllWindows()