from GameOfLifeV2.grid import ALIVE, DEAD

def test_cell_alive_is_dying_because_underpopulation():
    alive_cells = [[0,1],[1,0],[1,1],[2,2]]
    x = 2
    y = 2
    assert(next_state_cell(x, y, alive_cells, ALIVE)==DEAD)

def test_cell_alive_is_dying_because_overcrowding():
    alive_cells = [[0,0],[0,1],[0,2],[1,0],[1,1]]
    x = 1
    y = 0
    assert(next_state_cell(x, y, alive_cells, DEAD)==DEAD)

def test_cell_alive_is_still_alive_because_no_underpopulation_or_overcrowding():
    alive_cells = [[0,1],[1,0],[1,1]]
    x = 1
    y = 1
    assert(next_state_cell(x, y, alive_cells, ALIVE)==ALIVE)

def test_cell_dead_is_alive_because_three_living_cells():
    alive_cells = [[0,1],[1,0],[1,1]]
    x = 0
    y = 0
    assert(next_state_cell(x, y, alive_cells, DEAD)==ALIVE)


def next_state_cell(x, y, alive_cells, status_cell):
    status_next_generation = ""
    number_neighbors = __count_alive_neighbors([y, x], alive_cells)
    status_next_generation = __get_status_cell_next_round(status_cell, number_neighbors)
    return status_next_generation

def __count_alive_neighbors(coordonnates, alive_cells): 
        alive_neighbors = 0
        for cells in alive_cells : 
            y = coordonnates[0]
            x = coordonnates[1]
            cell_y = cells[0]
            cell_x = cells[1]
            for i in range(y - 1, y + 2 ) : 
                for j in range (x - 1 , x + 2 ) :
                    same_coordonnates = y == i and x == j
                    if i == cell_y and j == cell_x  and same_coordonnates == False: 
                        alive_neighbors +=1  
        return alive_neighbors
        
def __get_status_cell_next_round(actual_status, alive_neighbors): 
        if actual_status == ALIVE and alive_neighbors < 2 : 
            return DEAD
        elif actual_status == ALIVE and alive_neighbors > 3 : 
            return DEAD
        elif actual_status == ALIVE and (alive_neighbors == 2 or alive_neighbors == 3): 
            return ALIVE
        elif actual_status == DEAD and alive_neighbors == 3 : 
            return ALIVE
        else : 
            return DEAD