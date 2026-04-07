from GameOfLife.cell import DEAD, ALIVE


class Grid : 
    def __init__(self, locator, grid):
        self.locator = locator
        self.grid = grid

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
