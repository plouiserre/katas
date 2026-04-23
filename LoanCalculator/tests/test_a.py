from LoanCalculator.credit import Credit

def test_calculate_montly_payment_for_200000_euros_25_year_credit_with_no_interest() : 
    sum_total = 200000
    years = 25
    assert(get_monthly_payment(sum_total, years, 0)==666.67)

def test_calculate_montly_payment_for_300000_euros_20_year_credit_with_no_interest(): 
    sum_total = 300000
    years = 20
    assert(get_monthly_payment(sum_total, years, 0)==1250)

def test_calculate_montly_payment_for_100000_euros_10_year_credit_with_2_point_3_percent_interest():
    sum_total = 100000
    years = 10
    interests = 2.3
    assert(get_monthly_payment(sum_total, years, interests) == 933.63)

def test_calculate_montly_payment_for_300000_euros_25_year_credit_with_3_point_9_percent_interest():
    sum_total = 300000
    years = 25
    interests = 3.9
    assert(get_monthly_payment(sum_total, years, interests) == 1566.99)

def get_monthly_payment(capital, years, interests):
    credit = Credit(capital, years, interests)
    return credit.calculate_montly_payment()

def test_calculate_capital_remaining_after_first_month_with_100000_euros_10_years_with_2_point_3_percent_interest():
    assert(calculate_capital_remaining(100000, 10, 2.3) == 99258.04)    

def test_calculate_capital_remaining_after_first_month_with_300000_euros_25_years_with_3_point_9_percent_interest():
    assert(calculate_capital_remaining(300000, 25, 3.9) == 299408.01)

def calculate_capital_remaining(capital, years, rate_interest):
    credit = Credit(capital, years, rate_interest)
    return credit.calculate_capital_remaining()