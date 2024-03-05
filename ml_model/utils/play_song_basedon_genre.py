from getting_combined_mood import decide_combined_mood, last_mood_detected, predicted_mood
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import webbrowser


genre = decide_combined_mood(last_mood_detected, predicted_mood)


# Replace with your Spotify API credentials
CLIENT_ID = '5e72cefadf2242f185811400e85ae9cf'
CLIENT_SECRET = '7353a65633624c60996996693beba8e5'

# Set up Spotify API authentication
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_random_song(genre):
    # Get a list of tracks based on the selected genre
    tracks = sp.recommendations(seed_genres=[genre], limit=50)['tracks']

    # Select a random track
    random_track = random.choice(tracks)

    return random_track['name'], random_track['artists'][0]['name'], random_track['external_urls']['spotify']

def play_random_song(genre):
    # Get a random genre
    genre = genre
    print(f"Selected Genre: {genre}")

    # Get a random song from the selected genre
    song_name, artist_name, spotify_url = get_random_song(genre)
    print(f"Selected Song: {song_name} by {artist_name}")

    # Open the Spotify track page in the default web browser
    webbrowser.open(spotify_url)

print('Current Mood:\n', 'Face Mood: ', last_mood_detected, '\n', 'Weather Mood:', predicted_mood)
# Play a random song
play_random_song(genre)