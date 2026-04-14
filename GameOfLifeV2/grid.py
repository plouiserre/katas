DEAD = 0
ALIVE = 1

class Grid : 
    def __init__(self, grid_data):
        self.grid_data = grid_data

    def draw_next_generation(self) : 
        next_status = self.generate_next_generation_grid()
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

    def generate_next_generation_grid(self) : 
        alive_cells = self.determinate_alive_cells()
        all_status =[]
        for y, row in enumerate(self.grid_data) : 
            status_row = []
            for x, column in enumerate(self.grid_data[y]):
                number_neighbors = self.count_alive_neighbors([y, x])
                status_cell = self.__get_alive_cells(alive_cells, [y, x])
                status_next_generation = self.get_status_cell_next_round(status_cell, number_neighbors)
                status_row.append(status_next_generation)
            all_status.append(status_row)
        return all_status

    def __get_alive_cells(self, alive_cells, coordonnates) :
        is_alive = False
        for cell in alive_cells :
            if cell[0] == coordonnates[0] and cell[1] == coordonnates[1]:
                is_alive = True 
                break
        if is_alive :
            return ALIVE 
        else : 
            return  DEAD

    def count_alive_neighbors(self, coordonnates): 
        alive_neighbors = 0
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
                        alive_neighbors +=1  
        return alive_neighbors
        
    def get_status_cell_next_round(self, actual_status, alive_neighbors): 
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