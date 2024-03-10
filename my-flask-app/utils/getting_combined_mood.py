from utils import face_emotion_detection
from utils import weather_emotion_detection
from random import choice

def decide_combined_mood():
    last_mood_detected = face_emotion_detection.get_last_mood_detected()
    predicted_mood = weather_emotion_detection.predict_mood_based_on_weather()

    genre_energetic_energetic = [
        'edm',
        'electro',
        'electronic',
        'indie-pop',
        'j-dance',
        'j-pop',
        'j-rock',
        'latin',
        'party',
        'pop',
        'progressive-house',
        'rock',
        'techno',
        'trance',
        'world-music'
    ]
    genre_energetic_happy = [
        'disco', 'funk', 'happy'
    ]
    genre_energetic_calm = [
        'ambient', 'bossanova', 'chill'
    ]
    genre_energetic_sad = [
        'party', 'pop'
    ]
    genre_happy_happy = [
        'children',
        'disney',
        'indie-pop',
        'j-pop',
        'k-pop',
        'latino',
        'pop',
        'power-pop',
        'salsa',
        'samba',
        'summer',
        'swedish'
    ]
    genre_happy_calm = [
        'bossanova', 'chill', 'jazz', 'piano', 'soundtracks', 'study'
    ]
    genre_happy_sad = [
        'happy', 'study', 'soundtracks'
    ]
    genre_calm_calm = [
        'acoustic', 'bossanova', 'chill', 'classical', 'jazz', 'piano', 'sleep', 'soundtracks', 'study'
    ]
    genre_calm_sad = [
        'rainy-day', 'sad'
    ]
    genre_sad = [
        'blues', 'country', 'emo', 'gothic', 'grunge', 'metal-misc', 'metalcore', 'punk', 'punk-rock', 'rock-n-roll', 'trip-hop'
    ]

    # Logic to decide combined mood
    if (last_mood_detected == 'energetic' and predicted_mood == 'energetic'):
        return (choice(genre_energetic_energetic), last_mood_detected, predicted_mood)
    
    elif (last_mood_detected == 'energetic' and predicted_mood == 'happy') or (last_mood_detected == 'happy' and predicted_mood == 'energetic'):
        return (choice(genre_energetic_happy), last_mood_detected, predicted_mood)
    
    elif (last_mood_detected == 'energetic' and predicted_mood == 'calm') or (last_mood_detected == 'calm' and predicted_mood == 'energetic'):
        return (choice(genre_energetic_calm), last_mood_detected, predicted_mood)
    
    elif (last_mood_detected == 'energetic' and predicted_mood == 'sad') or (last_mood_detected == 'sad' and predicted_mood == 'energetic'):
        return (choice(genre_energetic_sad), last_mood_detected, predicted_mood)
    
    elif (last_mood_detected == 'happy' and predicted_mood == 'happy'):
        return (choice(genre_happy_happy), last_mood_detected, predicted_mood)
    
    elif (last_mood_detected == 'happy' and predicted_mood == 'calm') or (last_mood_detected == 'calm' and predicted_mood == 'happy'):
        return (choice(genre_happy_calm), last_mood_detected, predicted_mood)
    
    elif (last_mood_detected == 'happy' and predicted_mood == 'sad') or (last_mood_detected == 'sad' and predicted_mood == 'happy'):
        return (choice(genre_happy_sad), last_mood_detected, predicted_mood)
    
    elif (last_mood_detected == 'calm' and predicted_mood == 'calm'):
        return (choice(genre_calm_calm), last_mood_detected, predicted_mood)
    
    elif (last_mood_detected == 'calm' and predicted_mood == 'sad') or (last_mood_detected == 'sad' and predicted_mood == 'calm'):
        return (choice(genre_calm_sad), last_mood_detected, predicted_mood)
    elif (last_mood_detected == 'sad' and predicted_mood == 'sad'):
        return (choice(genre_sad), last_mood_detected, predicted_mood)
    else:
        return 'Cannot detect any genre! Playing a Random Song!! ENJOY!!'


