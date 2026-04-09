from GameOfLife.cell import DEAD, ALIVE, Cell


class Grid : 
    def __init__(self, locator, grid):
        self.locator = locator
        self.grid = grid

    def evolve_grid_next_round(self):
        cell_number = 0
        news_state = []
        for idx_line, line in enumerate(self.grid) : 
            all_new_cells_line = []
            for idx_column, column in enumerate(line):
                alive_neighbourgs = self.count_alive_neighbourgs(cell_number)
                actual_state = ""
                if column == "." :
                    actual_state = DEAD
                else : 
                    actual_state = ALIVE
                cell = Cell(actual_state, alive_neighbourgs)
                cell.evolve()
                all_new_cells_line.append(cell.status)
                cell_number +=1
            news_state.append(all_new_cells_line)
        return news_state

    def count_alive_neighbourgs(self, cell_number): 
        cells_alive = 0
        neighbourgs = self.locator.locate_neighbourgs(cell_number)
        states = []
        for neighbourg in neighbourgs :
            content = self.__find_content_from_coordonnates(neighbourg[0], neighbourg[1])
            state_cell = self.__convert_content_to_state_cell(content)
            states.append(state_cell)
        for state in states : 
            if state == ALIVE : 
                cells_alive += 1
        return cells_alive

    def get_contents_cells(self,cells):
        states = []
        for cell in cells :
            cell_location = self.locator.locate_cell(cell)
            content = self.__find_content_from_coordonnates(cell_location[0], cell_location[1])
            state_cell = self.__convert_content_to_state_cell(content)
            states.append(state_cell)
        return states
    
    def __find_content_from_coordonnates(self, y, x): 
        content = ""
        for idx_g, cells in enumerate(self.grid) : 
            if y != idx_g : 
                continue
            else : 
                for idx_c, content_cell in enumerate(cells) : 
                    if x != idx_c : 
                        continue
                    else : 
                        content = content_cell
        return content

    def __convert_content_to_state_cell(self, content) : 
        if content == "." :
            return DEAD 
        else : 
            return ALIVE
