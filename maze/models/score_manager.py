import json
import csv
from .score import Score
import operator
class ScoreManager():
    def __init__(self):
        self._scores = {}
    
    @property
    def scores(self):
        return list(self._scores.values())
    
    def add_score(self, score):
        """ Add a new score

        Args:
            Score (ScoreItem): the item to add

        Raises:
            TypeError: if the item is not a score instance

        Returns:
            None"""
        
        self._scores[score.name] = score

    def remove_score(self, score_name):
        """ Removes score

        Args:
            score_name(str): name of the score you want to remove

        Returns:
            None
        """
        if score_name in self._scores:
            del self._scores[score_name]
    def get_scores(self):
        """ Will get all of the scores 
        return: string of scores
        """
        score_list = []
        for score in self._scores:
            score_list.append({"name": self._scores[score]._name, 'score' :self._scores[score].score})
        return score_list

    def serialize(self):
        print(self.get_scores())
        return {'scores': self.get_scores()}


    def __len__(self):
        """Returns the length of the dictionary """
        return len(self._scores)
    
    def to_json(self, json_file):
        convert_list = []
        for score in self._scores:
            convert = {"name": self._scores[score]._name, 'score' :self._scores[score].score}
            convert_list.append(convert)
        scores = {"scores": convert_list}
        print(scores)
        with open(json_file,'w') as file:
            file.write(str(scores))
    
    def from_json (self, json_file):
        with open(json_file, 'r') as file:
            json_data = json.load(file)
            for item in json_data:
                for value in json_data[item]:
                    score = Score(value['name'],value['score'])
                    self.add_score(score)


    def from_csv (self, csv_file):
        with open(csv_file, 'r') as file:
            data = csv.reader(file)
            data = list(data)
            for item in data:
                if item[1].isnumeric():
                    print(item[1])
                    score = Score(item[0], int(item[1]))
                    self.add_score(score)
