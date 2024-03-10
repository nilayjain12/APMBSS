from flask import Flask, jsonify, render_template
from flask_cors import CORS
from utils.play_song_basedon_genre import song_data
import json

app = Flask(__name__, template_folder = r'C:\Users\njain\OneDrive - Cal State Fullerton\SPRING 2024\CPSC 597 Project\Project\APMBSS\my-flask-app\app\templates', static_folder = r'C:\Users\njain\OneDrive - Cal State Fullerton\SPRING 2024\CPSC 597 Project\Project\APMBSS\my-flask-app\app\static')
CORS(app) # This will enable CORS for all routes

@app.route('/', methods = ['GET'])
def main_app():

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=80, debug=True)
