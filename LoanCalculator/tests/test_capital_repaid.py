from LoanCalculator.capital_repaid import Capital_Repaid

def test_calculate_capital_remain(): 
    montly_payment = 988
    interests = 62.6
    capital_repaid_expected = 925.4
    assert(capital_repaid_expected == calculate_capital_repaid(montly_payment, interests))

def calculate_capital_repaid(montly_payment, interests):
    capital_repaid = Capital_Repaid(montly_payment, interests) 
    return capital_repaid.calculate_amount()