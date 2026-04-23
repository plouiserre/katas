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
    if interests == 0 :
        montly_payments = round(capital / (years*12) ,2) 
        return montly_payments
    else : 
        interests_by_months = interests/100/12
        total_months = years *12
        montly_payments_no_round = (capital * interests_by_months) /(1-(1+interests_by_months)**-total_months)
        montly_payments = round(montly_payments_no_round, 2)
        return montly_payments