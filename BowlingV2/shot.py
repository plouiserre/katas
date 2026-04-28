class Shot: 
    def __init__(self, point, number):
        self.point = point
        self.number = number

    def __eq__(self, other):
        return self.point == other.point and self.number == other.number