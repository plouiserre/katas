from LoanCalculator.capital_remaining import CapitalRemaining
from LoanCalculator.capital_repaid import Capital_Repaid
from LoanCalculator.cost_guarantee import CostGuarantee
from LoanCalculator.interest_this_month import InterestThisMonth
from LoanCalculator.montly_payment import MontlyPaiement

class Capital_Month : 
    def __init__(self, month_number, year, capital_total, last_capital_remaining, rate_interest, rate_guarantee): 
        self.month_number = month_number
        self.year = year
        self.capital_total = capital_total
        self.last_capital_remaining = last_capital_remaining
        self.rate_interest = rate_interest        
        self.rate_guarantee = rate_guarantee
        self.interests = 0
        self.monthly_payment = 0
        self.capital_repaid = 0
        self.capital_remaining = 0
        self.guarantee_cost = 0

    def build_capital_month(self): 
        self.__get_interest_by_month()
        self.__get_monthly_payment()
        self.__get_capital_repaid()
        self.__get_capital_remaining()
        self.__get_cost_guarantee()

    def __get_interest_by_month(self):
        interest_this_month = InterestThisMonth(self.last_capital_remaining, self.rate_interest)
        self.interests = interest_this_month.calculate()

    def __get_monthly_payment(self):
        monthly_paiement_calculator = MontlyPaiement(self.year, self.capital_total, self.rate_interest)
        self.monthly_payment = monthly_paiement_calculator.calculate_value_montly_paiement()

    def __get_capital_repaid(self):
        capital_repaid_calculator = Capital_Repaid(self.monthly_payment, self.interests)
        self.capital_repaid = capital_repaid_calculator.calculate_amount()

    def __get_capital_remaining(self): 
        capital_remaining_calculator = CapitalRemaining(self.last_capital_remaining, self.capital_repaid)
        self.capital_remaining = capital_remaining_calculator.calculate()

    def __get_cost_guarantee(self):
        cost_guarantee = CostGuarantee(self.capital_total, self.rate_guarantee)
        self.guarantee_cost = cost_guarantee.calculate()
        
    def __eq__(self, other):
        return self.month_number == other.month_number and self.monthly_payment == other.monthly_payment and self.interests == other.interests and self.capital_repaid == other.capital_repaid and self.capital_remaining == other.capital_remaining and self.guarantee_cost == other.guarantee_cost
