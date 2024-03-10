import getting_combined_mood
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import re
import os
from dotenv import load_dotenv

load_dotenv()

# Replace with your Spotify API credentials
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

# Set up Spotify API authentication
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_random_song(genre):
    # Get a list of tracks based on the selected genre
    tracks = sp.recommendations(seed_genres=[genre], limit=50)['tracks']

    # Select a random track
    random_track = random.choice(tracks)

    return random_track['name'], random_track['artists'][0]['name'], random_track['external_urls']['spotify']

def extract_track_id(url):
    match = re.search(r'/track/([a-zA-Z0-9]+)$', url)
    if match:
        return match.group(1)
    return None

def play_random_song(genre):
    # Get a random genre
    genre = genre
    print(f"Selected Genre: {genre}")

    # Get a random song from the selected genre
    song_name, artist_name, spotify_url = get_random_song(genre)
    # Extract and store the track ID in the variable
    track_id = extract_track_id(spotify_url)
    return (song_name, artist_name, spotify_url, track_id)

def return_all_data():
    genre, last_mood_detected, predicted_mood = getting_combined_mood.decide_combined_mood()
    # Play a random song
    song_name, artist_name, spotify_url, track_id = play_random_song(genre)

    return (genre, last_mood_detected, predicted_mood, song_name, artist_name, spotify_url, track_id)