from GameOfLifeV2.grid import Grid

simple_grid = [".*.", "**.", "..."]
complexe_grid = ["........", "...**...", "...**...", "........"]


def test_1(): 
    assert count_alive_neighbourgs([0,0], simple_grid) == 3

def test_2():
    assert count_alive_neighbourgs([1,1], simple_grid) == 2

def test_3(): 
    assert count_alive_neighbourgs([3,3], complexe_grid) == 2

def count_alive_neighbourgs(coordonnates, grid_data): 
    alive_neighbourgs = 0
    grid = Grid(grid_data)
    alive_cells = grid.determinate_alive_cells()
    for cells in alive_cells : 
        y = coordonnates[0]
        x = coordonnates[1]
        cell_y = cells[0]
        cell_x = cells[1]
        for i in range(y - 1, y + 2 ) : 
            for j in range (x - 1 , x + 2 ) :
                same_coordonnates = y == i and x == j
                if i == cell_y and j == cell_x  and same_coordonnates == False: 
                    alive_neighbourgs +=1  
    return alive_neighbourgs