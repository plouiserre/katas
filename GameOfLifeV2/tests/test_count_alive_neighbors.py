from GameOfLifeV2.grid import Grid

simple_grid = [".*.", "**.", "..."]
complexe_grid = ["........", "...**...", "...**...", "........"]

def test_count_alive_neighbors_first_cell_simple_grid(): 
    assert count_alive_neighbors([0,0], simple_grid) == 3

def test_count_alive_neighbors_fifth_cell_simple_grid():
    assert count_alive_neighbors([1,1], simple_grid) == 2

def test_count_alive_neighbors_twentieth_cell_complexe_grid(): 
    assert count_alive_neighbors([3,3], complexe_grid) == 2

def count_alive_neighbors(coordonnates, grid_data): 
    grid = Grid(grid_data)    
    return grid.count_alive_neighbors(coordonnates)