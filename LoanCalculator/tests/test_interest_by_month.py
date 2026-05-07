from LoanCalculator.interest_by_month import InterestByMonth

def test_calculate_interest_by_month_with_2_3_rate_interest(): 
    rate_interest = 2.3   
    assert(2.3/100/12 == calculate_interest_by_month(rate_interest))

def calculate_interest_by_month(rate_interest) : 
    interest_each_month = InterestByMonth(rate_interest)
    value_interest = interest_each_month.calculate() 
    return value_interest