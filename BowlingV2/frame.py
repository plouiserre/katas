class Frame : 
    def __init__(self, position, shots):
        self.position = position 
        self.shots = shots

    def __eq__(self, other):
        return self.shots[0] == other.shots[0] and self.shots[1] == other.shots[1] and self.position == other.position