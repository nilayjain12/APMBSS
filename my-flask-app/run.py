from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from utils.main import main



app = Flask(__name__, template_folder = r'C:\Users\njain\OneDrive - Cal State Fullerton\SPRING 2024\CPSC 597 Project\Project\APMBSS\my-flask-app\app\templates', static_folder = r'C:\Users\njain\OneDrive - Cal State Fullerton\SPRING 2024\CPSC 597 Project\Project\APMBSS\my-flask-app\app\static')
CORS(app) # This will enable CORS for all routes

@app.route('/detect_mood', methods=['GET'])
def main_app():
    data = main()
    return jsonify(data)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=80, debug=True)
