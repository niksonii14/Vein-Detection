import cv2
from picamera2 import Picamera2 
import numpy as np

piCam = Picamera2()
piCam.preview_configuration.main.size=(1280,720) 
piCam.preview_configuration.main.format="RGB888"
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()

while True:
    frame=piCam.capture_array()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    min_val = np.min(gray_frame)
    max_val = np.max(gray_frame)

    stretched_frame = (gray_frame - min_val)*(255 / (max_val - min_val))
    stretched_frame = stretched_frame.astype(np.int8)
    cv2. imshow("picam - contrast stretched", stretched_frame)
    if cv2. waitKey(1)==ord('q'):
        break
    
cv2.destroyAllWindows()