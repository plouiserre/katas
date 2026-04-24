from LoanCalculator.capital_month import Capital_Month
from LoanCalculator.credit import Credit

def test_calculate_payment_instalments_second_months_100000_euros_10_years_2_points_3_point_6_guarante(): 
    month_number = 1
    rate_guarantee = 0.5
    capital_month = Capital_Month(month_number, 933.63, 190.24,743.39,98514.65, 41.67)
    capitals_month_calculated = calculate_capital_month(100000, 10,2.3, rate_guarantee)
    assert(capitals_month_calculated[month_number]== capital_month)

def test_calculate_payment_instalments_second_months_300000_euros_25_years_3_points_9_point_4_guarante(): 
    month_number = 2
    rate_guarantee = 0.4
    capital_month = Capital_Month(month_number, 1566.99, 971.15,595.84,298218.26, 100)
    capitals_month_calculated = calculate_capital_month(300000, 25,3.9, rate_guarantee)
    assert(capitals_month_calculated[month_number]== capital_month)

def calculate_capital_month(capital, years, rate_interest, rate_guarantee):
    credit = Credit(capital, years, rate_interest, rate_guarantee)
    capitals_month = credit.calculate_loan_repayment()
    return capitals_month