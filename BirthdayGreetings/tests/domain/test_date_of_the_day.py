from BirthdayGreetings.domain.DateOfTheDay import DateOfTheDay

def test_evaluate_2026_is_not_a_leap_year_because_it_is_not_divisible_by_4():
    date_to_evaluate = "2026/07/15"
    assert(False == date_is_in_a_leap_year(date_to_evaluate))

def test_evaluate_2028_is_a_leap_year_because_it_is_divisible_by_4():
    date_to_evaluate = "2028/07/15"
    assert(True == date_is_in_a_leap_year(date_to_evaluate))

def test_evaluate_1900_is_not_a_leap_year_because_it_is_divisible_by_4_and_divisible_by_100():
    date_to_evaluate = "1900/07/15"
    assert(False == date_is_in_a_leap_year(date_to_evaluate))

def test_evaluate_2000_is_a_leap_year_because_it_is_divisible_by_4_and_divisible_by_100_and_by_400():
    date_to_evaluate = "2000/07/15"
    assert(True == date_is_in_a_leap_year(date_to_evaluate))

def date_is_in_a_leap_year(date_to_evaluate_str):
    date_of_the_day = DateOfTheDay(date_to_evaluate_str)
    return date_of_the_day.is_date_belongs_to_a_leap_of_year()