NORMAL = 0
SPARE = 1
STRIKE = 2

class Frame : 
    def __init__(self, position, shots):
        self.position = position 
        self.shots = shots

    def __eq__(self, other):
        if other != None :
            return self.shots[0] == other.shots[0] and self.shots[1] == other.shots[1] and self.position == other.position
        else :
            return False
    
    def determine_frame_type(self): 
        score_shots = 0
        if self.shots[0].points == 10 : 
            return STRIKE
        else : 
            for idx, shot in enumerate(self.shots): 
                if idx < 2 :
                    score_shots += shot.points
            if score_shots == 10 : 
                return SPARE
            else : 
                return NORMAL