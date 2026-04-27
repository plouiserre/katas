DEAD = 0
ALIVE = 1

class StatusCell : 
    def __init__(self):
       pass

    def evolve_next_generation(self, x, y, alive_cells):
        self.x = x
        self.y = y
        self.alive_cells = alive_cells
        status_next_generation = ""
        self.actual_status = self.__get_alive_cells([y, x])                
        number_neighbors = self.__count_alive_neighbors([self.y, self.x])
        status_next_generation = self.__get_status_cell_next_round(number_neighbors)
        return status_next_generation

    def __get_alive_cells(self, coordonnates) :
        is_alive = False
        for cell in self.alive_cells :
            if cell[0] == coordonnates[0] and cell[1] == coordonnates[1]:
                is_alive = True 
                break
        if is_alive :
            return ALIVE 
        else : 
            return  DEAD  
    
    def __count_alive_neighbors(self, coordonnates): 
        alive_neighbors = 0
        for cells in self.alive_cells : 
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
        
    def __get_status_cell_next_round(self, alive_neighbors): 
            if self.actual_status == ALIVE and alive_neighbors < 2 : 
                return DEAD
            elif self.actual_status == ALIVE and alive_neighbors > 3 : 
                return DEAD
            elif self.actual_status == ALIVE and (alive_neighbors == 2 or alive_neighbors == 3): 
                return ALIVE
            elif self.actual_status == DEAD and alive_neighbors == 3 : 
                return ALIVE
            else : 
                return DEAD