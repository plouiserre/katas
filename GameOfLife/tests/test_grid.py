from GameOfLife.cell import DEAD, ALIVE
from GameOfLife.grid import Grid
from GameOfLife.locator import Locator

simple_grid = [".*.", "**.", "..."]
complexe_grid = ["........", "...**...", "...**...", "........"]


def test_get_first_dead_cell_content_simple_grid(): 
    assert content_retrieve([0], simple_grid) == [DEAD]
    
def test_get_first_dead_cell_content_complexe_grid(): 
    assert content_retrieve([0], complexe_grid) == [DEAD]
    
def test_get_second_alive_cell_content_simple_grid(): 
    assert content_retrieve([1], simple_grid) == [ALIVE]

def test_get_tenth_eleventh_twentieth_content_complexe_grid(): 
    assert content_retrieve([10,11, 20], complexe_grid) == [DEAD, ALIVE, ALIVE]


def content_retrieve(cells, grid) : 
    location = Locator(grid)
    grid = Grid(location, grid)
    states = grid.get_contents_cells(cells)
    return states