def test_1(): 
    capital = 100000
    interest_by_month = 2.3/100/12
    assert(191.67 == calculate_interest_to_paid(capital, interest_by_month))

def test_2(): 
    capital = 300000
    interest_by_month = 3.9/100/12
    assert(975 == calculate_interest_to_paid(capital, interest_by_month))

def calculate_interest_to_paid(capital, interest_by_month): 
    return round(capital * interest_by_month, 2)