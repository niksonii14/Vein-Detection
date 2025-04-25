from picamera2 import Picamera2
import cv2
import time
import numpy as np

# Initialize the Pi Camera
piCam = Picamera2()
piCam.preview_configuration.main.size = (1280, 620)  # Adjust resolution if needed
piCam.preview_configuration.main.format = "RGB888"
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start ()

def capture_image():
    image = piCam.capture_array()
    gray_image = cv2.cvtColor (image, cv2.COLOR_RGB2GRAY)
    filename = "captured _image.jpg"
    cv2.imwrite(filename, gray_image)
    print(f"image saved as (filename)")

def record_video():
    filename = "captured video.avi"
    fourcc = cv2.VideoWriter_four (*'XVID')
    out = cv2.VideoWriter (filename, fourcc, 20.0, (1280, 720), False)
    start_time = time.time()
    while time.time() - start_time < 10:
        frame=piCam.capture_array()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        out.write(gray_frame)
        cv2.imshow("piCam - Recording...", gray_frame)
        if cv2.waitKey(1)==ord('q'):
            break
        
    out. release()
    print(f"Video saved as {filename}")

while True:
    frame=piCam.capture_array()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow("piCam - Grayscale", gray_frame)
    key= cv2.waitKey(1) & 0xFF
    if key==ord('q'):
        break
    elif key==ord('c'):
        capture_image()
    elif key == ord('y'):
        record_video()

cv2.destroyAllWindows()
