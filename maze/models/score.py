import json
from datetime import datetime
from typing import ByteString

class Score:
    def __init__(self, player_name, score, date):
        
        if type(score) is not int:
            raise ValueError("Invalid entry (score must be an integer)")
        elif score < 0:
            raise ValueError("Invalid entry (cannot be less than 0)")

        self._player_name = str(player_name)
        self._score = int(score)
        self._date = datetime.today().strftime('%Y-%m-%d')

def from_json(self, json_string):
    with open(json_string, 'r') as f:
        json_data = json.load(f)

        for entry in list(json_data):
            obj = Score(
                player_name=entry["player_name"],
                score=entry["score"],
                datetime=entry["datetime"]
            )
            self.add_item(obj)

def from_dict(self, dict):
        obj = Score(
            player_name=dict["player_name"],
            score=dict["score"],
            date=dict["date"]
        )

def to_json(self):
    string = f'{{"player_name" : {self._player_name}, "score" : {self._score}, "date" : {self._date}}}'
    return string

def to_dict(self):
    dict = {
        "player_name" : self._player_name,
        "score" : self._score,
        "date" : self._date
    }
    return dict
