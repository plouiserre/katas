simple_grid = [".*.", "**.", "..."]
complexe_grid = ["........", "...**...", "...**...", "........"]


def test_1(): 
    assert(get_alive_cells(simple_grid) == [[0,1], [1,0], [1,1]])

def test_2(): 
    assert(get_alive_cells(complexe_grid) == [[1,3], [1,4], [2,3], [2,4]])


def get_alive_cells(grid_data): 
    alive_cells = []
    for y, row in enumerate(grid_data) : 
        if ("*" in row) == False:
            continue
        else : 
            for x, column in enumerate(row): 
                if column == "*" : 
                    alive_cells.append([y, x])
    return alive_cells