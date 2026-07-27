from BirthdayGreetings.domain.BirthdayCollaborators import BirthdayCollaborators
from BirthdayGreetings.domain.Contact import Contact
from BirthdayGreetings.domain.Template import Template
from BirthdayGreetings.tests.fake.contact_manager_fake import ContactManagerFake
from BirthdayGreetings.tests.fake.template_manager_fake import TemplateManagerFake

def test_greetings_harry_potter_cast_birthday(): 
    driver = BirthdayCollaboratorsDriver()
    greetings_birthdays = (driver
                           .add_contacts([Contact("Daniel", "Radcliffe", "1989/07/19"), Contact("Emma", "Watson", "1992/07/19"),
                                          Contact("Coltrane", "Robbie", "1950/03/30"),Contact("Maggie", "Smith", "1934/12/28"),
                                          Contact("Rupert", "Grint", "1988/07/19")])
                            .add_date_to_study("2026/07/19")
                            .add_template_message("Happy Birthday, dear <first_name> !", "<first_name>")
                            .birthday_messages_send())  
    assert(greetings_birthdays == ["Happy Birthday, dear Daniel !", "Happy Birthday, dear Emma !","Happy Birthday, dear Rupert !"])                                        

class BirthdayCollaboratorsDriver : 
    def __init__(self):
        self.contacts = []
        self.template = None
        self.date_to_study = ""

    def add_contacts(self, contacts_to_add : list[Contact]):
        for contact in contacts_to_add :
            self.contacts.append(contact)
        return self

    def add_template_message(self, message, str_to_replace) : 
        self.template = Template(message, str_to_replace)
        return self

    def add_date_to_study(self, date_to_study : str): 
        self.date_to_study = date_to_study
        return self

    def birthday_messages_send(self) -> list[str]:
        contact_manager = ContactManagerFake(self.contacts)
        template_manager = TemplateManagerFake(self.template)
        birthday_collaborators = BirthdayCollaborators(contact_manager, template_manager)
        return birthday_collaborators.GreetingsBirthday(self.date_to_study)