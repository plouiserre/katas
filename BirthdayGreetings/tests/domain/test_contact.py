from BirthdayGreetings.domain.Contact import Contact
from BirthdayGreetings.domain.DateOfTheDay import DateOfTheDay

def test_find_it_is_birthday_for_john_doe(): 
    date_to_study = "2026/07/27"
    contact = Contact("John", "Doe", "1989/07/27")
    is_birthday = __it_is_birthday_contact(contact, date_to_study)
    assert(is_birthday == True)

def test_find_it_is_not_birthday_for_john_doe(): 
    date_to_study = "2026/07/26"
    contact = Contact("John", "Doe", "1989/07/27")
    is_birthday = __it_is_birthday_contact(contact, date_to_study)
    assert(is_birthday == False)

def test_find_it_is_birthday_for_john_doe_because_it_is_leap_year():
    date_to_study = "2026/02/28"
    contact = Contact("John", "Doe", "1988/02/29")
    is_birthday = __it_is_birthday_contact(contact, date_to_study)
    assert(is_birthday == True)

def test_find_it_is_not_birthday_for_john_doe_because_it_is_not_leap_year():
    date_to_study = "2024/02/28"
    contact = Contact("John", "Doe", "1988/02/29")
    is_birthday = __it_is_birthday_contact(contact, date_to_study)
    assert(is_birthday == False)

def test_find_it_is_not_birthday_for_john_doe_during_a_leap_year():
    date_to_study = "2024/02/29"
    contact = Contact("John", "Doe", "1988/02/29")
    is_birthday = __it_is_birthday_contact(contact, date_to_study)
    assert(is_birthday == True)

def __it_is_birthday_contact(contact : Contact, date_to_study_str : str): 
    return contact.is_birthday_today(date_to_study_str)