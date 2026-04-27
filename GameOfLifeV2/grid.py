from GameOfLifeV2.cell_evolution import ALIVE, CellEvolution, DEAD

class Grid : 
    def __init__(self, grid_data):
        self.__grid_data = grid_data
        self.__alive_cells = []

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
                status_cell = self.__get_alive_cells(self.__alive_cells, [y, x])
                cell = CellEvolution(x, y, self.__alive_cells, status_cell)
                status_next_generation = cell.transform()
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