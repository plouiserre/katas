DEAD = 0
ALIVE = 1

class Cell : 
    def __init__(self, status, alive_neighbourgs):
        self.status = status 
        self.alive_neighbourgs = alive_neighbourgs

    def evolve(self): 
        if self.status == ALIVE : 
            if self.alive_neighbourgs < 2 or self.alive_neighbourgs > 3 :
                self.status = DEAD
            else : 
                self.status = ALIVE
        else : 
            if self.alive_neighbourgs == 3 :
                self.status = ALIVE 
            else : 
                self.status = DEAD