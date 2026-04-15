from GameOfLifeV2.grid import Grid

grid_data = ["...*", "***.", "*.*.", "****"]
grid = Grid(grid_data)
new_generation_grid = grid.draw_next_generation()
print(new_generation_grid)