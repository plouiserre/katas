from GameOfLifeV2.grid import ALIVE, DEAD, Grid

simple_grid = [".*.", "**.", "..."]
complexe_grid = ["........", "...**...", "...**...", "........"]

def test_simple_grid_next_generation(): 
    assert calculate_futur_grid(simple_grid) ==  [[ALIVE, ALIVE, DEAD], [ALIVE, ALIVE, DEAD], [DEAD,DEAD,DEAD]]
    
def test_complexe_grid_next_generation():
    assert calculate_futur_grid(complexe_grid) ==  [[DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD], 
                                                  [DEAD, DEAD, DEAD, ALIVE, ALIVE, DEAD, DEAD, DEAD], 
                                                  [DEAD, DEAD, DEAD, ALIVE, ALIVE, DEAD, DEAD, DEAD], 
                                                  [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]]

def calculate_futur_grid(grid_datas): 
    grid = Grid(grid_datas)
    alive_cells = grid.determinate_alive_cells()
    all_status =[]
    for y, row in enumerate(grid_datas) : 
        status_row = []
        for x, column in enumerate(grid_datas[y]):
            number_neighbors = grid.count_alive_neighbors([y, x])
            status_cell = __get_alive_cells(alive_cells, [y, x])
            status_next_generation = grid.get_status_cell_next_round(status_cell, number_neighbors)
            status_row.append(status_next_generation)
        all_status.append(status_row)
    return all_status

def __get_alive_cells(alive_cells, coordonnates) :
    is_alive = False
    for cell in alive_cells :
        if cell[0] == coordonnates[0] and cell[1] == coordonnates[1]:
            is_alive = True 
            break
    if is_alive :
        return ALIVE 
    else : 
        return  DEAD