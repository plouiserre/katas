DEAD = 0
ALIVE = 1

class Grid : 
    def __init__(self, grid_data):
        self.grid_data = grid_data

    def count_alive_neighbourgs(self, coordonnates): 
        alive_neighbourgs = 0
        alive_cells = self.determinate_alive_cells()
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