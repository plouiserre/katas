DEAD = 0
ALIVE = 1

class Grid : 
    def __init__(self, grid_data):
        self.grid_data = grid_data
        
    def get_status_cell_next_round(self, actual_status, alive_neighbourgs): 
        if actual_status == ALIVE and alive_neighbourgs < 2 : 
            return DEAD
        elif actual_status == ALIVE and alive_neighbourgs > 3 : 
            return DEAD
        elif actual_status == ALIVE and (alive_neighbourgs == 2 or alive_neighbourgs == 3): 
            return ALIVE
        elif actual_status == DEAD and alive_neighbourgs == 3 : 
            return ALIVE
        else : 
            return DEAD
        
    def determinate_alive_cells(self): 
        alive_cells = []
        for y, row in enumerate(self.grid_data) : 
            if ("*" in row) == False:
                continue
            else : 
                for x, column in enumerate(row): 
                    if column == "*" : 
                        alive_cells.append([y, x])
        return alive_cells