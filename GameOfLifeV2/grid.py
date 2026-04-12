DEAD = 0
ALIVE = 1

class Grid : 
    def get_status_cell_next_round(self, actual_status, alive_neighbourgs): 
        if actual_status == ALIVE and alive_neighbourgs < 2 : 
            return DEAD
        elif actual_status == ALIVE and alive_neighbourgs > 3 : 
            return DEAD
        elif actual_status == ALIVE and (alive_neighbourgs == 2 or alive_neighbourgs == 3): 
            return ALIVE
        elif actual_status == DEAD and alive_neighbourgs == 3 : 
            return ALIVE
        else : 
            return DEAD