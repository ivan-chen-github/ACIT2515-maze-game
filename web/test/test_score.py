import pytest
from models.score import Score
import json
import os

@pytest.fixture
def score():
    return Score("charlie", 10, 'January 1 1999')

def test_score_init(score):
    """checks if it has the attributes player_name, score and date with the right values"""
    hasattr(score, "player_name")
    hasattr(score, "score")
    hasattr(score, "date")
    score.player_name == "charlie"
    score.score == 10 
    score.date == 'January 1 1999'

def test_to_json():
    """ test to if there is a score.json file and compares to what should be in there"""
    root = os.path.dirname((os.path.dirname(__file__)))
    json_url = os.path.join(root, 'scores.json')
    with open(json_url, mode='r') as f:
        data = json.load(f)
        print(data[0])
        if data[0] == {'player_name': 'AAA', 'score': 90, 'date': '01-01 00:00'}:
            assert True
        else:
            assert False
