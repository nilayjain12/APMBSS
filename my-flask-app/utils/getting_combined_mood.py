from utils.face_emotion_detection import get_last_mood_detected
from utils.weather_emotion_detection import predict_mood_based_on_weather
from random import choice


def decide_combined_mood(last_mood_detected, predicted):

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
        'bossanova', 'chill', 'jazz', 'new age', 'piano', 'relax', 'soundtracks', 'study'
    ]
    genre_happy_sad = [
        'happy', 'study', 'soundtracks'
    ]
    genre_calm_calm = [
        'acoustic', 'bossanova', 'chill', 'classical', 'jazz', 'new age', 'piano', 'relax', 'sleep', 'soundtracks', 'study'
    ]
    genre_calm_sad = [
        'rainy-day', 'sad'
    ]
    genre_sad = [
        'blues', 'country', 'emo', 'gothic', 'grunge', 'metal-misc', 'metalcore', 'punk', 'punk-rock', 'rock-n-roll', 'trip-hop'
    ]

    # Logic to decide combined mood
    if (last_mood_detected == 'energetic' and predicted_mood == 'energetic'):
        return choice(genre_energetic_energetic)
    
    elif (last_mood_detected == 'energetic' and predicted_mood == 'happy') or (last_mood_detected == 'happy' and predicted_mood == 'energetic'):
        return choice(genre_energetic_happy)
    
    elif (last_mood_detected == 'energetic' and predicted_mood == 'calm') or (last_mood_detected == 'calm' and predicted_mood == 'energetic'):
        return choice(genre_energetic_calm)
    
    elif (last_mood_detected == 'energetic' and predicted_mood == 'sad') or (last_mood_detected == 'sad' and predicted_mood == 'energetic'):
        return choice(genre_energetic_sad)
    
    elif (last_mood_detected == 'happy' and predicted_mood == 'happy'):
        return choice(genre_happy_happy)
    
    elif (last_mood_detected == 'happy' and predicted_mood == 'calm') or (last_mood_detected == 'calm' and predicted_mood == 'happy'):
        return choice(genre_happy_calm)
    
    elif (last_mood_detected == 'happy' and predicted_mood == 'sad') or (last_mood_detected == 'sad' and predicted_mood == 'happy'):
        return choice(genre_happy_sad)
    
    elif (last_mood_detected == 'calm' and predicted_mood == 'calm'):
        return choice(genre_calm_calm)
    
    elif (last_mood_detected == 'calm' and predicted_mood == 'sad') or (last_mood_detected == 'sad' and predicted_mood == 'calm'):
        return choice(genre_calm_sad)
    elif (last_mood_detected == 'sad' and predicted_mood == 'sad'):
        return choice(genre_sad)
    else:
        return 'Cannot detect any genre! Play Random Song!! ENJOY!!'


last_mood_detected = get_last_mood_detected()
predicted_mood = predict_mood_based_on_weather()
decide_combined_mood(last_mood_detected, predicted_mood)