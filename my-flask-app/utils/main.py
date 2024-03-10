# Importing all the required modules
import play_song_basedon_genre

def main():
    # will call all the function and return the final result

    # method to fetch song_name, artist_name, spotify_url, track_id
    genre, last_mood_detected, predicted_mood, song_name, artist_name, spotify_url, track_id = play_song_basedon_genre.return_all_data()
    
    dict_data = {
        "genre": genre,
        "last_mood_detected": last_mood_detected,
        "predicted_mood": predicted_mood,
        "song_name": song_name,
        "artist_name": artist_name,
        "spotify_url": spotify_url,
        "track_id": track_id
    }

    return dict_data