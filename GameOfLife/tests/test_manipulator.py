import math 
from GameOfLife.manipulator import Manipulator


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
    manipulator = Manipulator(grid)
    coordonnates = manipulator.locate_cell(cell_position)
    return coordonnates