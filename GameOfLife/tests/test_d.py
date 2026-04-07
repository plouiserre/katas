from GameOfLife.cell import DEAD, ALIVE
from GameOfLife.grid import Grid
from GameOfLife.locator import Locator

simple_grid = [".*.", "**.", "..."]
complexe_grid = ["........", "...**...", "...**...", "........"]

def test_1():    
    assert count_alive_neighbourgs_cells(1, simple_grid) == 2


def test_2(): 
    assert count_alive_neighbourgs_cells(11, complexe_grid) == 3
    

def count_alive_neighbourgs_cells(cell_number, grid_content):
    locator = Locator(grid_content)
    grid = Grid(locator, grid_content)
    return grid.count_alive_neighbourgs(cell_number)    