from LoanCalculator.credit import Credit

class Capital_Month : 
    def __init__(self, month_number, monthly_payment, interest, capital_repaid, capital_remaining):
        self.month_number = month_number
        self.monthly_payment = monthly_payment
        self.interest = interest
        self.capital_repaid = capital_repaid
        self.capital_remaining = capital_remaining

    def __eq__(self, other):
        return self.month_number == other.month_number and self.monthly_payment == other.monthly_payment and self.interest == other.interest and self.capital_repaid == other.capital_repaid and self.capital_remaining == other.capital_remaining

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

def test_calculate_paument_instalments_second_months_100000_euros_10_years_2_points_3(): 
    month_number = 1
    capital_month = Capital_Month(month_number, 933.63, 190.24,743.39,98514.65)
    capitals_month_calculated = calculate_capital_month(100000, 10,2.3)
    assert(capitals_month_calculated[month_number]== capital_month)

def test_calculate_paument_instalments_second_months_300000_euros_25_years_3_points_9(): 
    month_number = 2
    capital_month = Capital_Month(month_number, 1566.99, 971.15,595.84,298218.26)
    capitals_month_calculated = calculate_capital_month(300000, 25,3.9)
    assert(capitals_month_calculated[month_number]== capital_month)

def calculate_capital_month(capital, years, rate_interest):
    capitals_month = []
    credit = Credit(capital, years, rate_interest)
    total_months = years *12  
    i = 0
    monthly_payment = credit.calculate_montly_payment()
    while(i < total_months):
        interests = round(capital * (rate_interest /100/12),2)
        capital_repaid = round(monthly_payment - interests,2)
        capital_remaining = round(capital - capital_repaid,2)
        capital = capital_remaining
        capital_month = Capital_Month(i, monthly_payment, interests, capital_repaid, capital_remaining )
        capitals_month.append(capital_month)
        i += 1
    return capitals_month