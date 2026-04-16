class Score : 
    def __init__(self, turns):
        self.turns = turns

    def Calculate(self):
        score = 0
        for turn in self.turns : 
            score += turn[0]
            score += turn[1]
        return score