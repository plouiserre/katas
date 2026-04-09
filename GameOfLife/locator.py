class Locator :
    def __init__(self, grid):
        self.grid = grid

    def locate_cell(self, cell_position): 
        coordonnates = []
        if cell_position > 0 :
            x_max = len(self.grid[0])
            y = int(cell_position / x_max)
            x = cell_position - y * x_max 
            coordonnates.append(y)
            coordonnates.append(x)
        else : 
            coordonnates.append(0)
            coordonnates.append(0)
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