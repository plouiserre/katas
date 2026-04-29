from BowlingV2.frame import Frame, NORMAL, SPARE, STRIKE
from BowlingV2.shot import Shot

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
    return frame.determine_frame_type()

def test_count_frame_score_normal_with_no_previous_last_frame(): 
    frame = Frame(4, [Shot(2, 1), Shot(6, 2)])
    assert (count_frame_score(frame, None) == 8)

def test_count_frame_score_normal_with_previous_last_frame_normal(): 
    frame = Frame(4, [Shot(2, 1), Shot(6, 2)])
    last_frame = Frame(3, [Shot(4,1), Shot(3,1)])
    assert (count_frame_score(frame, last_frame) == 8)

def test_count_frame_score_normal_with_previous_last_frame_spare(): 
    frame = Frame(4, [Shot(2, 1), Shot(6, 2)])
    last_frame = Frame(3, [Shot(4,1), Shot(6,1)])
    assert (count_frame_score(frame, last_frame) == 10)

def test_count_frame_score_normal_with_previous_last_frame_strike(): 
    frame = Frame(4, [Shot(2, 1), Shot(6, 2)])
    last_frame = Frame(3, [Shot(10,1)])
    assert (count_frame_score(frame, last_frame) == 16)

def count_frame_score(frame, last_frame): 
    if last_frame == None : 
        return frame.shots[0].points + frame.shots[1].points
    else : 
        last_frame_type = last_frame.determine_frame_type()
        if last_frame_type == NORMAL:
            return frame.shots[0].points + frame.shots[1].points
        elif last_frame_type == SPARE :
            return (frame.shots[0].points * 2) + frame.shots[1].points
        elif last_frame_type == STRIKE : 
            return (frame.shots[0].points + frame.shots[1].points) * 2