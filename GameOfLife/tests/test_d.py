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
    cell_alive = 0
    locator = Locator(grid_content)
    neighbourgs = locator.locate_neighbourgs(cell_number)
    states = []
    for neighbourg in neighbourgs :
        content = __find_content_from_coordonnates(neighbourg[0], neighbourg[1], grid_content)
        state_cell = __convert_content_to_state_cell(content)
        states.append(state_cell)
    for state in states : 
        if state == ALIVE : 
            cell_alive += 1
    return cell_alive

def __find_content_from_coordonnates(y, x, grid_content): 
    content = ""
    for idx_g, cells in enumerate(grid_content) : 
        if y != idx_g : 
            continue
        else : 
            for idx_c, content_cell in enumerate(cells) : 
                if x != idx_c : 
                    continue
                else : 
                    content = content_cell
    return content

def __convert_content_to_state_cell(content) : 
    if content == "." :
        return DEAD 
    else : 
        return ALIVE