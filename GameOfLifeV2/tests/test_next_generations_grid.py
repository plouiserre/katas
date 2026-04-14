from GameOfLifeV2.grid import ALIVE, DEAD, Grid

simple_grid = [".*.", "**.", "..."]
complexe_grid = ["........", "...**...", "...**...", "........"]

def test_simple_grid_next_generation(): 
    assert calculate_futur_grid(simple_grid) ==  [[ALIVE, ALIVE, DEAD], [ALIVE, ALIVE, DEAD], [DEAD,DEAD,DEAD]]
    
def test_complexe_grid_next_generation():
    assert calculate_futur_grid(complexe_grid) ==  [[DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD], 
                                                  [DEAD, DEAD, DEAD, ALIVE, ALIVE, DEAD, DEAD, DEAD], 
                                                  [DEAD, DEAD, DEAD, ALIVE, ALIVE, DEAD, DEAD, DEAD], 
                                                  [DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD]]

def calculate_futur_grid(grid_datas): 
    grid = Grid(grid_datas)    
    return grid.generate_next_generation_grid()