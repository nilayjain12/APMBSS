import cv2
import numpy as np
import time
import tensorflow as tf

def get_last_mood_detected():
    # Loading the saved model
    model_load_dir = r'C:\Users\njain\OneDrive - Cal State Fullerton\SPRING 2024\CPSC 597 Project\Project\APMBSS\data\models\Saved_Model'
    loaded_model = tf.keras.models.load_model(model_load_dir)

    # Creating dictionary for mood detection
    mood_dict = {
        0: 'calm',
        1: 'energetic',
        2: 'happy',
        3: 'sad'
    }

    # Starting the webcam feed
    vs = cv2.VideoCapture(3)  # Capture from source 3
    fps = cv2.CAP_DSHOW
    time.sleep(2.0)  # Allow the camera sensor to warm up

    # Variable to store the last mood detected
    last_mood_detected = None

    # Start time for capturing frames
    start_time = time.time()

    while time.time() - start_time < 20:  # Capture frames for 20 seconds
        ret, frame = vs.read()
        if not ret:  # Check if frame was successfully read
            break

        frame = cv2.resize(frame, (1920, 1080))
        face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Detect faces in the frame
        faces = face_detector.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

        # Process each detected face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
            roi_color_frame = frame[y: y + h, x: x + w]  # Use color frame
            cropped_img = cv2.resize(roi_color_frame, (224, 224))  # Resize for model input
            cropped_img = np.expand_dims(cropped_img, axis=0)  # Add batch dimension

            # Preprocess the image (if necessary)
            # For example, you can normalize the pixel values
            cropped_img = cropped_img / 255.0

            # Predict the mood
            mood_prediction = loaded_model.predict(cropped_img)
            max_index = int(np.argmax(mood_prediction))
            last_mood_detected = mood_dict[max_index]  # Update the last mood detected
            cv2.putText(frame, mood_dict[max_index], (x + 5, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('Mood Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Check for 'q' keypress
            break

    # Release the video stream and close all OpenCV windows
    vs.release()
    cv2.destroyAllWindows()

    return last_mood_detected