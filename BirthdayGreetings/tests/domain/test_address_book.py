from BirthdayGreetings.domain.AddressBook import AddressBook
from BirthdayGreetings.domain.Contact import Contact
from BirthdayGreetings.domain.ContactManager import ContactManager
from BirthdayGreetings.domain.DateOfTheDay import DateOfTheDay
from BirthdayGreetings.tests.fake.contact_manager_fake import ContactManagerFake

def test_search_contact_with_11_12_birthday_and_return_anne_hathaway():  
    address_book = __init_address_book([Contact("Matt", "Damon", "1970/10/08" ), 
     Contact("Anne", "Hathaway", "1982/11/12"),
     Contact("Tom", "Holland", "1996/06/01")], "2026/11/12")
    birthdays_persons = __get_birthdays_persons(address_book)
    __compare_birthdays_persons_with_expected_contacts ([Contact("Anne", "Hathaway", "1982/11/12")], birthdays_persons)

def test_search_contact_with_05_25_birthday_and_return_cillian_murphy():
    address_book = __init_address_book([Contact("Cillian", "Murphy", "1976/05/25" ), 
     Contact("Emily", "Blunt", "1983/02/23"),
     Contact("Robert", "Downey", "1965/04/04")], "2026/05/25")
    birthdays_persons = __get_birthdays_persons(address_book)
    __compare_birthdays_persons_with_expected_contacts ([Contact("Cillian", "Murphy", "1976/05/25")], birthdays_persons)

def test_search_contact_with_good_month_and_bad_day_birthday_and_return_no_one():
    address_book = __init_address_book([Contact("John-David", "Washington", "1984/07/28" ), 
     Contact("Robert", "Pattinson", "1986/05/13"),
     Contact("Elizabeth", "Debicki", "1990/08/24")], "2026/08/25")
    birthdays_persons = __get_birthdays_persons(address_book)
    __compare_birthdays_persons_with_expected_contacts ([], birthdays_persons)

def test_search_contact_with_bad_month_and_good_day_birthday_and_return_no_one():
    address_book = __init_address_book([Contact("Fionn", "Whitehead", "1997/07/18" ), 
     Contact("Tom", "Glynn-Carney", "1995/02/07"),
     Contact("Jack", "Lowden", "1990/06/02")], "2026/08/18")
    birthdays_persons = __get_birthdays_persons(address_book)
    __compare_birthdays_persons_with_expected_contacts ([], birthdays_persons)

def test_search_contact_with_11_11_birthday_and_return_demi_moore_and_leonardo_dicaprio():
    address_book = __init_address_book([Contact("Demi", "Moore", "1962/11/11"), 
     Contact("Tom", "Glynn-Carney", "1995/02/07"),
     Contact("Leonardo", "DiCaprio", "1974/11/11")], "1974/11/11")
    birthdays_persons = __get_birthdays_persons(address_book)
    __compare_birthdays_persons_with_expected_contacts ([Contact("Demi", "Moore", "1962/11/11"),Contact("Leonardo", "DiCaprio", "1974/11/11")], birthdays_persons)
    
def test_search_contact_with_29_02_birthday_in_a_leap_year_the_28_02():
    address_book = __init_address_book([Contact("Clark", "Kent", "1988/09/30"), 
     Contact("Diana", "Prince", "1992/02/29"),
     Contact("Bruce", "Wayne", "1989/03/28")], "2028/02/28")
    birthdays_persons = __get_birthdays_persons(address_book)
    __compare_birthdays_persons_with_expected_contacts ([], birthdays_persons)

def test_search_contact_with_29_02_birthday_in_a_leap_year_the_29_02():
    address_book = __init_address_book([Contact("Clark", "Kent", "1988/09/30"), 
     Contact("Diana", "Prince", "1992/02/29"),
     Contact("Bruce", "Wayne", "1989/03/28")], "2028/02/29")
    birthdays_persons = __get_birthdays_persons(address_book)
    __compare_birthdays_persons_with_expected_contacts ([Contact("Diana", "Prince", "1992/02/29")], birthdays_persons)

def test_search_contact_with_29_02_birthday_in_normal_year_the_28_02():
    address_book = __init_address_book([Contact("Clark", "Kent", "1988/09/30"), 
     Contact("Diana", "Prince", "1992/02/29"),
     Contact("Bruce", "Wayne", "1989/03/28")], "2026/02/28")
    birthdays_persons = __get_birthdays_persons(address_book)
    __compare_birthdays_persons_with_expected_contacts ([Contact("Diana", "Prince", "1992/02/29")], birthdays_persons)

def __init_address_book(contacts_save_in_address_books, date_to_celebrate_str) -> AddressBook: 
    contact_manager = ContactManagerFake(contacts_save_in_address_books)
    date_of_the_year = DateOfTheDay(date_to_celebrate_str)
    address_book = AddressBook(contact_manager, date_of_the_year)
    return address_book

def __get_birthdays_persons(address_book : AddressBook) -> list[Contact]: 
    return address_book.search_birthday_persons_in_this_date()

def __compare_birthdays_persons_with_expected_contacts(expected_contacts, birthdays_persons) : 
    assert(expected_contacts, birthdays_persons)
