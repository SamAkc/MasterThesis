'''
# TODO:
* Login-Seite
* Hauptseite mit
* Karte
* Annotationen
* Feedback?
* Visualisierung einbinden
* DB wie umsetzen?
'''

'''
# NOTE:
* Flask als Framework für Webapp mit Python (https://learn.microsoft.com/de-de/visualstudio/ide/quickstart-python?view=vs-2022)
* Python 3.11 als Python-Version, requirements.txt für Frameworks pflegen
* Jinja als Template-Engine
# '''

from flask import Flask
from flask import render_template

# create an instance of class Flask
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('login.html', name=name)

# run application with command "flask --app <name_of_pythonfile without .py> run"