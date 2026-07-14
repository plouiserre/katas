from datetime import datetime

def test_1():    
    people = [("Matt", "Damon", "1970/10/08" ), 
     ("Anne", "Hathaway", "1982/11/12"),
     ("Tom", "Holland", "1996/06/01")]
    assert ([("Anne", "Hathaway", "1982/11/12")] == __get_birthdays(people, "11/12"))

def test_2():
    people = [("Cillian", "Murphy", "1976/05/25" ), 
     ("Emily", "Blunt", "1983/02/23"),
     ("Robert", "Downey", "1965/04/04")]
    assert ([("Cillian", "Murphy", "1976/05/25" )] == __get_birthdays(people, "05/25"))

def test_3():
    people = [("John-David", "Washington", "1984/07/28" ), 
     ("Robert", "Pattinson", "1986/05/13"),
     ("Elizabeth", "Debicki", "1990/08/24")]
    assert ([] == __get_birthdays(people, "08/25"))

def test_4():
    people = [("Fionn", "Whitehead", "1997/07/18" ), 
     ("Tom", "Glynn-Carney", "1995/02/07"),
     ("Jack", "Lowden", "1990/06/02")]
    assert ([] == __get_birthdays(people, "08/18"))

def test_5():
    people = [("Demi", "Moore", "1962/11/11"), 
     ("Tom", "Glynn-Carney", "1995/02/07"),
     ("Leonardo", "DiCaprio", "1974/11/11")]
    assert ([("Demi", "Moore", "1962/11/11"),("Leonardo", "DiCaprio", "1974/11/11")] == __get_birthdays(people, "11/11"))


def __get_birthdays(people, date_to_celebrate_str) -> list[tuple[str,str,str]]: 
    date_to_celebrate = datetime.strptime(date_to_celebrate_str, '%m/%d').date()
    birthday_humans = []
    for human in people :
        birthday_date_str = human[2]
        birthday_date = datetime.strptime(birthday_date_str, '%Y/%m/%d').date()
        if date_to_celebrate.day == birthday_date.day and date_to_celebrate.month == birthday_date.month : 
            birthday_humans.append(human)
    return birthday_humans
