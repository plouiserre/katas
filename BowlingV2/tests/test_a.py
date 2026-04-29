from BowlingV2.frame import Frame
from BowlingV2.shot import Shot

NORMAL = 0
SPARE = 1
STRIKE = 2

def test_identify_normal_frame():
    frame = Frame(4, [Shot(2, 1), Shot(6, 2)])
    assert(identify_frame_type(frame) == NORMAL)

def test_identify_spare_frame(): 
    frame = Frame(5, [Shot(2, 1), Shot(8, 2)])
    assert(identify_frame_type(frame) == SPARE)

def test_identify_strike_frame(): 
    frame = Frame(6, [Shot(10, 1)])
    assert(identify_frame_type(frame) == STRIKE)

def identify_frame_type(frame):
    score_shots = 0
    if frame.shots[0].points == 10 : 
        return STRIKE
    else : 
        for shot in frame.shots: 
            score_shots += shot.points
        if score_shots == 10 : 
            return SPARE
        else : 
            return NORMAL