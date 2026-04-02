from GameOfLife.cell import Cell

DEAD = 0
ALIVE = 1

def test_alive_cell_with_no_alive_neighbourgs():
    assert next_generation_of(ALIVE, alive_neighbourgs = 0) == DEAD

def test_alive_cell_with_four_alive_neighbourgs(): 
    assert next_generation_of(ALIVE, alive_neighbourgs=4) == DEAD

def test_alive_cell_with_two_alive_neighbourgs():
    assert next_generation_of(ALIVE, alive_neighbourgs=2) == ALIVE

def test_alive_cell_with_one_alive_neighbourg(): 
    assert next_generation_of(ALIVE, alive_neighbourgs=1) == DEAD

def test_alive_cell_with_six_alive_neighbourgs():
    assert next_generation_of(ALIVE, alive_neighbourgs=6) == DEAD

def test_dead_cell_with_three_alive_neighbourgs(): 
    assert next_generation_of(DEAD, alive_neighbourgs= 3) == ALIVE

def test_dead_cell_with_two_alive_neighbourgs(): 
    assert next_generation_of(DEAD, alive_neighbourgs= 2) == DEAD

def test_dead_cell_with_four_alive_neighbourgs(): 
    assert next_generation_of(DEAD, alive_neighbourgs= 4) == DEAD

def next_generation_of(state, alive_neighbourgs): 
    cell = Cell(state, alive_neighbourgs)
    cell.evolve()
    return cell.status   