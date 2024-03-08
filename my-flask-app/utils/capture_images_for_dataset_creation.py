import cv2
import time
import os

# Initialize the camera
camera = cv2.VideoCapture(2)

# Check if the camera is opened correctly
if not camera.isOpened():
    raise IOError("Cannot open camera")

# Set the resolution to 1920x1080
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# Display a message to inform the user to press the key to capture images
print("Press 's' to capture an image")
file_path = r'C:\Users\njain\Desktop\sad images'

# Variable to keep track of the number of images captured
image_count = 0

while True:
    # Read the camera frame
    ret, frame = camera.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the grayscale frame
    cv2.imshow('Camera Feed', gray)
    
    # Check if the 's' key is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        # Construct the full file path
        full_file_path = os.path.join(file_path, f'image_{image_count}.png')
        # Save the current frame
        cv2.imwrite(full_file_path, frame)
        # Increment the image count
        image_count += 1
        # Wait for a short period to ensure the camera captures different frames
        time.sleep(0.9)
        print(f"Image {image_count} saved.")
    
    # Break the loop on 'q' key press
    if key == ord('q'):
        break

# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()
