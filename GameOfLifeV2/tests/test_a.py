from GameOfLifeV2.grid import ALIVE, DEAD, Grid

simple_grid = [".*.", "**.", "..."]
complexe_grid = ["........", "...**...", "...**...", "........"]

def test_1() : 
    assert(draw_next_grid_generation(simple_grid) == ["**.", "**.", "..."])

def test_2(): 
    assert(draw_next_grid_generation(complexe_grid) == ["........", "...**...", "...**...", "........"])
 
def draw_next_grid_generation(grid_data):
    grid = Grid(grid_data)
    next_status = grid.generate_next_generation_grid()
    ihm = []
    for status_row in next_status :
        row_draw = ""            
        for status_column in status_row :  
            if status_column == DEAD : 
                row_draw += "."
            else : 
                row_draw += "*"
        ihm.append(row_draw)
    return ihm