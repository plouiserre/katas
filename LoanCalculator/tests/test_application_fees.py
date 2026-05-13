from LoanCalculator.application_fee import Application_Fee

def test_calculate_application_fee_300000_capital_and_0_point_9_percentage_af():
    capital = 300000
    application_fees_percentage = 0.9
    assert(2700 == calculate_cost_application_fees(application_fees_percentage, capital))

def test_calculate_application_fee_100000_capital_and_1_point_5_percentage_af():
    capital = 100000
    application_fees_percentage = 1.5
    assert(1500 == calculate_cost_application_fees(application_fees_percentage, capital))

def calculate_cost_application_fees(percentage, capital) : 
    application_fee = Application_Fee(capital, percentage)
    return application_fee.calculate_costs()