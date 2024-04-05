from utils import face_emotion_detection
from utils import weather_emotion_detection
from random import choice

def decide_combined_mood():
    last_mood_detected = face_emotion_detection.get_last_mood_detected()
    predicted_mood = weather_emotion_detection.predict_mood_based_on_weather()

    genre_energetic_energetic = [
        'dance', 'dubstep', 'edm', 'electro', 'house', 'techno', 'trance', 'garage', 'emo', 'punk', 'punk-rock', 'grindcore', 'hard-rock'
    ]
    genre_energetic_happy = [
        'disco', 'k-pop', 'party', 'reggaeton', 'work-out', 'breakbeat', 'chicago-house', 'latin', 'post-dubstep', 'hip-hop', 'guitar'
    ]
    genre_energetic_calm = [
        'afrobeat', 'turkish', 'bossanova', 'club', 'dancehall', 'funk', 'power-pop', 'rock-n-roll', 'salsa', 'samba', 'minimal-techno'
    ]
    genre_energetic_sad = [
        'progressive-house', 'pop', 'alternative'
    ]
    genre_happy_happy = [
        'ska', 'summer', 'synth-pop', 'children', 'comedy', 'disney', 'folk', 'holidays', 'kids', 'alt-rock', 'forro', 'malay', 'road-trip'
    ]
    genre_happy_calm = [
        'world-music', 'synth-pop', 'trip-hop', 'mandopop', 'acoustic', 'bluegrass'
    ]
    genre_happy_sad = [
        'indie', 'indie-pop', 'tango', 'cantopop', 'show-tunes', 'country'
    ]
    genre_calm_calm = [
        'jazz', 'ambient', 'chill', 'minimal-techno', 'post-dubstep', 'cantopop', 'show-tunes', 'acoustic', 'brazil', 'romance', 'soul', 'spanish', 'indian'
    ]
    genre_calm_sad = [
        'blues', 'classical', 'piano', 'singer-songwriter', 'acoustic', 'british', 'opera', 'sleep'
    ]
    genre_sad = [
        'study', 'blues', 'jazz', 'sad', 'reggae', 'r-n-b', 'singer-songwriter', 'soul', 'sleep'
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


