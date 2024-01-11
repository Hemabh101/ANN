import cv2
import time
import os

# Access the webcam
camera = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not camera.isOpened():
    print("Error opening camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Display the resulting frame
    cv2.imshow('Camera', frame)

    # Wait for 'p' key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord('p'):
        # Take a photo when 'p' is pressed
        filename = f"photo_{time.strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)
        photo_path = os.path.abspath(filename)
        print("Photo saved at:", photo_path)
        break  # Exit the loop after taking the photo

# Release the camera and close the window
camera.release()
cv2.destroyAllWindows()
