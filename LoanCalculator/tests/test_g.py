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

def calculate_taeg(capital, years, montly_paiment, cost_guarantee, application_fee):
    r_max = 0.0001
    number_months = years *12
    application_fee_by_months = application_fee / number_months
    montly_paiment_all_included = montly_paiment + cost_guarantee + application_fee_by_months
    r = 0
    while (r <= 0 ) :
        r = __calcute_r(capital, montly_paiment_all_included, r_max, number_months)
        if r <= 0 :
            r_max = round(r_max + 0.0001, 4)
    r_min = round(r_max - 0.0001, 4)    
    r_min_r = __calcute_r(capital, montly_paiment_all_included, r_min, number_months)
    r_max_r = __calcute_r(capital, montly_paiment_all_included, r_max, number_months)
    TAEG =  round((r_min + (r_max - r_min) * r_min_r / (r_min_r - r_max_r)) *12*100, 2)
    return TAEG


def __calcute_r(capital, monthly_paiement, r_candidate, number_months):
    return capital - monthly_paiement * (1 - (1+r_candidate)**-number_months)/r_candidate