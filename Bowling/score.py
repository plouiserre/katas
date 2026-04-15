class Score : 
    def __init__(self, turns):
        self.turns = turns

    def Calculate(self):
        return self.turns[0]+self.turns[1]