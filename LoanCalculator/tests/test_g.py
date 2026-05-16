from LoanCalculator.taeg import Taeg

def test_1():
    capital = 100000
    montly_paiment = 933.63
    years = 10
    cost_guarantee = 41.67
    application_fee = 800
    assert(3.35 == calculate_taeg(capital, years, montly_paiment, cost_guarantee, application_fee))

def test_2():
    capital = 300000
    montly_paiment = 1566.99
    years = 25
    cost_guarantee = 100
    application_fee = 3600
    assert(4.57 == calculate_taeg(capital, years, montly_paiment, cost_guarantee, application_fee))

def calculate_taeg(capital, years, monthly_paiment, cost_guarantee, application_fee):
    taeg = Taeg(years, application_fee, monthly_paiment, cost_guarantee, capital)
    return taeg.calculate()