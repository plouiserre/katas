from LoanCalculator.interest_this_month import InterestThisMonth

def test_calculate_interest_by_month_with_2_3_rate_interest(): 
    capital_remain = 9860
    rate_interest = 2.3   
    assert(18.90 == calculate_interest_by_month(capital_remain, rate_interest))

def calculate_interest_by_month(capital_remain, rate_interest) : 
    interest_this_month = InterestThisMonth(capital_remain, rate_interest)
    value_interest = interest_this_month.calculate() 
    return value_interest