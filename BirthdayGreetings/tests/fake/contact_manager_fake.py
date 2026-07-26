from BirthdayGreetings.domain.ContactManager import ContactManager

class ContactManagerFake(ContactManager): 
    def __init__(self, all_contacts_memory):
        super().__init__()
        self.all_contacts = all_contacts_memory

    def get_all_contacts(self):
        return self.all_contacts