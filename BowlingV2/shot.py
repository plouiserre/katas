class Shot: 
    def __init__(self, points, number):
        self.points = points
        self.number = number

    def __eq__(self, other):
        return self.points == other.points and self.number == other.number