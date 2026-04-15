class Player : 
    def __init__(self, scores):
        self.scores = scores

    def calculate_score(self):
        return self.scores[0]+self.scores[1]