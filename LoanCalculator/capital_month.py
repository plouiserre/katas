class Capital_Month : 
    def __init__(self, month_number, monthly_payment, interest, capital_repaid, capital_remaining, guarantee):
        self.month_number = month_number
        self.monthly_payment = monthly_payment
        self.interest = interest
        self.capital_repaid = capital_repaid
        self.capital_remaining = capital_remaining
        self.guarantee = guarantee

    def __eq__(self, other):
        return self.month_number == other.month_number and self.monthly_payment == other.monthly_payment and self.interest == other.interest and self.capital_repaid == other.capital_repaid and self.capital_remaining == other.capital_remaining and self.guarantee == other.guarantee
