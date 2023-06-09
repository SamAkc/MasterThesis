'''
# TODO:
* Login-Seite
* Hauptseite mit
* Karte
* Annotationen
* Feedback?
* Visualisierung einbinden
'''

'''
# NOTE:
* Flask als Framework für Webapp mit Python (https://learn.microsoft.com/de-de/visualstudio/ide/quickstart-python?view=vs-2022)
* Python 3.11 als Python-Version, requirements.txt für Frameworks pflegen
# '''

from flask import Flask
from flask import url_for
from markupsafe import escape

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
def home():
    return "This is the homepage."

@app.route('/login')
def login():
    return "Here is the login page"

@app.route('/index')
def hello():
    # Render the page
    return "Hello Python!"

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    # print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)