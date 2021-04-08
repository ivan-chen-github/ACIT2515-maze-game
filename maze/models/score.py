import json
import requests
import ast
from datetime import datetime

class Score:
    """
    Creates score object that can be serialized to JSON

    """
    def __init__(self, player_name, score, date = 'Undefined'):
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
        if date == 'Undefined':
            self._date = datetime.today().strftime('%m-%d %H:%M')
        else:
            self._date = date

    def to_dict(self):
        """ Takes Score object and creates a dictionary

        """
        dict = {
            "player_name" : self._player_name,
            "score" : self._score,
            "date" : self.._date
        }
        return dict

"""def from_json(flask_url):
    Reads data from Flask server and creates nested list of scores

    :param flask_url: url of Flask server to get data from
    :type flask_url: str
    
    reply = requests.get(flask_url)
    payload = reply.content
    dict_payload = ast.literal_eval(payload.decode("UTF-8"))
    
    return dict_payload

def from_dict(dict):
    Reads data from a dictionary and creates object

    :param dict: dictionary to be read
    :type dict: dict
    
    obj =''
    if "date" in dict:
        obj = Score(
            player_name=dict["player_name"],
            score=dict["score"],
            date=dict["date"]
        )
    elif "date" not in dict:
        obj = Score(
            player_name=dict["player_name"],
            score=dict["score"])
    if type(obj) is Score:      
        return obj

def to_json(score_data):
    Takes score data and serializes into JSON file

    
    with open('scores.json') as json_file:
        data = json.load(json_file)
    with open('scores.json', mode='w') as f:
        data.append(json.loads(score_data))
        json.dump(data, f)"""
