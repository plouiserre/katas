class CapitalRemaining : 
    def __init__(self, capital, capital_repaid):
        self.capital = capital
        self.capital_repaid = capital_repaid

    def calculate(self) : 
        return self.capital - self.capital_repaid