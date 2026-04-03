import math 
from GameOfLife.locator import Locator


simple_grid = [".*.", "**.", "..."]
complexe_grid = ["........", "...**...", "...**...", "........"]

def test_locate_first_case_small_grid():
    assert locate_me(0,simple_grid) == [0, 0]

def test_locate_fourth_case_small_grid(): 
    assert locate_me(4, simple_grid) == [1, 1]

def test_locate_eighth_case_small_grid(): 
    assert locate_me(8, simple_grid) == [2, 2]

def test_locate_first_case_big_grid(): 
    assert locate_me(0, complexe_grid) == [0,0]

def test_locate_twelfth_case_small_grid(): 
    assert locate_me(12, complexe_grid) == [1,4]

def test_locate_twenty_eighth_case_small_grid(): 
    assert locate_me(28, complexe_grid) == [3,4]


def locate_me(cell_position, grid) :    
    locator = Locator(grid)
    coordonnates = locator.locate_cell(cell_position)
    return coordonnates

def test_first_cell_neighbourg():
    assert find_neighbourgs(0, simple_grid) == [[0, 1],[1, 0],[1, 1]]

def test_fourth_cell_neighbourgs(): 
    assert find_neighbourgs(4, simple_grid) == [[1,0],[1,2],[0,1],[2,1],[0,0],[0,2],[2,0],[2,2]]

def test_fifth_neighbourgs(): 
    assert find_neighbourgs(5, simple_grid) == [[1,1],[0,2],[2,2],[0,1],[2,1]]

def test_eighth_neighbourgs(): 
    assert find_neighbourgs(8, simple_grid) == [[2,1],[1,2],[1,1]]

def find_neighbourgs(position, grid): 
    locator = Locator(grid)
    neighbourgs_coordonnates = locator.locate_neighbourgs(position)
    return neighbourgs_coordonnates