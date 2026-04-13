from GameOfLifeV2.grid import ALIVE, DEAD, Grid

def test_cell_is_alive_with_one_neighbourg():
    assert(is_cell_alive(ALIVE, 1) == DEAD)

def test_is_alive_with_four_neighbourgs(): 
    assert(is_cell_alive(ALIVE, 4) == DEAD)

def test_is_alive_with_two_neighbourgs(): 
    assert(is_cell_alive(ALIVE, 2) == ALIVE)

def test_is_alive_with_three_neighbourgs(): 
    assert(is_cell_alive(ALIVE, 3) == ALIVE)

def test_is_dead_with_three_neighbourgs(): 
    assert(is_cell_alive(DEAD, 3) == ALIVE)

def test_is_dead_with_two_neighbourgs(): 
    assert(is_cell_alive(DEAD, 2) == DEAD)

def test_is_dead_with_six_neighbourgs(): 
    assert(is_cell_alive(DEAD, 6) == DEAD)

def is_cell_alive(actual_status, alive_neighbourgs):
    grid = Grid()
    return grid.get_status_cell_next_round(actual_status, alive_neighbourgs)