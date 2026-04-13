from GameOfLifeV2.grid import Grid
simple_grid = [".*.", "**.", "..."]
complexe_grid = ["........", "...**...", "...**...", "........"]


def test_get_alive_cell_for_simple_grid(): 
    assert(get_alive_cells(simple_grid) == [[0,1], [1,0], [1,1]])

def test_get_alive_cells_for_complexe_grid(): 
    assert(get_alive_cells(complexe_grid) == [[1,3], [1,4], [2,3], [2,4]])


def get_alive_cells(grid_data): 
    grid = Grid(grid_data)
    return grid.determinate_alive_cells()