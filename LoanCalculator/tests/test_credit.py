from LoanCalculator.capital_month import Capital_Month
from LoanCalculator.credit import Credit

def test_calculate_payment_instalments_second_months_100000_euros_10_years_2_points_3_point_6_guarante(): 
    month_number = 1
    rate_guarantee = 0.5
    application_fees_percentage = 0.8
    capital_month = __build_capital_month(month_number, 10, 100000, 99258.04, 2.3, 190.24, 933.63, 41.67, 98514.65, rate_guarantee, 41.67, application_fees_percentage, 800)
    capital_month.build_capital_month()
    capitals_month_calculated = calculate_capital_month(100000, 10,2.3, rate_guarantee, application_fees_percentage)
    assert(capitals_month_calculated[month_number]== capital_month)

def test_calculate_payment_instalments_second_months_300000_euros_25_years_3_points_9_point_4_guarante(): 
    month_number = 2
    rate_guarantee = 0.4
    application_fees_percentage = 1.2
    capital_month = __build_capital_month(month_number, 25, 300000, 298814.1, 3.9, 971.15, 1566.99, 595.84, 298218.26, rate_guarantee, 100, application_fees_percentage, 3600)
    capitals_month_calculated = calculate_capital_month(300000, 25,3.9, rate_guarantee, application_fees_percentage)
    assert(capitals_month_calculated[month_number]== capital_month)

def calculate_capital_month(capital, years, rate_interest, rate_guarantee, application_fees_percentage):
    credit = Credit(capital, years, rate_interest, rate_guarantee, application_fees_percentage)
    capitals_month = credit.calculate_loan_repayment()
    return capitals_month

def __build_capital_month(month_number, years, capital, last_remaining_capital, rate_interest, interest_this_month, montly_payment, capital_repaid, capital_remaining, rate_guarantee, guarantee_cost, application_fee_percentage, application_fees_value) : 
    capital_month = Capital_Month(month_number, years, capital, last_remaining_capital, rate_interest, rate_guarantee, application_fee_percentage)
    capital_month.interests = interest_this_month
    capital_month.monthly_payment = montly_payment
    capital_month.capital_repaid = capital_repaid
    capital_month.capital_remaining = capital_remaining
    capital_month.guarantee_cost = guarantee_cost
    capital_month.application_fees_value = application_fees_value
    return capital_month