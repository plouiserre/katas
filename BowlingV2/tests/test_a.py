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

def test_count_last_frame_score_normal():
    frame = Frame(10, [Shot(2, 1), Shot(6, 2)])
    last_frame = Frame(9, [Shot(4,1), Shot(3,1)])
    assert (count_frame_score(frame, last_frame) == 8)

def test_count_last_frame_score_spare():
    frame = Frame(10, [Shot(2, 1), Shot(8, 2), Shot(4, 2)])
    last_frame = Frame(9, [Shot(4,1), Shot(3,1)])
    assert (count_frame_score(frame, last_frame) == 14)

def test_count_last_frame_score_strike():
    frame = Frame(10, [Shot(10, 1), Shot(8, 2), Shot(1, 2)])
    last_frame = Frame(9, [Shot(4,1), Shot(3,1)])
    assert (count_frame_score(frame, last_frame) == 19)

def test_count_last_frame_score_normal_with_previous_frame_spare():
    frame = Frame(10, [Shot(2, 1), Shot(6, 2)])
    last_frame = Frame(9, [Shot(4,1), Shot(6,1)])
    assert (count_frame_score(frame, last_frame) == 10)

def test_count_last_frame_score_spare_with_previous_frame_spare():
    frame = Frame(10, [Shot(2, 1), Shot(8, 2), Shot(6, 3)])
    last_frame = Frame(9, [Shot(4,1), Shot(6,1)])
    assert (count_frame_score(frame, last_frame) == 18)

def test_count_last_frame_score_strike_with_previous_frame_spare():
    frame = Frame(10, [Shot(10, 1), Shot(3, 2), Shot(6, 3)])
    last_frame = Frame(9, [Shot(4,1), Shot(6,1)])
    assert (count_frame_score(frame, last_frame) == 29)

def test_count_last_frame_score_normal_with_previous_frame_strike():
    frame = Frame(10, [Shot(2, 1), Shot(6, 2)])
    last_frame = Frame(9, [Shot(10,1)])
    assert (count_frame_score(frame, last_frame) == 16)

def test_count_last_frame_score_spare_with_previous_frame_strike():
    frame = Frame(10, [Shot(2, 1), Shot(8, 2), Shot(5, 2)])
    last_frame = Frame(9, [Shot(10,1)])
    assert (count_frame_score(frame, last_frame) == 25)

def test_count_last_frame_score_strike_with_previous_frame_strike():
    frame = Frame(10, [Shot(10, 1), Shot(3, 2), Shot(5, 2)])
    last_frame = Frame(9, [Shot(10,1)])
    assert (count_frame_score(frame, last_frame) == 31)

def count_frame_score(frame, previous_frame): 
    return frame.count_frame_score(previous_frame)