class Credit : 
    def __init__(self, capital, years, rate_interest):
        self.capital = capital
        self.years = years 
        self.rate_interest = rate_interest

    def calculate_montly_payment(self): 
        if self.rate_interest == 0 :
            montly_payments = round(self.capital / (self.years*12) ,2) 
            return montly_payments
        else : 
            interests_by_months = self.rate_interest/100/12
            total_months = self.years *12
            montly_payments_no_round = (self.capital * interests_by_months) /(1-(1+interests_by_months)**-total_months)
            montly_payments = round(montly_payments_no_round, 2)
        return montly_payments
    
    def calculate_capital_remaining(self):
        first_mensuality = self.calculate_montly_payment()
        interests = self.capital * (self.rate_interest /100/12) 
        capital_repaid = first_mensuality - interests
        capital_remaining = round(self.capital - capital_repaid,2)
        return capital_remaining