from GameOfLifeV2.grid import Grid
from GameOfLifeV2.status_cell import StatusCell

simple_grid = [".*.", "**.", "..."]
medium_grid = ["*.*", ".*.", "..*"]
complexe_grid = ["........", "...**...", "...**...", "........"]

def test_draw_first_generation_simple_grid() : 
    assert(draw_next_grid_generation(simple_grid) == ["**.", "**.", "..."])

def test_draw_first_generation_medium_grid() : 
    assert(draw_next_grid_generation(medium_grid) == [".*.", ".**", "..."])

def test_draw_first_generation_complexe_grid(): 
    assert(draw_next_grid_generation(complexe_grid) == ["........", "...**...", "...**...", "........"])

def draw_next_grid_generation(grid_data):
    status_cell = StatusCell()
    grid = Grid(grid_data, status_cell)
    return grid.draw_next_generation()