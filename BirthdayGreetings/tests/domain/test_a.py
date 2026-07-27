from BirthdayGreetings.domain.Contact import Contact
from BirthdayGreetings.domain.DateOfTheDay import DateOfTheDay

def test_1(): 
    date_to_study = "2026/07/27"
    contact = Contact("John", "Doe", "1989/07/27")
    is_birthday = __it_is_birthday_contact(contact, date_to_study)
    assert(is_birthday == True)

def test_2(): 
    date_to_study = "2026/07/26"
    contact = Contact("John", "Doe", "1989/07/27")
    is_birthday = __it_is_birthday_contact(contact, date_to_study)
    assert(is_birthday == False)

def test_3():
    date_to_study = "2026/02/28"
    contact = Contact("John", "Doe", "1988/02/29")
    is_birthday = __it_is_birthday_contact(contact, date_to_study)
    assert(is_birthday == True)

def test_4():
    date_to_study = "2024/02/28"
    contact = Contact("John", "Doe", "1988/02/29")
    is_birthday = __it_is_birthday_contact(contact, date_to_study)
    assert(is_birthday == False)

def __it_is_birthday_contact(contact : Contact, date_to_study_str : str): 
    date_of_the_day = DateOfTheDay(date_to_study_str)
    is_leap_year = date_of_the_day.is_date_belongs_to_a_leap_of_year()
    return contact.is_birthday_today(date_to_study_str, is_leap_year)