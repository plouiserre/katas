class BowlingParser : 
    def __init__(self):
        pass

    def parse_all_bowling_frames(self, notation):
        score_translate =[]
        score_elements = notation.split("|")
        for element in score_elements :
            score_element_translate =[] 
            points = element.split(" ")
            for point_writing in points : 
                point_value = 0
                if point_writing == "/":
                    point_value = self.__manage_spare_score(score_element_translate)
                elif point_writing == "X": 
                    point_value = 10
                elif point_writing != "-" and point_writing != "":
                    point_value = int(point_writing)            
                score_element_translate.append(point_value)
            score_translate.append(score_element_translate)
        return score_translate
    
    def __manage_spare_score(self, score_element_translate): 
        last_point = score_element_translate[0]
        point_value = 10 - last_point
        return point_value