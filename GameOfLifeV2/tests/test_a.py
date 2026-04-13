from GameOfLifeV2.grid import Grid

simple_grid = [".*.", "**.", "..."]
complexe_grid = ["........", "...**...", "...**...", "........"]

def test_1(): 
    assert count_alive_neighbourgs([0,0], simple_grid) == 3

def test_2():
    assert count_alive_neighbourgs([1,1], simple_grid) == 2

def test_3(): 
    assert count_alive_neighbourgs([3,3], complexe_grid) == 2

def count_alive_neighbourgs(coordonnates, grid_data): 
    grid = Grid(grid_data)    
    return grid.count_alive_neighbourgs(coordonnates)