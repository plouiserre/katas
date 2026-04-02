import math 

simple_grid = [".*.", "**.", "..."]
complexe_grid = ["........", "...**...", "...**...", "........"]

def test_1():
    assert locate_me(0,simple_grid) == [0, 0]

def test_2(): 
    assert locate_me(4, simple_grid) == [1, 1]

def test_3(): 
    assert locate_me(8, simple_grid) == [2, 2]

def test_4(): 
    assert locate_me(0, complexe_grid) == [0,0]

def test_5(): 
    assert locate_me(12, complexe_grid) == [1,4]

def test_6(): 
    assert locate_me(28, complexe_grid) == [3,4]


def locate_me(cell_position, grid) :    
    coordonnates = []
    for i, line in enumerate(grid) :
        for j, column in enumerate(line) : 
            if cell_position == 0 : 
                coordonnates.append(i)
                coordonnates.append(j)
                break
            else : 
                cell_position =cell_position - 1
        if cell_position == 0 : 
            break         
    return coordonnates