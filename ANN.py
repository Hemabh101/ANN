import cv2
import time
import os


camera = cv2.VideoCapture(0)


if not camera.isOpened():
    print("Error opening camera")
    exit()

while True:
    
    ret, frame = camera.read()

    
    cv2.imshow('Camera', frame)

    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('p'):
        
        filename = f"photo_{time.strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)
        photo_path = os.path.abspath(filename)
        print("Photo saved at:", photo_path)
        break  


camera.release()




ref_images = [
    ("Your photo", cv2.imread(photo_path))
]

cap = cv2.VideoCapture(0)

should_detect = False  

while True:
    ret, frame = cap.read()

    if should_detect:
        for ref_image_name, ref_image in ref_images:
            result = cv2.matchTemplate(frame, ref_image, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            if max_val >= 0.8:
                print("I see:", ref_image_name)
                x, y = max_loc
                w, h = ref_image.shape[1], ref_image.shape[0]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break
    elif key == ord("y"):
        should_detect = True  

cap.release()


cv2.destroyAllWindows()
