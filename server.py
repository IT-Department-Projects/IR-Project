from gevent import monkey
import json
from flask import Flask, request, Response, render_template, abort, url_for
from flask_httpauth import HTTPDigestAuth
import time
import subprocess

# Flask Variables
app = Flask(__name__)
monkey.patch_all()

auth = HTTPDigestAuth()

app.config['SECRET_KEY'] = 'IR Project'

@app.route('/about')
# @auth.login_required
def about():
    return render_template('about.html')

@app.route('/team')
# @auth.login_required
def team():
    return render_template('team.html')

@app.route('/rank', methods=['POST'])
def rank():
    print(str(json.dumps(request.json)))
    query = request.json['query']

    subprocess.run(["python", "tfidf_query.py", query])
    process = subprocess.Popen(
        ["python", "cosine_similarity.py"], stdout=subprocess.PIPE)
    stdout = process.communicate()[0]
    print(stdout)

    return stdout

@app.route('/')
# @auth.login_required
def index():
    return render_template('index.html', name='Image Find')

# Main Method in the Server code
if __name__ == '__main__':
    # Set server address 0.0.0.0:5000/
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
