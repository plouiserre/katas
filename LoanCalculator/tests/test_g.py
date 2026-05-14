def test_1():
    montly_paiment = 933.63
    interest = 2.3
    assert(3.62 == calculate_taeg(montly_paiment, interest))

def test_2():
    montly_paiment = 1566.99
    interest = 3.9
    assert(4.84 == calculate_taeg(montly_paiment, interest))

def calculate_taeg(montly_paiment, interest):
    return 0