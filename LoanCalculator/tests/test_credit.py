from LoanCalculator.capital_month import Capital_Month
from LoanCalculator.credit import Credit

def test_calculate_payment_instalments_second_months_100000_euros_10_years_2_points_3_point_6_guarante(): 
    month_number = 1
    rate_guarantee = 0.5
    capital_month = __build_capital_month(month_number, 10, 100000, 99258.04, 2.3, 190.24, 933.63, 41.67, 98514.65, rate_guarantee, 41.67)
    capital_month.build_capital_month()
    capitals_month_calculated = calculate_capital_month(100000, 10,2.3, rate_guarantee)
    assert(capitals_month_calculated[month_number]== capital_month)

def test_calculate_payment_instalments_second_months_300000_euros_25_years_3_points_9_point_4_guarante(): 
    month_number = 2
    rate_guarantee = 0.4
    capital_month = __build_capital_month(month_number, 25, 300000, 298814.1, 3.9, 971.15, 1566.99, 595.84, 298218.26, rate_guarantee, 100)
    capitals_month_calculated = calculate_capital_month(300000, 25,3.9, rate_guarantee)
    assert(capitals_month_calculated[month_number]== capital_month)

def calculate_capital_month(capital, years, rate_interest, rate_guarantee):
    credit = Credit(capital, years, rate_interest, rate_guarantee)
    capitals_month = credit.calculate_loan_repayment()
    return capitals_month

def __build_capital_month(month_number, years, capital, last_remaining_capital, rate_interest, interest_this_month, montly_payment, capital_repaid, capital_remaining, rate_guarantee, guarantee_cost) : 
    capital_month = Capital_Month(month_number, years, capital, last_remaining_capital, rate_interest, rate_guarantee)
    capital_month.interests = interest_this_month
    capital_month.monthly_payment = montly_payment
    capital_month.capital_repaid = capital_repaid
    capital_month.capital_remaining = capital_remaining
    capital_month.guarantee_cost = guarantee_cost
    return capital_month