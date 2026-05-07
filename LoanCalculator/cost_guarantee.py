class CostGuarantee : 
    def __init__(self, capital, rate_guarantee):
        self.capital = capital
        self.rate_guarantee = rate_guarantee

    def calculate(self):
        return round(self.capital * self.rate_guarantee/100/12, 2)