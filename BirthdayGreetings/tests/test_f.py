from unittest.mock import Mock

from BirthdayGreetings.BirthdayCollaborators import BirthdayCollaborators
from BirthdayGreetings.Contact import Contact
from BirthdayGreetings.DateOfTheDay import DateOfTheDay
from BirthdayGreetings.Template import Template

def test_1(): 
    message_birthdays = ["Happy Birthday, dear Daniel !", "Happy Birthday, dear Emma !","Happy Birthday, dear Rupert !"]
    assert(message_birthdays == greetings_birthdays())

def greetings_birthdays():    
    contact_manager = Mock()
    contact_manager.get_all_contacts.return_value = [Contact("Daniel", "Radcliffe", "1989/07/19"), 
     Contact("Emma", "Watson", "1992/07/19"),
     Contact("Coltrane", "Robbie", "1950/03/30"),
     Contact("Maggie", "Smith", "1934/12/28"),
     Contact("Rupert", "Grint", "1988/07/19")]
    
    template_manager = Mock()
    template_manager.get_template_message.return_value = Template("Happy Birthday, dear <first_name> !", "<first_name>")    

    date_of_the_day = DateOfTheDay("2026/07/19")
    
    birthday_collaborators = BirthdayCollaborators(contact_manager, date_of_the_day, template_manager)
    return birthday_collaborators.GreetingsBirthday()