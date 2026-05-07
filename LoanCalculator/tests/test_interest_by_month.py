from LoanCalculator.interest_by_month import InterestByMonth

def test_calculate_interest_by_month_with_2_3_rate_interest(): 
    rate_interest = 2.3
    interest_each_month = InterestByMonth(rate_interest)
    value_interest = interest_each_month.calculate()
    assert(2.3/100/12 == value_interest)