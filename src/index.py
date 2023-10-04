from flask import Flask, render_template

app = Flask(__name__)

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
