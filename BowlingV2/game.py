from BowlingV2.frame import SPARE, STRIKE

class Game : 
    def __init__(self, notation, bowling_parser):
        self.notation = notation
        self.bowling_parser = bowling_parser
        self.score = 0
        self.previous_frame = None

    def Calculate(self):     
        frames = self.bowling_parser.parse_all_bowling_frames(self.notation)   
        for frame in frames :    
            self.score += frame.count_frame_score(self.previous_frame)
            self.previous_frame = frame
        return self.score       