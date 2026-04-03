from GameOfLife.manipulator import Manipulator

#quatre cas :
# 0 0 OK 
# 2 2
# 2 3 
# 3 3
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
    coordonnates = mani.locate_cell(position)
    neighbourgs_coordonnates = __get_all_neighbourgs_coordonnates(coordonnates, grid)
    return neighbourgs_coordonnates
    # if position == 0 : 
    #     return [[0,1],[1,0],[1,1]]
    # elif position == 4 : 
    #     return [[1,0],[1,2],[0,1],[2,1],[0,0],[0,2],[2,0],[2,2]]
    # elif position == 5 :
    #     return  [[2,2],[0,2],[2,0],[0,1],[2,1]]
    # elif position == 8 :
    #     return  [[2,1],[1,2],[1,1]]
    
def __get_all_neighbourgs_coordonnates(coordonnates,grid) : 
    neighbourgs_coordonnates = []
    left_neighbourg = __find_left_neighbourg(coordonnates)
    right_neighbourg = __find_right_neighbourg(coordonnates, grid)
    top_neighbourg = __find_top_neighbourg(coordonnates)
    bottom_neighbourg = __find_bottom_neighbourg(coordonnates, grid)
    top_left_neighbourg = __find_top_left_neighbourg(coordonnates)
    top_right_neighbourg = __find_top_right_neighbourg(coordonnates, grid)
    bottom_left_neighbourg = __find_bottom_left_neighbourg(coordonnates, grid)
    bottom_right_neighbourg = __find_bottom_right_neighbourg(coordonnates, grid)
    all_coordonnates = [left_neighbourg, right_neighbourg, top_neighbourg, bottom_neighbourg, top_left_neighbourg, 
                        top_right_neighbourg, bottom_left_neighbourg, bottom_right_neighbourg]
    for coordonnates in all_coordonnates : 
        if coordonnates != None : 
            neighbourgs_coordonnates.append(coordonnates)
    return neighbourgs_coordonnates
    
def __find_left_neighbourg(coordonnates) : 
    y = coordonnates[0]
    x = coordonnates[1]
    new_x = x - 1
    if new_x >= 0 :
        return [y, new_x]
    else : 
        return None
    
def __find_right_neighbourg(coordonnates, grid) : 
    y = coordonnates[0]
    x = coordonnates[1]
    new_x = x + 1
    if new_x < len(grid[0]) : 
        return [y, new_x]
    else : 
        return None

def __find_top_neighbourg(coordonnates): 
    y = coordonnates[0]
    x = coordonnates[1]
    new_y = y - 1 
    if new_y >= 0 : 
        return [new_y, x]
    else : 
        return None
    
def __find_bottom_neighbourg(coordonnates, grid): 
    y = coordonnates[0]
    x = coordonnates[1]
    new_y = y + 1
    if new_y < len(grid): 
        return [new_y, x]
    else : 
        return None
    
def __find_top_left_neighbourg(coordonnates): 
    y = coordonnates[0]
    x = coordonnates[1]
    new_y = y - 1
    new_x = x - 1
    if new_y >= 0 and new_x >= 0:
        return [new_y, new_x]
    else : 
        return None
    
def __find_top_right_neighbourg(coordonnates, grid): 
    y = coordonnates[0]
    x = coordonnates[1]
    new_y = y - 1
    new_x = x + 1
    if new_y >= 0 and new_x < len(grid[0]):
        return [new_y, new_x]
    else : 
        return None
    
def __find_bottom_left_neighbourg(coordonnates, grid): 
    y = coordonnates[0]
    x = coordonnates[1]
    new_y = y + 1
    new_x = x - 1
    if new_y < len(grid) and new_x >= 0:
        return [new_y, new_x]
    else : 
        return None
    
def __find_bottom_right_neighbourg(coordonnates, grid): 
    y = coordonnates[0]
    x = coordonnates[1]
    new_y = y + 1
    new_x = x + 1
    if new_y < len(grid) and new_x < len(grid[0]):
        return [new_y, new_x]
    else : 
        return None