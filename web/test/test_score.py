import pytest
from models.score import Score
import json
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
    with open('../scores.json', mode='r') as f:
        data = json.load(f)
        data = json.dumps(data)
        if data == '[{"player_name": "AAA", "score": 90, "date": "01-01 00:00"}, {"player_name": "BBB", "score": 85, "date": "01-01 00:00"}, {"player_name": "DDD", "score": 70, "date": "01-01 00:00"}, {"player_name": "CCC", "score": 80, "date": "01-01 00:00"}, {"player_name": "EEE", "score": 60, "date": "01-01 00:00"}, {"player_name": "FFF", "score": 50, "date": "01-01 00:00"}, {"player_name": "LENKA", "score": 100, "date": "01-01 00:00"}, {"player_name": "BRAD", "score": 108, "date": "04-08 21:27"}]':
            assert True
        else: 
            assert False