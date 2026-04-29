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
            
    def count_frame_score(self, previous_frame): 
        if previous_frame == None : 
            return self.shots[0].points + self.shots[1].points
        elif self.position < 9 : 
            return self.__count_frame_score_before_last_frame(previous_frame)
        else : 
            last_frame_type = previous_frame.determine_frame_type()
            if last_frame_type == NORMAL:
                return self.__count_last_frame_score_when_previous_frame_is_normal()
            elif last_frame_type == SPARE : 
                return self.__count_last_frame_score_when_previous_frame_is_spare()
            elif last_frame_type == STRIKE : 
                return self.__count_last_frame_score_when_previous_frame_is_strike()

    def __count_frame_score_before_last_frame(self, previous_frame): 
        last_frame_type = previous_frame.determine_frame_type()
        if last_frame_type == NORMAL:
            return self.shots[0].points + self.shots[1].points
        elif last_frame_type == SPARE :
            return (self.shots[0].points * 2) + self.shots[1].points
        elif last_frame_type == STRIKE : 
            return (self.shots[0].points + self.shots[1].points) * 2
        
    def __count_last_frame_score_when_previous_frame_is_normal(self):
        two_shots_score = self.shots[0].points + self.shots[1].points
        if two_shots_score < 10 : 
            return two_shots_score
        else : 
            return self.shots[0].points + self.shots[1].points + self.shots[2].points
        
    def __count_last_frame_score_when_previous_frame_is_spare(self): 
        normal_two_score = self.shots[0].points + self.shots[1].points
        if normal_two_score < 10 : 
            return self.shots[0].points * 2 + self.shots[1].points
        else : 
            return self.shots[0].points * 2 + self.shots[1].points + self.shots[2].points
        
    def __count_last_frame_score_when_previous_frame_is_strike(self):
        normal_two_score = self.shots[0].points + self.shots[1].points
        if normal_two_score < 10 : 
            return (self.shots[0].points + self.shots[1].points ) *2 
        else : 
            return (self.shots[0].points + self.shots[1].points) *2  + self.shots[2].points
        