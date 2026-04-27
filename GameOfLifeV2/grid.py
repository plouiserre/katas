from GameOfLifeV2.status_cell import ALIVE, DEAD

class Grid : 
    def __init__(self, grid_data, status_cell):
        self.__grid_data = grid_data
        self.__alive_cells = []
        self.status_cell = status_cell

    def draw_next_generation(self) : 
        next_status = self.__generate_next_generation_grid()
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

    def __generate_next_generation_grid(self) : 
        self.__alive_cells = self.__determinate_alive_cells()
        all_status =[]
        for y, row in enumerate(self.__grid_data) : 
            status_row = []
            for x, column in enumerate(self.__grid_data[y]):
                status_next_generation = self.status_cell.evolve_next_generation(x, y, self.__alive_cells)
                status_row.append(status_next_generation)
            all_status.append(status_row)
        return all_status  
        
    def __determinate_alive_cells(self): 
        alive_cells = []
        for y, row in enumerate(self.__grid_data) : 
            if ("*" in row) == False:
                continue
            else : 
                for x, column in enumerate(row): 
                    if column == "*" : 
                        alive_cells.append([y, x])
        return alive_cells