def test_1() : 
    sum_total = 200000
    years = 25
    assert(get_monthly_payment(sum_total, years)==666.67)

def test_2(): 
    sum_total = 300000
    years = 20
    assert(get_monthly_payment(sum_total, years)==1250)

def get_monthly_payment(sum_total, years):
    montly_payments = round(sum_total / (years*12) ,2) 
    return montly_payments