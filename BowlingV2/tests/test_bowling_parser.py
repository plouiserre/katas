from BowlingV2.bowling_parser import BowlingParser

def test_notation_simple(): 
    notation = "9 1|1 2|5 3|1 8|6 2|2 4|5 1|3 5|4 2|1 5"
    assert(translate_notation(notation)==[[9,1],[1,2],[5,3],[1,8],[6,2],[2,4],[5,1],[3,5],[4,2],[1,5]])

def test_notation_with_null_shot(): 
    notation = "9 1|1 2|5 3|1 -|6 2|2 4|5 1|3 5|4 2|1 5"
    assert(translate_notation(notation)==[[9,1],[1,2],[5,3],[1,0],[6,2],[2,4],[5,1],[3,5],[4,2],[1,5]])

def test_notation_with_spare(): 
    notation = "9 1|1 2|5 3|1 -|6 2|2 4|5 /|3 5|4 2|1 5"
    assert(translate_notation(notation)==[[9,1],[1,2],[5,3],[1,0],[6,2],[2,4],[5,5],[3,5],[4,2],[1,5]])

def test_notation_with_spare_and_strike():
    notation = "9 1|1 2|5 3|1 -|6 2|2 4|X |3 5|4 2|1 5"
    assert(translate_notation(notation)==[[9,1],[1,2],[5,3],[1,0],[6,2],[2,4],[10,0],[3,5],[4,2],[1,5]])

def test_notation_with_spare_and_strike_and_last_frame_spare():
    notation = "9 1|1 2|5 3|1 /|6 2|2 4|X |3 5|4 2|1 / 3"
    assert(translate_notation(notation)==[[9,1],[1,2],[5,3],[1,9],[6,2],[2,4],[10,0],[3,5],[4,2],[1,9,3]])


def test_notation_with_spare_and_strike_and_last_frame_strike():
    notation = "9 1|1 2|5 3|1 /|6 2|2 4|X |3 5|4 2|X 3"
    assert(translate_notation(notation)==[[9,1],[1,2],[5,3],[1,9],[6,2],[2,4],[10,0],[3,5],[4,2],[10,3]])

def translate_notation(notation):
    parser = BowlingParser()
    score = parser.parse_all_bowling_frames(notation)
    return score