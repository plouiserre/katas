def test_1(): 
    montly_payment = MontlyPaiement(10, 100000, 0)
    value = montly_payment.calculate_value_montly_paiement()
    assert(833.33 == value)

def test_2(): 
    montly_payment = MontlyPaiement(25, 300000, 0)
    value = montly_payment.calculate_value_montly_paiement()
    assert(1000 == value)

def test_3(): 
    montly_paiement = MontlyPaiement(10, 100000, 2.3)
    value = montly_paiement.calculate_value_montly_paiement()
    assert(933.63 == value)

def test_4(): 
    montly_payment = MontlyPaiement(25, 300000, 3.9)
    value = montly_payment.calculate_value_montly_paiement()
    assert(1566.99 == value)

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