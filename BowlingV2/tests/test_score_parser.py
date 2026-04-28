from BowlingV2.frame import Frame
from BowlingV2.score_parser import ScoreParser
from BowlingV2.shot import Shot

def test_notation_simple(): 
    notation = "9 1|1 2|5 3|1 8|6 2|2 4|5 1|3 5|4 2|1 5"
    frames = __translate_score_to_frame([[9,1],[1,2],[5,3],[1,8],[6,2],[2,4],[5,1],[3,5],[4,2],[1,5]])
    assert(translate_notation(notation)==frames)

def test_notation_with_null_shot(): 
    notation = "9 1|1 2|5 3|1 -|6 2|2 4|5 1|3 5|4 2|1 5"
    frames = __translate_score_to_frame([[9,1],[1,2],[5,3],[1,0],[6,2],[2,4],[5,1],[3,5],[4,2],[1,5]])
    assert(translate_notation(notation)== frames)

def test_notation_with_spare(): 
    notation = "9 1|1 2|5 3|1 -|6 2|2 4|5 /|3 5|4 2|1 5"
    frames = __translate_score_to_frame([[9,1],[1,2],[5,3],[1,0],[6,2],[2,4],[5,5],[3,5],[4,2],[1,5]])
    assert(translate_notation(notation)== frames)

def test_notation_with_spare_and_strike():
    notation = "9 1|1 2|5 3|1 -|6 2|2 4|X |3 5|4 2|1 5"
    frames = __translate_score_to_frame([[9,1],[1,2],[5,3],[1,0],[6,2],[2,4],[10,0],[3,5],[4,2],[1,5]])
    assert(translate_notation(notation)== frames)

def test_notation_with_spare_and_strike_and_last_frame_spare():
    notation = "9 1|1 2|5 3|1 /|6 2|2 4|X |3 5|4 2|1 / 3"
    frames = __translate_score_to_frame([[9,1],[1,2],[5,3],[1,9],[6,2],[2,4],[10,0],[3,5],[4,2],[1,9,3]])
    assert(translate_notation(notation)== frames)


def test_notation_with_spare_and_strike_and_last_frame_strike():
    notation = "9 1|1 2|5 3|1 /|6 2|2 4|X |3 5|4 2|X 3"
    frames = __translate_score_to_frame([[9,1],[1,2],[5,3],[1,9],[6,2],[2,4],[10,0],[3,5],[4,2],[10,3]])
    assert(translate_notation(notation) == frames)

def translate_notation(notation):
    parser = ScoreParser()
    frames = parser.parse_all_bowling_frames(notation)
    return frames

def __translate_score_to_frame(scores): 
    frames = []
    for idx, score in enumerate(scores) : 
        first_shot = Shot(score[0], 0)
        second_shot = Shot(score[1], 1)
        shots = [first_shot, second_shot]
        frame = Frame(idx, shots)
        frames.append(frame)
    return frames