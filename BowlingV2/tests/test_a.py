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