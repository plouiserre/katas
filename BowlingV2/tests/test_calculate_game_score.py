from BowlingV2.score_parser import ScoreParser
from BowlingV2.game import Game

def test_calculate_game_score_with_one_frame_with_7_points(): 
    notation = "5 2"    
    assert(calculate_score(notation) == 7)

def test_calculate_game_score_with_one_frame_with_9_points(): 
    notation = "6 3"
    assert(calculate_score(notation) == 9)

def test_calculate_game_score_with_eight_frames_with_nothing_special(): 
    notation = "5 2|6 3|4 1|- 6|5 3|4 3|4 4|2 6"
    assert (calculate_score(notation) == 58)

def test_calculate_game_score_with_eight_frames_with_one_spare(): 
    notation = "5 2|6 3|4 1|- 6|5 3|4 3|4 /|2 6"
    assert (calculate_score(notation) == 62)

def test_calculate_game_score_with_eight_frames_with_one_strike(): 
    notation = "5 2|6 3|4 1|- 6|5 3|4 3|X |2 6"
    assert (calculate_score(notation) == 68)

def test_calculate_all_game_score_finishing_by_a_spare(): 
    notation = "5 2|6 3|4 1|- 6|5 3|4 3|4 4|2 6|1 5|8 / 6"
    assert (calculate_score(notation) == 80)

def test_calculate_all_game_score_finishing_by_a_strike(): 
    notation = "5 2|6 3|4 1|- 6|5 3|4 3|4 4|2 6|1 5|X 6"
    assert (calculate_score(notation) == 80)

def calculate_score(turns): 
    score_parser = ScoreParser()
    game = Game(turns, score_parser)
    return game.Calculate()