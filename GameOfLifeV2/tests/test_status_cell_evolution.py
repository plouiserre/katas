from GameOfLifeV2.status_cell import ALIVE, DEAD, StatusCell

def test_status_cell_alive_is_dying_because_underpopulation():
    alive_cells = [[0,1],[1,0],[1,1],[2,2]]
    x = 2
    y = 2
    assert(next_state_cell(x, y, alive_cells)==DEAD)

def test_status_cell_alive_is_dying_because_overcrowding():
    alive_cells = [[0,0],[0,1],[0,2],[1,0],[1,1]]
    x = 1
    y = 0
    assert(next_state_cell(x, y, alive_cells)==DEAD)

def test_status_cell_alive_is_still_alive_because_no_underpopulation_or_overcrowding():
    alive_cells = [[0,1],[1,0],[1,1]]
    x = 1
    y = 1
    assert(next_state_cell(x, y, alive_cells)==ALIVE)

def test_status_cell_dead_is_alive_because_three_living_cells():
    alive_cells = [[0,1],[1,0],[1,1]]
    x = 0
    y = 0
    assert(next_state_cell(x, y, alive_cells)==ALIVE)


def next_state_cell(x, y, alive_cells):
    status_cell = StatusCell()
    return status_cell.evolve_next_generation(x, y, alive_cells)
