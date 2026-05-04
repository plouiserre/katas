class Participant : 
    def __init__(self,name, balance):
        self.name = name 
        self.balance = balance

    def __eq__(self, other):
        if other == None : 
            return False
        return self.name == other.name and self.balance == other.balance

