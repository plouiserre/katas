from GameOfLife.cell import DEAD, ALIVE, Cell
from GameOfLife.grid import Grid
from GameOfLife.locator import Locator

simple_grid = [".*.", "**.", "..."]
complexe_grid = ["........", "...**...", "...**...", "........"]

def test_1():
    assert calculate_futur_grid(simple_grid) ==  [[ALIVE, ALIVE, DEAD], [ALIVE, ALIVE, DEAD], [DEAD,DEAD,DEAD]]

def test_2():
    assert calculate_futur_grid(complexe_grid) ==  [[DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD], 
                                                  [DEAD, DEAD, DEAD, ALIVE, ALIVE, DEAD, DEAD, DEAD], 
                                                  [DEAD, DEAD, DEAD, ALIVE, ALIVE, DEAD, DEAD, DEAD], 
                                                  [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]]


def calculate_futur_grid(grid_content): 
    locator = Locator(grid_content)
    grid = Grid(locator, grid_content)
    cell_number = 0
    news_state = []
    for idx_line, line in enumerate(grid_content) : 
        all_new_cells_line = []
        for idx_column, column in enumerate(line):
            alive_neighbourgs = grid.count_alive_neighbourgs(cell_number)
            actual_state = ""
            if column == "." :
                actual_state = DEAD
            else : 
                actual_state = ALIVE
            cell = Cell(actual_state, alive_neighbourgs)
            cell.evolve()
            all_new_cells_line.append(cell.status)
            cell_number +=1
        news_state.append(all_new_cells_line)
    return news_state