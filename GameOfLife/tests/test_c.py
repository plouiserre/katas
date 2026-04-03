from GameOfLife.manipulator import Manipulator

simple_grid = [".*.", "**.", "..."]

    
def test_1():
    assert find_neighbourgs(0, simple_grid) == [[0, 1],[1, 0],[1, 1]]

def test_2(): 
    assert find_neighbourgs(4, simple_grid) == [[1,0],[1,2],[0,1],[2,1],[0,0],[0,2],[2,0],[2,2]]

def test_3(): 
    assert find_neighbourgs(5, simple_grid) == [[1,1],[0,2],[2,2],[0,1],[2,1]]

def test_4(): 
    assert find_neighbourgs(8, simple_grid) == [[2,1],[1,2],[1,1]]

def find_neighbourgs(position, grid): 
    mani = Manipulator(grid)
    neighbourgs_coordonnates = mani.locate_neighbourgs(position)
    return neighbourgs_coordonnates