from unittest.mock import Mock

from BirthdayGreetings.domain.AddressBook import AddressBook
from BirthdayGreetings.domain.Contact import Contact
from BirthdayGreetings.domain.ContactManager import ContactManager
from BirthdayGreetings.domain.DateOfTheDay import DateOfTheDay

def test_search_contact_with_11_12_birthday_and_return_anne_hathaway():  
    contact_manager = Mock()
    contact_manager.get_all_contacts.return_value = [Contact("Matt", "Damon", "1970/10/08" ), 
     Contact("Anne", "Hathaway", "1982/11/12"),
     Contact("Tom", "Holland", "1996/06/01")]
    assert ([Contact("Anne", "Hathaway", "1982/11/12")] == __get_birthdays(contact_manager, "2026/11/12"))

def test_search_contact_with_05_25_birthday_and_return_cillian_murphy():
    contact_manager = Mock()
    contact_manager.get_all_contacts.return_value = [Contact("Cillian", "Murphy", "1976/05/25" ), 
     Contact("Emily", "Blunt", "1983/02/23"),
     Contact("Robert", "Downey", "1965/04/04")]
    assert ([Contact("Cillian", "Murphy", "1976/05/25" )] == __get_birthdays(contact_manager, "2026/05/25"))

def test_search_contact_with_good_month_and_bad_day_birthday_and_return_no_one():
    contact_manager = Mock()
    contact_manager.get_all_contacts.return_value = [Contact("John-David", "Washington", "1984/07/28" ), 
     Contact("Robert", "Pattinson", "1986/05/13"),
     Contact("Elizabeth", "Debicki", "1990/08/24")]
    assert ([] == __get_birthdays(contact_manager, "2026/08/25"))

def test_search_contact_with_bad_month_and_good_day_birthday_and_return_no_one():
    contact_manager = Mock()
    contact_manager.get_all_contacts.return_value = [Contact("Fionn", "Whitehead", "1997/07/18" ), 
     Contact("Tom", "Glynn-Carney", "1995/02/07"),
     Contact("Jack", "Lowden", "1990/06/02")]
    assert ([] == __get_birthdays(contact_manager, "2026/08/18"))

def test_search_contact_with_11_11_birthday_and_return_demi_moore_and_leonardo_dicaprio():
    contact_manager = Mock()
    contact_manager.get_all_contacts.return_value = [Contact("Demi", "Moore", "1962/11/11"), 
     Contact("Tom", "Glynn-Carney", "1995/02/07"),
     Contact("Leonardo", "DiCaprio", "1974/11/11")]
    assert ([Contact("Demi", "Moore", "1962/11/11"),Contact("Leonardo", "DiCaprio", "1974/11/11")] == __get_birthdays(contact_manager, "2026/11/11"))

def test_search_contact_with_29_02_birthday_in_a_leap_year_the_28_02():
    contact_manager = Mock()
    contact_manager.get_all_contacts.return_value = [Contact("Clark", "Kent", "1988/09/30"), 
     Contact("Diana", "Prince", "1992/02/29"),
     Contact("Bruce", "Wayne", "1989/03/28")]
    assert ([] == __get_birthdays(contact_manager, "2028/02/28"))

def test_search_contact_with_29_02_birthday_in_a_leap_year_the_29_02():
    contact_manager = Mock()
    contact_manager.get_all_contacts.return_value = [Contact("Clark", "Kent", "1988/09/30"), 
     Contact("Diana", "Prince", "1992/02/29"),
     Contact("Bruce", "Wayne", "1989/03/28")]
    assert ([Contact("Diana", "Prince", "1992/02/29")] == __get_birthdays(contact_manager, "2028/02/29"))

def test_search_contact_with_29_02_birthday_in_normal_year_the_28_02():
    contact_manager = Mock()
    contact_manager.get_all_contacts.return_value = [Contact("Clark", "Kent", "1988/09/30"), 
     Contact("Diana", "Prince", "1992/02/29"),
     Contact("Bruce", "Wayne", "1989/03/28")]
    assert ([Contact("Diana", "Prince", "1992/02/29")] == __get_birthdays(contact_manager, "2026/02/28"))


def __get_birthdays(contact_manager : ContactManager, date_to_celebrate_str:str) -> list[Contact]: 
    date_of_the_year = DateOfTheDay(date_to_celebrate_str)
    address_book = AddressBook(contact_manager, date_of_the_year)
    return address_book.search_birthday_persons_in_this_date(date_to_celebrate_str)
