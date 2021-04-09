import json
import csv
import requests
import ast
from models.score import Score
import operator
class ScoreManager():
    """
    Keeps track of all the scores from the game
    """
    def __init__(self):
        self._scores = {} #-- empty dictionary to add the scores
    
    @property
    def scores(self):
        """
        scores will return all of the scores in the manager as list
        
        return: list of scores
        return type: list
        """
        return list(self._scores.values())
    
    def add_score(self, score):
        """ 
        adds the score to the dictionary
        
        params score: is the score to add to the dictionary
        type: score
        
        Returns: none
        """
        
        self._scores[score.player_name] = score

    def remove_score(self, score_name):
        """ 
        Removes score with the player name

        param score_name: is the name that you want to delete from the manager
        type score_name: str
        
        Returns: None
        """
        if score_name in self._scores:
            del self._scores[score_name]
    def get_scores(self):
        """ 
        Will get all of the scores that is in the dictionary
        
        return: list of scores
        return type: list
        """
        score_list = []
        for score in self._scores:
            score_list.append({"name": self._scores[score].player_name, 'score' :self._scores[score]._score})
        return score_list

    def serialize(self):
        """
        will get the list of scores from get_scores() and return the dictionary for it
        
        return: dictionary of the scores
        return type : dictionary
        """
        print(self.get_scores())
        return {'scores': self.get_scores()}


    def __len__(self):
        """
        Returns the number of scores that is in the dictionary
        
        return: the number of scores
        return type: int
        """
        return len(self._scores)
    
    def to_json(self, json_file):
        """
        serialize the scores and writes it to json_file
        
        param json_file: the name of the file you want to write the scores too
        type: string
        
        return: none
        """
        convert_list = []
        for score in self._scores: #-- serialize the scores
            convert = {"name": self._scores[score].player_name, 'score' :self._scores[score].score}
            convert_list.append(convert)
        scores = {"scores": convert_list}
        print(scores)
        with open(json_file,'w') as file: #-- opens the file and writes the serialized scores to it
            file.write(str(scores))
    
    def from_json(self, flask_url):
        """
        Reads data from Flask server and creates nested list of scores

        :param flask_url: url of Flask server to get data from
        :type flask_url: str
        
        :return dict_payload: is the dict of scores
        return type: dict
        """
        reply = requests.get(flask_url)
        payload = reply.content
        dict_payload = ast.literal_eval(payload.decode("UTF-8"))
        
        return dict_payload


    def from_csv (self, csv_file):
        """
        reads a csv files of scores then adds them to the dictionary
        
        params csv_file: the name of the file you want to read that has the scores in them
        type: string
        
        return: none
        """
        with open(csv_file, 'r') as file: #-- opens the csv file to read
            data = csv.reader(file) #-- gets the data that is in the file
            data = list(data) #-- makes it a list
            for item in data:
                if item[1].isnumeric(): #-- checks if the score is numeric
                    print(item[1])
                    score = Score(item[0], int(item[1])) #-- converts the data to a score object
                    self.add_score(score) #-- ads the score

