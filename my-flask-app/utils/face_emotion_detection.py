import cv2
import pickle
import numpy as np
from utils.threaded_video_stream import *
import time

# Loading face emotion detection model
face_model_pickle_file_path = r'C:\Users\njain\OneDrive - Cal State Fullerton\SPRING 2024\CPSC 597 Project\Project\APMBSS\data\models\mood_detection_model.pkl'

with open(face_model_pickle_file_path, 'rb+') as file:
    mood_detection_face_model = pickle.load(file)

# Creating dictionary for mood detection
mood_dict = {
    0: 'calm',
    1: 'energetic',
    2: 'happy',
    3: 'sad'
}

def get_last_mood_detected():
    global last_mood_detected
    # Starting the webcam feed
    vs = WebcamVideoStream(src=3).start()
    fps = FPS().start()

    # Initialize the start time
    start_time = time.time()

    # Variable to store the last mood detected
    last_mood_detected = None

    while True:
        # Check if 20 seconds have passed
        if time.time() - start_time > 20:
            break

        frame = vs.read()
        if frame is None:
            break

        frame = cv2.resize(frame, (640, 360))
        face_detector = cv2.CascadeClassifier(r'C:\Users\njain\OneDrive - Cal State Fullerton\SPRING 2024\CPSC 597 Project\Project\Automated-Personalized-Mood-Based-Song-Selector\haarcascade_face_detection\haarcascade_frontalface_default.xml')
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_detector.detectMultiScale(gray_frame, scaleFactor=2.3, minNeighbors=5)

        # Process each detected face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
            roi_gray_frame = gray_frame[y: y + h, x: x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)

            # Predict the mood
            mood_prediction = mood_detection_face_model.predict(cropped_img)
            max_index = int(np.argmax(mood_prediction))
            last_mood_detected = mood_dict[max_index] # Update the last mood detected
            cv2.putText(frame, mood_dict[max_index], (x + 5, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('Mood Detection', frame)
        fps.update()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Stop the timer and display FPS information
    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # Release the video stream and close all OpenCV windows
    vs.stop()
    cv2.destroyAllWindows()

    return last_mood_detected