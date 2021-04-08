from flask import Flask, render_template, request, jsonify
import json
import os
from models.score import Score, to_json

app = Flask(__name__)

site_root = os.path.realpath(os.path.dirname(__file__)) #-- get root path
json_url = os.path.join(site_root, 'scores.json') #-- append scores.json to rooth path

@app.route("/")
def home():
    """
    Homepage which displays index.html
    """
    with open(json_url) as json_file:
        data = json.load(json_file)
    return render_template('index.html', var = data)

@app.route("/score", methods=['PUT'])
def score():
    """
    Gets scores from maze game
    """
    to_json(request.get_json())
    return f'', 200

@app.route("/json", methods=['GET'])
def _json():
    """
    Hosts data from scores.json which can be retrieved elsewhere
    """
    with open(json_url) as json_file:
        data = json.load(json_file)
    return f'{data}'

if __name__ == "__main__":
    app.run()
    