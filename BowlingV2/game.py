class Game : 
    def __init__(self, notation, bowling_parser):
        self.notation = notation
        self.bowling_parser = bowling_parser
        self.score = 0
        self.is_spare = False 
        self.is_strike = False

    def Calculate(self):     
        frames = self.bowling_parser.parse_all_bowling_frames(self.notation)   
        for number_frame, frame in enumerate(frames) :    
            self.__manage_spare_or_strike(frame)        
            self.__determinate_is_spare_or_strike(frame)
            self.score += frame.shots[0].point
            self.score += frame.shots[1].point   
            if number_frame == 9: 
                self.__manage_last_turn(frame)
        return self.score
    
    def __manage_spare_or_strike(self, frame):
        if self.is_spare : 
            self.score += frame.shots[0].point
            self.is_spare = False
        elif self.is_strike : 
            self.score += frame.shots[0].point+frame.shots[1].point
            self.is_strike= False

    def __determinate_is_spare_or_strike(self, frame): 
        if frame.shots[0].point == 10 : 
            self.is_strike = True
        elif frame.shots[0].point+frame.shots[1].point == 10 :            
            self.is_spare = True

    #rewriting this method
    def __manage_last_turn(self, frame):
        if self.is_spare or (self.is_strike and len(frame.shots)==3): 
            self.score += frame.shots[2].point        