class Game : 
    def __init__(self, notation, bowling_parser):
        self.notation = notation
        self.bowling_parser = bowling_parser
        self.score = 0
        self.is_spare = False 
        self.is_strike = False

    def Calculate(self):     
        turns = self.bowling_parser.parse_all_bowling_frames(self.notation)   
        for number_turn, turn in enumerate(turns) :    
            self.__manage_spare_or_strike(turn)        
            self.__determinate_is_spare_or_strike(turn)
            self.score += turn[0]
            self.score += turn[1]   
            if number_turn == 9: 
                self.__manage_last_turn(turn)
        return self.score
    
    def __manage_spare_or_strike(self, turn):
        if self.is_spare : 
            self.score += turn[0]
            self.is_spare = False
        elif self.is_strike : 
            self.score += turn[0]+turn[1] 
            self.is_strike= False

    def __determinate_is_spare_or_strike(self, turn): 
        if turn[0] == 10 : 
            self.is_strike = True
        elif turn[0]+turn[1] == 10 :            
            self.is_spare = True

    #rewriting this method
    def __manage_last_turn(self, turn):
        if self.is_spare or (self.is_strike and len(turn)==3): 
            self.score += turn[2]        