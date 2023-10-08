from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)

# CORS-Konfiguration mit spezifischen Optionen
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:5000", "methods": ["GET", "POST"], "headers": "Content-Type"}})

@app.route("/")
def home():
    return render_template('map.html')

@app.route("/feedback")
def feedback():
    return render_template('feedback.html')

@app.route("/sensorinspector")
def sensorinspector():
    return render_template('sensorinspector.html')    

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')
