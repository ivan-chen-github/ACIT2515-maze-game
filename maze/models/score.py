import pygame
import json
from datetime import date

class Score:
    def __init__(self, player_name, score, datetime):
        
        if type(score) is not int:
            raise ValueError("Invalid entry (score must be an integer)")
        elif score < 0:
            raise ValueError("Invalid entry (cannot be less than 0)")

        self._player_name = 'Player'
        self._score = score
        self._datetime = date.today()

def from_json(self, json_string):
    with open(json_string, 'r') as f:
        json_data = json.load(f)

        for entry in list(json_data):
            obj = Score(
                player_name=entry['player_name'],
                score=entry['score'],
                datetime=entry['datetime']
            )
            self.add_item(obj)

def from_dict(self, dict):
        obj = Score(
            player_name=dict['player_name'],
            score=dict['score'],
            datetime=dict['datetime']
        )

def to_json(self):
    n = Score()
    json_string = json.dumps(vars(n))

def to_dict(self):
    n = Score()
    vars(n)