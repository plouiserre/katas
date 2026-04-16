from Bowling.score import Score

def test_one_turn_with_7_scores(): 
    turns = [[5,2]]
    assert(calculate_score(turns) == 7)

def test_one_turn_with_9_scores(): 
    turns = [[6,3]]
    assert(calculate_score(turns) == 9)

def test_eight_turns_with_nothing_special(): 
    turns = [[5,2], [6,3], [4,1], [0,6], [5,3], [4,3], [4,4], [2,6]]
    assert (calculate_score(turns) == 58)

def test_eight_turns_with_spare(): 
    turns = [[5,2], [6,3], [4,1], [0,6], [5,3], [4,3], [4,6], [2,6]]
    assert (calculate_score(turns) == 62)

def test_eight_turns_with_strike(): 
    turns = [[5,2], [6,3], [4,1], [0,6], [5,3], [4,3], [10,0], [2,6]]
    assert (calculate_score(turns) == 68)


#Improve when code is finished
def calculate_score(turns): 
    score = Score(turns)
    return score.Calculate()