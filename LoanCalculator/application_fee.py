class Application_Fee : 
    def __init__(self, capital, percentage):
        self.capital = capital
        self.percentage = percentage 
        self.cost = 0

    def calculate_costs(self): 
        self.cost = self.capital * self.percentage / 100
        return self.cost