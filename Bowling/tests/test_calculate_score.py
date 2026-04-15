from Bowling.score import Score

def test_first_turn_with_7_scores(): 
    turns = [5,2]
    assert(calculate_score(turns) == 7)

def test_second_turn_with_9_scores(): 
    turns = [6,3]
    assert(calculate_score(turns) == 9)


def calculate_score(points): 
    score = Score(points)
    return score.Calculate()