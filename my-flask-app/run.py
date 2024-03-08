from flask import Flask, jsonify
from flask_cors import CORS
from utils.play_song_basedon_genre import song_data

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

@app.route("/")
def main_app():
    return jsonify(song_data), 200

if __name__ == '__main__':
    app.run(port=81, debug=True)
