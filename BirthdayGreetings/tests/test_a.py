from datetime import datetime
from typing import Iterator

from BirthdayGreetings.Person import Person

def test_1():    
    people = [Person("Matt", "Damon", "1970/10/08" ), 
     Person("Anne", "Hathaway", "1982/11/12"),
     Person("Tom", "Holland", "1996/06/01")]
    assert ([Person("Anne", "Hathaway", "1982/11/12")] == __get_birthdays(people, "11/12"))

def test_2():
    people = [Person("Cillian", "Murphy", "1976/05/25" ), 
     Person("Emily", "Blunt", "1983/02/23"),
     Person("Robert", "Downey", "1965/04/04")]
    assert ([Person("Cillian", "Murphy", "1976/05/25" )] == __get_birthdays(people, "05/25"))

def test_3():
    people = [Person("John-David", "Washington", "1984/07/28" ), 
     Person("Robert", "Pattinson", "1986/05/13"),
     Person("Elizabeth", "Debicki", "1990/08/24")]
    assert ([] == __get_birthdays(people, "08/25"))

def test_4():
    people = [Person("Fionn", "Whitehead", "1997/07/18" ), 
     Person("Tom", "Glynn-Carney", "1995/02/07"),
     Person("Jack", "Lowden", "1990/06/02")]
    assert ([] == __get_birthdays(people, "08/18"))

def test_5():
    people = [Person("Demi", "Moore", "1962/11/11"), 
     Person("Tom", "Glynn-Carney", "1995/02/07"),
     Person("Leonardo", "DiCaprio", "1974/11/11")]
    assert ([Person("Demi", "Moore", "1962/11/11"),Person("Leonardo", "DiCaprio", "1974/11/11")] == __get_birthdays(people, "11/11"))


def __get_birthdays(people : Iterator[Person], date_to_celebrate_str:str) -> list[tuple[str,str,str]]: 
    date_to_celebrate = datetime.strptime(date_to_celebrate_str, '%m/%d').date()
    birthday_humans = []
    for human in people :
        birthday_date = datetime.strptime(human.birthday, '%Y/%m/%d').date()
        if date_to_celebrate.day == birthday_date.day and date_to_celebrate.month == birthday_date.month : 
            birthday_humans.append(human)
    return birthday_humans
