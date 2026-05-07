from LoanCalculator.interest_paid import InterestPaid
def test_calculate_interest_to_paid_with_1000000_capital_and_two_point_three_rate(): 
    capital = 100000
    interest_by_month = 2.3/100/12
    assert(191.67 == calculate_interest_to_paid(capital, interest_by_month))

def test_calculate_interest_to_paid_with_3000000_capital_and_three_point_nine_rate(): 
    capital = 300000
    interest_by_month = 3.9/100/12
    assert(975 == calculate_interest_to_paid(capital, interest_by_month))

def calculate_interest_to_paid(capital, interest_by_month): 
    interest_paid = InterestPaid(capital, interest_by_month)
    return interest_paid.calculate()