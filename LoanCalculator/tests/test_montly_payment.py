from LoanCalculator.montly_payment import MontlyPaiement

def test_calcul_paiement_mensuel_10_ans_capital_100000_sans_interet(): 
    montly_payment = MontlyPaiement(10, 100000, 0)
    value = montly_payment.calculate_value_montly_paiement()
    assert(833.33 == value)

def test_calcul_paiement_mensuel_25_ans_capital_300000_sans_interet(): 
    montly_payment = MontlyPaiement(25, 300000, 0)
    value = montly_payment.calculate_value_montly_paiement()
    assert(1000 == value)

def test_calcul_paiement_mensuel_10_ans_capital_100000_avec_2_virgule_3_interet(): 
    montly_paiement = MontlyPaiement(10, 100000, 2.3)
    value = montly_paiement.calculate_value_montly_paiement()
    assert(933.63 == value)

def test_calcul_paiement_mensuel_25_ans_capital_300000_avec_3_virgule_9_interet(): 
    montly_payment = MontlyPaiement(25, 300000, 3.9)
    value = montly_payment.calculate_value_montly_paiement()
    assert(1566.99 == value)