from BowlingV2.bowling_parser import BowlingParser
from BowlingV2.score import Score

def test_one_turn_with_7_scores(): 
    notation = "5 2"    
    assert(calculate_score(notation) == 7)

def test_one_turn_with_9_scores(): 
    notation = "6 3"
    assert(calculate_score(notation) == 9)

def test_eight_turns_with_nothing_special(): 
    notation = "5 2|6 3|4 1|- 6|5 3|4 3|4 4|2 6"
    assert (calculate_score(notation) == 58)

def test_eight_turns_with_spare(): 
    notation = "5 2|6 3|4 1|- 6|5 3|4 3|4 /|2 6"
    assert (calculate_score(notation) == 62)

def test_eight_turns_with_strike(): 
    notation = "5 2|6 3|4 1|- 6|5 3|4 3|X |2 6"
    assert (calculate_score(notation) == 68)

def test_ten_turns_spare(): 
    notation = "5 2|6 3|4 1|- 6|5 3|4 3|4 4|2 6|1 5|8 / 6"
    assert (calculate_score(notation) == 80)

def test_ten_turns_strike(): 
    notation = "5 2|6 3|4 1|- 6|5 3|4 3|4 4|2 6|1 5|X 6"
    assert (calculate_score(notation) == 80)

def calculate_score(turns): 
    bowling_parser = BowlingParser()
    score = Score(turns, bowling_parser)
    return score.Calculate()