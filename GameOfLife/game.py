from GameOfLife.grid import Grid
from GameOfLife.status_cell import StatusCell

class Game : 
    def __init__(self, grid_data, max_turn):
        self.max_turn = max_turn
        self.grid_data = grid_data
        

    def Throw(self):
        all_evolutions = []
        all_evolutions.append(self.grid_data)
        for i in range(self.max_turn - 1) :
            status_cell = StatusCell()
            grid = Grid(self.grid_data, status_cell)
            evolution = grid.draw_next_generation()
            all_evolutions.append(evolution)
            self.grid_data = evolution
        return all_evolutions