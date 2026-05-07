class InterestPaid(): 
    def __init__(self, capital, rate_interest):
        self.capital = capital 
        self.rate_interest = rate_interest

    def calculate(self): 
        return round(self.capital * self.rate_interest, 2)