from BowlingV2.frame import Frame
from BowlingV2.shot import Shot

class ScoreParser : 
    def __init__(self):
        pass

    def parse_all_bowling_frames(self, notation):
        frames =[]
        score_elements = notation.split("|")
        for idx_f, element in enumerate(score_elements) :            
            points = element.split(" ")
            shots = []
            for idx_s, point_writing in enumerate(points) : 
                point_value = 0
                if point_writing == "/":
                    point_value = self.__manage_spare_score(shots)
                elif point_writing == "X": 
                    point_value = 10
                elif point_writing != "-" and point_writing != "":
                    point_value = int(point_writing)    
                shots.append(Shot(point_value, idx_s))                        
            frame = Frame(idx_f, shots)
            frames.append(frame)
        return frames
    
    def __manage_spare_score(self, score_element_translate): 
        last_shot = score_element_translate[0]
        point_value = 10 - last_shot.points
        return point_value