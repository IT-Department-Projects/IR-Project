from gevent import monkey
import json
from flask import Flask, request, Response, render_template, abort, url_for
from flask_httpauth import HTTPDigestAuth
import time

# Flask Variables
app = Flask(__name__)
monkey.patch_all()

auth = HTTPDigestAuth()

app.config['SECRET_KEY'] = 'Image Find'

# Users to access app
# Users to be authenticated
users = {
    "aiman": "abdullah",
    "salman": "shah",
    "chowlek": "rashika"
}

# Authenticating users from Dictionary
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/about')
@auth.login_required
def about():
    return render_template('about.html')

@app.route('/team')
@auth.login_required
def team():
    return render_template('team.html')

@app.route('/')
@auth.login_required
def index():
    return render_template('index.html', name='Image Find')

# Main Method in the Server code
if __name__ == '__main__':
    # Set server address 0.0.0.0:5000/
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)