from BirthdayGreetings.domain.BirthdayCollaborators import BirthdayCollaborators
from BirthdayGreetings.domain.Contact import Contact
from BirthdayGreetings.domain.DateOfTheDay import DateOfTheDay
from BirthdayGreetings.tests.fake.contact_manager_fake import ContactManagerFake
from BirthdayGreetings.tests.fake.template_manager_fake import TemplateManagerFake

def test_greetings_harry_potter_cast_birthday(): 
    birthdays_collaborators = __init_birthday_collaborators("2026/07/19", [Contact("Daniel", "Radcliffe", "1989/07/19"), 
    Contact("Emma", "Watson", "1992/07/19"),
    Contact("Coltrane", "Robbie", "1950/03/30"),
    Contact("Maggie", "Smith", "1934/12/28"),
    Contact("Rupert", "Grint", "1988/07/19")], "Happy Birthday, dear <first_name> !", "<first_name>")

    greetings_birthdays = greetings_birthdays_send(birthdays_collaborators)

    __compare_greetings_birthdays_with_expected_contacts(["Happy Birthday, dear Daniel !", "Happy Birthday, dear Emma !","Happy Birthday, dear Rupert !"], greetings_birthdays)

def greetings_birthdays_send(birthday_collaborators : BirthdayCollaborators) -> list[str]:    
    return birthday_collaborators.GreetingsBirthday()

def __init_birthday_collaborators(date_studied, contacts_from_files, template_message, code_to_replace): 
    contact_manager = ContactManagerFake(contacts_from_files)
        
    template_manager = TemplateManagerFake(template_message, code_to_replace)

    date_of_the_day = DateOfTheDay(date_studied)
    
    birthday_collaborators = BirthdayCollaborators(contact_manager, date_of_the_day, template_manager)
    return birthday_collaborators

def __compare_greetings_birthdays_with_expected_contacts(greetings_birthdays_expected, greetings_birthdays_send): 
    assert(greetings_birthdays_expected == greetings_birthdays_send)