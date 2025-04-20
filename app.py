from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response
import json
import os
from functools import wraps
import jinja2
from datetime import datetime

app = Flask(__name__, static_folder='public', static_url_path='/static')
app.secret_key = 'your-secret-key-here'
app.url_map.strict_slashes = False  # Add this line to handle trailing slashes

JSON_FILE = './database/auth.json'

# Public funtion
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def load_users():
    with open('./database/auth.json', 'r') as f:
        return json.load(f)['data']


# Routes Login
@app.route('/', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('home'))
        
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = load_users()
        user = next((user for user in users if user['username'] == username and user['password'] == password), None)
        
        if user:
            session['logged_in'] = True
            session['user_id'] = user['id_petugas']
            session['username'] = user['username']
            return redirect(url_for('home'))
        else:
            return render_template('auth/index.html', error='Invalid username or password')
            
    return render_template('auth/index.html')

# Routes Home
@app.route('/home')
@login_required
def home():
    
    return render_template('home/index.html')

@app.route('/rey', methods=['GET', 'POST'])
@login_required
def rey():
    if request.method == 'POST':
        data = request.form['data']
        # Process the data as needed
        return redirect(url_for('home'))
    
    return render_template('rey/index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


