from GameOfLife.grid import Grid
from GameOfLife.status_cell import StatusCell

simple_grid = [".*.", "**.", "..."]
medium_grid = ["*.*", ".*.", "..*"]
complexe_grid = ["...**...", "..*.*...", "...**...", ".*......"]

def test_1():
    grid_evoluting  = __get_all_turns(simple_grid, 3)
    assert(grid_evoluting[0] == [".*.", "**.", "..."])
    assert(grid_evoluting[1] == ["**.", "**.", "..."])
    assert(grid_evoluting[2] == ["**.", "**.", "..."])

def test_2(): #il y a un soucis dans cette ligne!!!!!
    grid_evoluting = __get_all_turns(medium_grid, 3)
    assert(grid_evoluting[0] == ["*.*", ".*.", "..*"])
    assert(grid_evoluting[1] == [".*.", ".**", "..."])
    assert(grid_evoluting[2] == [".**", ".**", "..."])

def test_3(): 
    grid_evoluting = __get_all_turns(complexe_grid, 3)
    assert(grid_evoluting[0] == ["...**...", "..*.*...", "...**...", ".*......"])
    assert(grid_evoluting[1] == ["...**...", "..*..*..", "..***...","........"])
    assert(grid_evoluting[2] == ["...**...", "..*..*..", "..***...","...*...."])

def __get_all_turns(grid_data, max_turn):
    i = 0
    all_evolutions = []
    all_evolutions.append(grid_data)
    for i in range(max_turn - 1) :
        status_cell = StatusCell()
        grid = Grid(grid_data, status_cell)
        evolution = grid.draw_next_generation()
        all_evolutions.append(evolution)
        grid_data = evolution
    return all_evolutions