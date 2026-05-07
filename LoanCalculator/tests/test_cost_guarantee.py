from LoanCalculator.cost_guarantee import CostGuarantee

def test_calculate_cost_guarantee_100000_capital_zero_point_five(): 
    capital = 100000
    rate_guarantee = 0.5
    cost_guarantee_expected = 41.67
    assert(cost_guarantee_expected == calculate_cost_guarantee_expected(capital, rate_guarantee))

def calculate_cost_guarantee_expected(capital, rate_guarantee):
    cost_guarantee = CostGuarantee(capital, rate_guarantee) 
    return cost_guarantee.calculate()