def test_1(): 
    score = [5,2]
    assert(count_score(score) == 7)

def test_2(): 
    score = [6,3]
    assert(count_score(score) == 9)


def count_score(points): 
    return points[0]+points[1]