from flask import Flask, request, render_template, jsonify, request, redirect, session
from flask_cors import CORS
from utils.main import main
from pymongo import MongoClient
from bson import ObjectId
import bcrypt



app = Flask(__name__, template_folder = r'C:\Users\njain\OneDrive - Cal State Fullerton\SPRING 2024\CPSC 597 Project\Project\APMBSS\my-flask-app\app\templates', static_folder = r'C:\Users\njain\OneDrive - Cal State Fullerton\SPRING 2024\CPSC 597 Project\Project\APMBSS\my-flask-app\app\static')
CORS(app) # This will enable CORS for all routes
app.secret_key = "A19@ahmnprsy123456789"

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
        return redirect('/')
    
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

if __name__ == '__main__':
    app.run(port=80, debug=True)
