from GameOfLife.cell import DEAD, ALIVE
from GameOfLife.locator import Locator

simple_grid = [".*.", "**.", "..."]
complexe_grid = ["........", "...**...", "...**...", "........"]


def test_1(): 
    assert content_retrieve([0], simple_grid) == [DEAD]

    
def test_2(): 
    assert content_retrieve([0], complexe_grid) == [DEAD]

    
def test_3(): 
    assert content_retrieve([1], simple_grid) == [ALIVE]

def test_4(): 
    assert content_retrieve([10,11, 20], complexe_grid) == [DEAD, ALIVE, ALIVE]


def content_retrieve(cells, grid) : 
    location = Locator(grid)
    states = []
    for cell in cells :
        cell_location = location.locate_cell(cell)
        content = __find_content_from_coordonnates(cell_location[0], cell_location[1], grid)
        state_cell = __convert_content_to_state_cell(content)
        states.append(state_cell)
    return states


def __find_content_from_coordonnates(y, x, grid): 
    content = ""
    for idx_g, cells in enumerate(grid) : 
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