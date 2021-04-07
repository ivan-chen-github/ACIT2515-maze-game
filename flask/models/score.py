import json
from datetime import datetime

class Score:
    """
    Creates score object that can be serialized to JSON

    """
    def __init__(self, player_name, score):
        """ Initializes score

        :param player_name: name of player
        :type player_name: str

        :param score: total score of player
        :type score: int
        """
        if type(score) is not int:
            raise ValueError("Invalid entry (score must be an integer)")
        elif score < 0:
            raise ValueError("Invalid entry (cannot be less than 0)")

        self._player_name = str(player_name)
        self._score = int(score)
        self._date = datetime.today().strftime('%m-%d %H:%M')

def from_json(self, json_file):
    """ Reads data from JSON file and creates object

    :param json_file: file to be read
    :type json_file: .json
    """
    with open(json_file, 'r') as f:
        json_data = json.load(f)

        for entry in list(json_data):
            obj = Score(
                player_name=entry["player_name"],
                score=entry["score"],
                datetime=entry["datetime"]
            )
            
    return obj

def from_dict(self, dict):
    """ Reads data from a dictionary and creates object

    :param dict: dictionary to be read
    :type dict: dict
    """
    obj = Score(
        player_name=dict["player_name"],
        score=dict["score"],
        date=dict["date"]
    )

def to_json(self):
    """ Takes Score object and serializes into JSON file

    """
    with open('scores.json') as json_file:
        data = json.load(json_file)
    with open('scores.json', mode='w') as f:
        data.append(json.loads(self))
        json.dump(data, f)

def to_dict(self):
    """ Takes Score object and creates a dictionary

    """
    dict = {
        "player_name" : self._player_name,
        "score" : self._score,
        "date" : self._date
    }
    return dict
