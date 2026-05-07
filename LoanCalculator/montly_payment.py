class MontlyPaiement : 
    def __init__(self, year, capital_total, rate_interest):
        self.years = year
        self.capital_total = capital_total
        self.value = 0
        self.rate_interest = rate_interest

    def calculate_value_montly_paiement(self): 
        montly_payments = 0
        if self.rate_interest == 0 :
            montly_payments =  round(self.capital_total / (self.years * 12), 2)
        else : 
            interests_by_months = self.rate_interest/100/12
            total_months = self.years *12
            montly_payments_no_round = (self.capital_total * interests_by_months) /(1-(1+interests_by_months)**-total_months)
            montly_payments = round(montly_payments_no_round, 2)
        return montly_payments