import pytest
from models.score import Score
from models.score import to_dict
from models.score import from_dict, to_json
from datetime import datetime
import json
import os
def test_intialization_score():
    score = Score("billy", 80)
    assert score._player_name == "billy"
    assert score._score == 80
    assert hasattr(score, "_date")

def test_to_dict():
    score = Score("billy", 80)
    dict = to_dict(score)
    assert dict == {"player_name": "billy", "score": 80, "date":datetime.today().strftime('%m-%d %H:%M')}

def test_from_dict():
    score = from_dict({"player_name": "billy", "score": 80, 'date': datetime.today().strftime('%m-%d %H:%M')})
    if type(score) is Score:
        assert True
    else:
        assert False

def test_to_json():
    score = from_dict({"player_name": "billy", "score": 80, 'date': datetime.today().strftime('%m-%d %H:%M')})
    to_json(score)
    site_root = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(site_root, 'scores.json')
    with open(json_url, mode = 'r') as file:
        assert file.data.getvalue() == json.dumps({"player_name": "billy", "score": 80, 'date': datetime.today().strftime('%m-%d %H:%M')})
