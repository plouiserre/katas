from LoanCalculator.capital_month import Capital_Month

class Credit : 
    def __init__(self, capital, years, rate_interest, rate_guarantee, application_fees_percentage):
        self.capital = capital
        self.years = years 
        self.rate_interest = rate_interest
        self.rate_guarantee = rate_guarantee
        self.application_fees_percentage = application_fees_percentage
        
    def calculate_loan_repayment(self):
        capitals_month = []
        total_months = self.years *12  
        i = 0
        last_capital_remaining = self.capital
        while(i < total_months):
            capital_month = Capital_Month(i, self.years, self.capital, last_capital_remaining, self.rate_interest, self.rate_guarantee, self.application_fees_percentage)
            capital_month.build_capital_month()
            capitals_month.append(capital_month)
            last_capital_remaining = capital_month.capital_remaining
            i += 1
        return capitals_month