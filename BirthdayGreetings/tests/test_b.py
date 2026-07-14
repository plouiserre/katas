from typing import Iterator
from BirthdayGreetings.Contact import Contact
from BirthdayGreetings.Template import Template

def test_1():
    contacts = [Contact("Matthew", "McConaughey", "1969/07/14"), 
                Contact("Michael", "Caine", "1933/07/14"),
                Contact("Jessica", "Chastain", "1977/07/14" )]
    template = Template("Happy birthday, dear <first_name>!", "<first_name>")
    
    messages = wish_birthdays(contacts, template)
    assert(3 == len(messages))
    assert("Happy birthday, dear Matthew!", messages[0])
    assert("Happy birthday, dear Michael!", messages[1])
    assert("Happy birthday, dear Jessica!", messages[2])

    
def test_2():
    contacts = [Contact("Christian", "Bale", "1974/07/14"), 
                Contact("Gary", "Oldman", "1958/07/14"),
                Contact("Tom", "Hardy", "1977/07/14" )]
    template = Template("Happy birthday, dear <first_name>!", "<first_name>")
    
    messages = wish_birthdays(contacts, template)
    assert(3 == len(messages))
    assert("Happy birthday, dear Christian!", messages[0])
    assert("Happy birthday, dear Gary!", messages[1])
    assert("Happy birthday, dear Tom!", messages[2])

def wish_birthdays(contacts: Iterator[Contact], template : Template) -> list[str]:
    all_messages = []
    for contact in contacts : 
        message = template.message.replace(template.code_to_replace, contact.first_name)
        all_messages.append(message)
    return all_messages