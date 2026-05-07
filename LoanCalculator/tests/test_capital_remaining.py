from LoanCalculator.capital_remaining import CapitalRemaining

def test_calculate_capital_remaining_with_100000_capital_and_988_point_65_capital_repaid():
    capital = 100000 
    capital_repaid = 988.65
    capital_remaining_expected = 99011.35
    assert(capital_remaining_expected == calculate_capital_remaining(capital, capital_repaid))

def calculate_capital_remaining(capital, capital_repaid):
    capital_remaining = CapitalRemaining(capital, capital_repaid)
    return capital_remaining.calculate()