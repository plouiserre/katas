from BirthdayGreetings.domain.Contact import Contact
from BirthdayGreetings.domain.ContactManager import ContactManager

class ContactManagerFake(ContactManager): 
    def __init__(self):
        super().__init__()
        self.all_contacts = []

    def add_contacts(self, contacts_to_add : list[Contact]):
        for contact in contacts_to_add :
            self.all_contacts.append(contact)
        return self

    def get_all_contacts(self):
        return self.all_contacts