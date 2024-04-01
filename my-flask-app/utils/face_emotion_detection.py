import cv2
import numpy as np
import tensorflow as tf

def get_last_mood_detected():
    # Loading face emotion detection model
    model_path = r'C:\Users\njain\OneDrive - Cal State Fullerton\SPRING 2024\CPSC 597 Project\Project\APMBSS\data\models\Saved_Model\Final_model.h5'
    mood_detection_face_model = tf.keras.models.load_model(model_path)

    # Creating dictionary for mood detection
    mood_dict = {
        0: 'calm',
        1: 'energetic',
        2: 'happy',
        3: 'sad'
    }

    global last_mood_detected
    # Starting the webcam feed
    vs = cv2.VideoCapture(3, cv2.CAP_DSHOW)
    fps = cv2.getTickFrequency()

    # Initialize the start time
    start_time = cv2.getTickCount()

    # Variable to store the last mood detected
    last_mood_detected = None

    while True:
        # Check if 20 seconds have passed
        if (cv2.getTickCount() - start_time) / cv2.getTickFrequency() > 20:
            break

        ret, frame = vs.read()
        if not ret: # Check if frame was successfully read
            break

        frame = cv2.resize(frame, (1920, 1080))
        face_detector = cv2.CascadeClassifier(r'C:\Users\njain\OneDrive - Cal State Fullerton\SPRING 2024\CPSC 597 Project\Project\Automated-Personalized-Mood-Based-Song-Selector\haarcascade_face_detection\haarcascade_frontalface_default.xml')
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_detector.detectMultiScale(gray_frame, scaleFactor=2.3, minNeighbors=5)

        # Process each detected face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
            roi_gray_frame = gray_frame[y: y + h, x: x + w]
            cropped_img = cv2.resize(roi_gray_frame, (224, 224))  # Resize to match model input shape
            cropped_img = cv2.cvtColor(cropped_img, cv2.COLOR_GRAY2RGB)  # Convert to RGB
            cropped_img = np.expand_dims(cropped_img, axis=0)  # Expand dimensions to match model input shape
            cropped_img = cropped_img / 255.0  # Normalize

            # Predict the mood
            mood_prediction = mood_detection_face_model.predict(cropped_img)
            max_index = np.argmax(mood_prediction)
            last_mood_detected = mood_dict[max_index] # Update the last mood detected
            cv2.putText(frame, mood_dict[max_index], (x + 5, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('Mood Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Stop the timer and display FPS information
    print("[INFO] approx. FPS: {:.2f}".format(fps / (cv2.getTickCount() - start_time)))

    # Release the video stream and close all OpenCV windows
    vs.release()
    cv2.destroyAllWindows()

    return last_mood_detected
