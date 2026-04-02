class Manipulator :
    def __init__(self, grid):
        self.grid = grid

    def locate_cell(self, cell_position): 
        coordonnates = []
        for i, line in enumerate(self.grid) :
            for j, column in enumerate(line) : 
                if cell_position == 0 : 
                    coordonnates.append(i)
                    coordonnates.append(j)
                    break
                else : 
                    cell_position =cell_position - 1
            if cell_position == 0 : 
                break         
        return coordonnates