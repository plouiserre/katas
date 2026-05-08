class InterestThisMonth  :
    def __init__(self, capital_remaining, rate_interest):
        self.capital_remaining = capital_remaining
        self.rate_interest = rate_interest

    def calculate(self):
        return round(self.capital_remaining * (self.rate_interest /100/12),2)