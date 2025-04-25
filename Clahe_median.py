from picamera2 import Picamera2
import cv2
import numpy as np

# Initialize the Pi Camera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)  # Adjust resolution if needed
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

# Create CLAHE object
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

while True:
    # Capture frame from Pi Camera
    frame = picam2.capture_array()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Apply CLAHE
    clahe_image = clahe.apply(gray)

    # Apply Median Filtering
    median_filtered = cv2.medianBlur(clahe_image, 5)  # Kernel size 5 (tune as needed)

    # Display the processed frames
    cv2.imshow("Original", gray)
    cv2.imshow("CLAHE Applied", clahe_image)
    cv2.imshow("Median Filtered", median_filtered)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cv2.destroyAllWindows()
picam2.stop()
