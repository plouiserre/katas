DEAD = 0
ALIVE = 1

class CellEvolution : 
    def __init__(self, x, y, alive_cells, status_cell):
        self.x = x
        self.y = y
        self.alive_cells = alive_cells
        self.status_cell = status_cell

    def transform(self): 
        status_next_generation = ""
        number_neighbors = self.__count_alive_neighbors([self.y, self.x], self.alive_cells)
        status_next_generation = self.__get_status_cell_next_round(self.status_cell, number_neighbors)
        return status_next_generation
    
    def __count_alive_neighbors(self, coordonnates, alive_cells): 
        alive_neighbors = 0
        for cells in alive_cells : 
            y = coordonnates[0]
            x = coordonnates[1]
            cell_y = cells[0]
            cell_x = cells[1]
            for i in range(y - 1, y + 2 ) : 
                for j in range (x - 1 , x + 2 ) :
                    same_coordonnates = y == i and x == j
                    if i == cell_y and j == cell_x  and same_coordonnates == False: 
                        alive_neighbors +=1  
        return alive_neighbors
        
    def __get_status_cell_next_round(self, actual_status, alive_neighbors): 
            if actual_status == ALIVE and alive_neighbors < 2 : 
                return DEAD
            elif actual_status == ALIVE and alive_neighbors > 3 : 
                return DEAD
            elif actual_status == ALIVE and (alive_neighbors == 2 or alive_neighbors == 3): 
                return ALIVE
            elif actual_status == DEAD and alive_neighbors == 3 : 
                return ALIVE
            else : 
                return DEAD