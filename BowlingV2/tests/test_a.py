def test_1(): 
    score = "9 1|1 2|5 3|1 8|6 2|2 4|5 1|3 5|4 2|1 5"
    assert(translate_score(score)==[[9,1],[1,2],[5,3],[1,8],[6,2],[2,4],[5,1],[3,5],[4,2],[1,5]])

def test_2(): 
    score = "9 1|1 2|5 3|1 -|6 2|2 4|5 1|3 5|4 2|1 5"
    assert(translate_score(score)==[[9,1],[1,2],[5,3],[1,0],[6,2],[2,4],[5,1],[3,5],[4,2],[1,5]])

def test_3(): 
    score = "9 1|1 2|5 3|1 -|6 2|2 4|5 /|3 5|4 2|1 5"
    assert(translate_score(score)==[[9,1],[1,2],[5,3],[1,0],[6,2],[2,4],[5,5],[3,5],[4,2],[1,5]])

def test_4():
    score = "9 1|1 2|5 3|1 -|6 2|2 4|X |3 5|4 2|1 5"
    assert(translate_score(score)==[[9,1],[1,2],[5,3],[1,0],[6,2],[2,4],[10,0],[3,5],[4,2],[1,5]])

def test_5():
    score = "9 1|1 2|5 3|1 /|6 2|2 4|X |3 5|4 2|1 / 3"
    assert(translate_score(score)==[[9,1],[1,2],[5,3],[1,9],[6,2],[2,4],[10,0],[3,5],[4,2],[1,9,3]])


def translate_score(score):
    score_translate =[]
    score_elements = score.split("|")
    for element in score_elements :
        score_element_translate =[] 
        points = element.split(" ")
        for point_writing in points : 
            point_value = 0
            if point_writing == "/":
                point_value = __manage_spare_score(score_element_translate)
            elif point_writing == "X": 
                point_value = 10
            elif point_writing != "-" and point_writing != "":
                point_value = int(point_writing)            
            score_element_translate.append(point_value)
        score_translate.append(score_element_translate)
    return score_translate

def __manage_spare_score(score_element_translate): 
    last_point = score_element_translate[0]
    point_value = 10 - last_point
    return point_value