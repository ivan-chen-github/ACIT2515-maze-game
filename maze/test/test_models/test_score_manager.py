import pytest
from models.score_manager import ScoreManager
from models.score import Score
from unittest.mock import Mock

def test_add_score():
    ''' Test to see if add_score works'''
    manager = ScoreManager()
    score = Score("ben", 79)
    manager.add_score(score)
    assert manager.scores[0].player_name == 'ben'

def test_remove_score():
    """ test to see if it will remove the score"""
    manager = ScoreManager()
    manager.add_score (Score("ben", 79))
    manager.remove_score("ben")
    assert len(manager) == 0

def test_serialize():
    ''' will see if it returns the serialize'''
    manager = ScoreManager()
    manager.add_score(Score('ben',79))
    assert manager.serialize() == {'scores': [
        {"name": "ben", "score": 79},
    ]}