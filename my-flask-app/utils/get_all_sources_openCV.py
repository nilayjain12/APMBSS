import cv2

for i in range(10):  # Try indices from 0 to 9
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Source {i}: Webcam found")
        cap.release()
    else:
        print(f"Source {i}: No webcam found")