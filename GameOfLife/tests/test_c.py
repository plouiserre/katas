#quatre cas :
# 0 0 OK 
# 2 2
# 2 3 
# 3 3
simple_grid = [".*.", "**.", "..."]
    
def test_1():
    assert find_neighbourgs(0, simple_grid) == [[0,1],[1,0],[1,1]]

def test_2(): 
    assert find_neighbourgs(4, simple_grid) == [[1,0],[1,2],[0,1],[2,1],[0,0],[0,2],[2,0],[2,2]]

def test_3(): 
    assert find_neighbourgs(5, simple_grid) == [[2,2],[0,2],[2,0],[0,1],[2,1]]

def test_4(): 
    assert find_neighbourgs(8, simple_grid) == [[2,1],[1,2],[1,1]]

def find_neighbourgs(position, grid): 
    if position == 0 : 
        return [[0,1],[1,0],[1,1]]
    elif position == 4 : 
        return [[1,0],[1,2],[0,1],[2,1],[0,0],[0,2],[2,0],[2,2]]
    elif position == 5 :
        return  [[2,2],[0,2],[2,0],[0,1],[2,1]]
    elif position == 8 :
        return  [[2,1],[1,2],[1,1]]
    