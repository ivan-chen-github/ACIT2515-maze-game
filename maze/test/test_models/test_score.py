import pytest
from models.score import Score
from models.score import from_dict
from datetime import datetime
import json
from unittest.mock import patch
def test_intialization_score():
    """ 
    test the initialization of the score
    """
    score = Score("billy", 80)
    assert score.player_name == "billy" #-- checks if its the right name
    assert score.score == 80 #-- checks if the score is 80
    assert hasattr(score, "date")

def test_to_dict():
    score = Score("billy", 80)
    dict = score.to_dict()
    assert dict == {"player_name": "billy", "score": 80, "date":datetime.today().strftime('%m-%d %H:%M')} #-- checks if it returns the dictionary in order

def test_from_dict():
    score = from_dict({"player_name": "billy", "score": 80, 'date': datetime.today().strftime('%m-%d %H:%M')}) #-- inserts a dictionary
    if type(score) is Score: #-- makes sure it is a score and if not it will fail
        assert True
    else:
        assert False

