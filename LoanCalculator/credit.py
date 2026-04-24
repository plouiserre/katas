from LoanCalculator.capital_month import Capital_Month

class Credit : 
    def __init__(self, capital, years, rate_interest, rate_guarantee):
        self.capital = capital
        self.years = years 
        self.rate_interest = rate_interest
        self.rate_guarantee = rate_guarantee
        
    def calculate_loan_repayment(self):
        capitals_month = []
        total_months = self.years *12  
        i = 0
        monthly_payment = self.__calculate_montly_payment()
        cost_guarantee = self.__calculate_cost_guarantee()
        while(i < total_months):
            interests = round(self.capital * (self.rate_interest /100/12),2)
            capital_repaid = round(monthly_payment - interests,2)
            capital_remaining = round(self.capital - capital_repaid,2)
            self.capital = capital_remaining
            capital_month = Capital_Month(i, monthly_payment, interests, capital_repaid, capital_remaining, cost_guarantee)
            capitals_month.append(capital_month)
            i += 1
        return capitals_month

    def __calculate_montly_payment(self): 
        if self.rate_interest == 0 :
            montly_payments = round(self.capital / (self.years*12) ,2) 
            return montly_payments
        else : 
            interests_by_months = self.rate_interest/100/12
            total_months = self.years *12
            montly_payments_no_round = (self.capital * interests_by_months) /(1-(1+interests_by_months)**-total_months)
            montly_payments = round(montly_payments_no_round, 2)
        return montly_payments
    
    def __calculate_cost_guarantee(self):
        return round(self.capital*self.rate_guarantee/100/12, 2)