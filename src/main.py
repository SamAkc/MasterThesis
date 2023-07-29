import sqlite3
import lnetatmo
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('db/database.db')
    conn.row_factory = sqlite3.Row
    return conn
    
@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * from posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

# run application with command "flask --app <name_of_pythonfile without .py> run"