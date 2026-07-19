from BirthdayGreetings.domain.BirthdayCollaborators import BirthdayCollaborators
from BirthdayGreetings.adapters.driven.ContactManagerTxt import ContactManagerTxt
from BirthdayGreetings.domain.DateOfTheDay import DateOfTheDay
from BirthdayGreetings.adapters.driven.TemplateManagerTxt import TemplateManagerTxt

def greetings_birthday_employees(date_to_evaluate):
    contact_manager_txt = ContactManagerTxt()
    date_of_the_day = DateOfTheDay(date_to_evaluate)
    template_manager_txt = TemplateManagerTxt()
    birthday_collaborators = BirthdayCollaborators(contact_manager_txt, date_of_the_day, template_manager_txt)
    messages_birthday_employees = birthday_collaborators.GreetingsBirthday(date_to_evaluate)
    for message in messages_birthday_employees : 
        print(message)