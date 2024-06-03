import cv2
import numpy as np
import tensorflow as tf
from cvzone.FaceMeshModule import FaceMeshDetector
import pickle
import cvzone
import os
from config import config  # Import the config dictionary

def get_last_mood_detected():
    # # Loading face emotion detection model
    # model_path = os.path.join(config['BASE_DIR'], 'data', 'models', 'Saved_Model', 'Final_model.h5')
    # mood_detection_face_model = tf.keras.models.load_model(model_path)

    # Loading behavior prediction model
    behaviour_model_path = os.path.join(config['BASE_DIR'], 'data', 'models', 'model_LR.pkl')
    with open(behaviour_model_path, 'rb') as f:
        behaviour_model = pickle.load(f)

    # Creating dictionary for mood detection
    mood_dict = {
        1: 'calm',
        2: 'energetic',
        3: 'happy',
        4: 'sad'
    }

    # Starting the webcam feed
    vs = cv2.VideoCapture(0)
    fps = cv2.getTickFrequency()

    # Initialize the start time
    start_time = cv2.getTickCount()

    # Variable to store the last mood detected
    last_mood_detected = None

    # Initialize FaceMeshDetector
    FMD = FaceMeshDetector()

    while True:
        # Check if 20 seconds have passed
        if (cv2.getTickCount() - start_time) / cv2.getTickFrequency() > 20:
            break

        ret, frame = vs.read()
        if not ret:  # Check if frame was successfully read
            break

        # frame = cv2.resize(frame, (960, 540))
        img, faces = FMD.findFaceMesh(frame)

        # Process each detected face
        if faces:
            face = faces[0]
            face_data = list(np.array(face).flatten())

            try:
                # Predict behavior using behavior prediction model
                result = behaviour_model.predict([face_data])
                mood = mood_dict[result[0]]
                last_mood_detected = mood
                cvzone.putTextRect(frame, mood, (250, 80))

            except Exception as e:
                pass

        cv2.imshow('Mood Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Stop the timer and display FPS information
    print("[INFO] approx. FPS: {:.2f}".format(fps / (cv2.getTickCount() - start_time)))

    # Release the video stream and close all OpenCV windows
    vs.release()
    cv2.destroyAllWindows()

    return last_mood_detected