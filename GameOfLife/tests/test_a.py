DEAD = 0
ALIVE = 1

def test_1():
    assert next_generation_of(ALIVE, alive_neighbourgs = 0) == DEAD

def test_2(): 
    assert next_generation_of(ALIVE, alive_neighbourgs=4) == DEAD

def test_3():
    assert next_generation_of(ALIVE, alive_neighbourgs=2) == ALIVE

def test_4(): 
    assert next_generation_of(ALIVE, alive_neighbourgs=1) == DEAD

def test_5():
    assert next_generation_of(ALIVE, alive_neighbourgs=6) == DEAD

def test_6(): 
    assert next_generation_of(DEAD, alive_neighbourgs= 3) == ALIVE

def test_7(): 
    assert next_generation_of(DEAD, alive_neighbourgs= 2) == DEAD

def test_8(): 
    assert next_generation_of(DEAD, alive_neighbourgs= 2) == DEAD

def next_generation_of(state, alive_neighbourgs): 
    if state == ALIVE : 
        if alive_neighbourgs < 2 or alive_neighbourgs > 3 :
            return DEAD
        else : 
            return ALIVE
    else : 
        if alive_neighbourgs == 3 :
            return ALIVE 
        else : 
            return DEAD