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
        
        :param date: is the date that the score the player achieved
        :type date: date
        """
        if type(score) is not int:
            raise ValueError("Invalid entry (score must be an integer)")
        elif score < 0:
            raise ValueError("Invalid entry (cannot be less than 0)")

        self.player_name = str(player_name)
        self.score = int(score)
        if date == 'Undefined': #-- if it is the default value make self._date the current date and time
            self.date = datetime.today().strftime('%m-%d %H:%M')
        else:
            self.date = date #-- if there is a date inputed then it will set it to that date

    def to_dict(self):
        """ 
        Takes Score object and creates a dictionary
        
        return dict: returns a dictionary of that current score object
        return type: dictionary
        """
        dict = {
            "player_name" : self.player_name,
            "score" : self.score,
            "date" : self.date
        }
        return dict

def from_dict(dict):
    """
    Reads data from a dictionary and creates object
    
    :param dict: dictionary to be read
    :type dict: dict
    
    return obj: is the score object created by the information of dict
    :return type: score
    """
    obj =''
    if "date" in dict: #-- if date is included in the dictionary that was pass through then we will make that score with the date given
        obj = Score(
            player_name=dict["player_name"],
            score=dict["score"],
            date=dict["date"]
        )
    elif "date" not in dict: #--if it was not given a date then we will not pass in the date and score will make it the current date and time
        obj = Score(
            player_name=dict["player_name"],
            score=dict["score"])
    if type(obj) is Score: #-- makes sure the the variable is a Score object      
        return obj
