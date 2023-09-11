from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def login():
    project_id = os.getenv('PROJECT_ID')
    return render_template('login.html', project_id=project_id)

@app.route('/home')
def home():
    project_id = os.getenv('PROJECT_ID')
    return render_template('home.html', project_id=project_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
