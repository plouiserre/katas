from typing import Iterator

from BirthdayGreetings.AddressBook import AddressBook
from BirthdayGreetings.Contact import Contact

def test_search_contact_with_11_12_birthday_and_return_anne_hathaway():    
    people = [Contact("Matt", "Damon", "1970/10/08" ), 
     Contact("Anne", "Hathaway", "1982/11/12"),
     Contact("Tom", "Holland", "1996/06/01")]
    assert ([Contact("Anne", "Hathaway", "1982/11/12")] == __get_birthdays(people, "11/12"))

def test_search_contact_with_05_25_birthday_and_return_cillian_murphy():
    people = [Contact("Cillian", "Murphy", "1976/05/25" ), 
     Contact("Emily", "Blunt", "1983/02/23"),
     Contact("Robert", "Downey", "1965/04/04")]
    assert ([Contact("Cillian", "Murphy", "1976/05/25" )] == __get_birthdays(people, "05/25"))

def test_search_contact_with_good_month_and_bad_day_birthday_and_return_no_one():
    people = [Contact("John-David", "Washington", "1984/07/28" ), 
     Contact("Robert", "Pattinson", "1986/05/13"),
     Contact("Elizabeth", "Debicki", "1990/08/24")]
    assert ([] == __get_birthdays(people, "08/25"))

def test_search_contact_with_bad_month_and_good_day_birthday_and_return_no_one():
    people = [Contact("Fionn", "Whitehead", "1997/07/18" ), 
     Contact("Tom", "Glynn-Carney", "1995/02/07"),
     Contact("Jack", "Lowden", "1990/06/02")]
    assert ([] == __get_birthdays(people, "08/18"))

def test_search_contact_with_11_11_birthday_and_return_demi_moore_and_leonardo_dicaprio():
    people = [Contact("Demi", "Moore", "1962/11/11"), 
     Contact("Tom", "Glynn-Carney", "1995/02/07"),
     Contact("Leonardo", "DiCaprio", "1974/11/11")]
    assert ([Contact("Demi", "Moore", "1962/11/11"),Contact("Leonardo", "DiCaprio", "1974/11/11")] == __get_birthdays(people, "11/11"))


def __get_birthdays(people : Iterator[Contact], date_to_celebrate_str:str) -> list[Contact]: 
    address_book = AddressBook(people)
    return address_book.search_birthday_persons_in_this_date(date_to_celebrate_str)
