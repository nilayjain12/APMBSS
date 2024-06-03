from flask import Flask, request, render_template, jsonify, redirect, session
from flask_cors import CORS
from utils.main import main
from pymongo import MongoClient
from bson import ObjectId
import bcrypt
import os
import requests
import base64
from config import config  # Import the config dictionary

app = Flask(
    __name__, 
    template_folder=os.path.join(config['BASE_DIR'], 'my-flask-app', 'app', 'templates'),
    static_folder=os.path.join(config['BASE_DIR'], 'my-flask-app', 'app', 'static')
)
CORS(app)  # This will enable CORS for all routes
app.secret_key = os.getenv('SECRET_KEY')

# MongoDB Configuration
client = MongoClient('mongodb+srv://nilayjain12:oF1dRfYhS59Cdxte@cluster0.paccwtr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['user_authentication']
users_collection = db['user_id_pass']

# Routes
@app.route('/')
def home():
    if 'username' in session:
        user_data = users_collection.find_one({'username': session['username']})
        if user_data:
            first_name = user_data.get('firstname', 'Guest')  # Get first name or default to 'Guest'
            return render_template('index.html', first_name=first_name)
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        username = request.form['username']
        password = request.form['password']

        existing_user = users_collection.find_one({'username': username})
        if existing_user:
            return 'Username already exists!'

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users_collection.insert_one({'firstname': first_name, 'lastname': last_name, 'username': username, 'password': hashed_password})
        session['username'] = username
        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing_user = users_collection.find_one({'username': username})
        if existing_user and bcrypt.checkpw(password.encode('utf-8'), existing_user['password']):
            session['username'] = username
            return redirect('/')
        else:
            return 'Invalid username/password combination!'

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/detect_mood', methods=['GET'])
def main_app():
    data = main()
    return jsonify(data)


# Add this function to get access token from Spotify
def get_spotify_access_token():
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    access_token = auth_response.json().get('access_token')
    return access_token

@app.route('/get_recommendations/<genre>', methods=['GET'])
def get_recommendations(genre):
    access_token = get_spotify_access_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    # You might need to adjust the endpoint and parameters based on the Spotify API documentation
    recommendations_url = f'https://api.spotify.com/v1/recommendations?seed_genres={genre}&limit=4'
    recommendations_response = requests.get(recommendations_url, headers=headers)
    recommendations = recommendations_response.json().get('tracks', [])
    track_ids = [track['id'] for track in recommendations]
    return jsonify(track_ids)


if __name__ == '__main__':
    app.run(port=81, debug=True)
