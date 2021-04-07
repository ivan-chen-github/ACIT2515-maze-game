from flask import Flask, render_template, request, jsonify
import json
import os
from models.score import Score, to_json

app = Flask(__name__)
site_root = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(site_root, 'scores.json')

@app.route("/")
def home():
    with open(json_url) as json_file:
        data = json.load(json_file)
    return render_template('index.html', var = data)

@app.route("/score", methods=['PUT'])
def score():
    to_json(request.get_json())
    return 200

if __name__ == "__main__":
    app.run()