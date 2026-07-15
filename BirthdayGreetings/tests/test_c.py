from datetime import datetime

def test_1():
    date_to_evaluate = "2026/07/15"
    assert(False == date_is_in_a_leap_year(date_to_evaluate))

def test_2():
    date_to_evaluate = "2028/07/15"
    assert(True == date_is_in_a_leap_year(date_to_evaluate))

def test_3():
    date_to_evaluate = "1900/07/15"
    assert(False == date_is_in_a_leap_year(date_to_evaluate))

def test_4():
    date_to_evaluate = "2000/07/15"
    assert(True == date_is_in_a_leap_year(date_to_evaluate))

def date_is_in_a_leap_year(date_to_evaluate_str):
    date_to_evaluate = datetime.strptime(date_to_evaluate_str, '%Y/%m/%d').date()
    year = date_to_evaluate.year
    if year % 4 == 0 and year % 100 != 0 : 
        return True
    elif year %4 == 0 and year % 100 == 0 and year % 400 == 0 : 
        return True
    else :
        return False