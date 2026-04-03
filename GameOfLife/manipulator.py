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
    
    def locate_neighbourgs(self, cell_position) : 
        coordonnates = self.locate_cell(cell_position)
        neighbourgs_coordonnates = self.__get_all_neighbourgs_coordonnates(coordonnates)
        return neighbourgs_coordonnates
    
    def __get_all_neighbourgs_coordonnates(self, coordonnates) : 
        neighbourgs_coordonnates = []
        left_neighbourg = self.__find_left_neighbourg(coordonnates)
        right_neighbourg = self.__find_right_neighbourg(coordonnates)
        top_neighbourg = self.__find_top_neighbourg(coordonnates)
        bottom_neighbourg = self.__find_bottom_neighbourg(coordonnates)
        top_left_neighbourg = self.__find_top_left_neighbourg(coordonnates)
        top_right_neighbourg = self.__find_top_right_neighbourg(coordonnates)
        bottom_left_neighbourg = self.__find_bottom_left_neighbourg(coordonnates)
        bottom_right_neighbourg = self.__find_bottom_right_neighbourg(coordonnates)
        all_coordonnates = [left_neighbourg, right_neighbourg, top_neighbourg, bottom_neighbourg, top_left_neighbourg, 
                            top_right_neighbourg, bottom_left_neighbourg, bottom_right_neighbourg]
        for coordonnates in all_coordonnates : 
            if coordonnates != None : 
                neighbourgs_coordonnates.append(coordonnates)
        return neighbourgs_coordonnates
    
    def __find_left_neighbourg(self, coordonnates) : 
        y = coordonnates[0]
        x = coordonnates[1]
        new_x = x - 1
        if new_x >= 0 :
            return [y, new_x]
        else : 
            return None
        
    def __find_right_neighbourg(self, coordonnates) : 
        y = coordonnates[0]
        x = coordonnates[1]
        new_x = x + 1
        if new_x < len(self.grid[0]) : 
            return [y, new_x]
        else : 
            return None

    def __find_top_neighbourg(self, coordonnates): 
        y = coordonnates[0]
        x = coordonnates[1]
        new_y = y - 1 
        if new_y >= 0 : 
            return [new_y, x]
        else : 
            return None
        
    def __find_bottom_neighbourg(self, coordonnates): 
        y = coordonnates[0]
        x = coordonnates[1]
        new_y = y + 1
        if new_y < len(self.grid): 
            return [new_y, x]
        else : 
            return None
        
    def __find_top_left_neighbourg(self, coordonnates): 
        y = coordonnates[0]
        x = coordonnates[1]
        new_y = y - 1
        new_x = x - 1
        if new_y >= 0 and new_x >= 0:
            return [new_y, new_x]
        else : 
            return None
        
    def __find_top_right_neighbourg(self, coordonnates): 
        y = coordonnates[0]
        x = coordonnates[1]
        new_y = y - 1
        new_x = x + 1
        if new_y >= 0 and new_x < len(self.grid[0]):
            return [new_y, new_x]
        else : 
            return None
        
    def __find_bottom_left_neighbourg(self, coordonnates): 
        y = coordonnates[0]
        x = coordonnates[1]
        new_y = y + 1
        new_x = x - 1
        if new_y < len(self.grid) and new_x >= 0:
            return [new_y, new_x]
        else : 
            return None
        
    def __find_bottom_right_neighbourg(self, coordonnates): 
        y = coordonnates[0]
        x = coordonnates[1]
        new_y = y + 1
        new_x = x + 1
        if new_y < len(self.grid) and new_x < len(self.grid[0]):
            return [new_y, new_x]
        else : 
            return None