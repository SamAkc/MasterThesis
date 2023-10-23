from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('map.html')


@app.route("/feedback")
def feedback():
    return render_template('feedback.html')


# # Define a function to set the X-Frame-Options header for specific routes.
# def allow_iframe(response):
#     response.headers['X-Frame-Options'] = 'ALLOW-FROM *'


# @app.route("/sensorinspector")
# def sensorinspector():
#     response = make_response(render_template('sensorinspector.html'))
#     return allow_iframe(response)

@app.route("/sensorinspector")
def sensorinspector():
    return render_template('sensorinspector.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')
