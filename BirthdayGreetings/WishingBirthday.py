from typing import Iterator
from BirthdayGreetings.Contact import Contact
from BirthdayGreetings.Template import Template

class WishingBirthday : 
    def __init__(self, contacts : Iterator[Contact], template : Template):
        self.contacts = contacts
        self.template = template

    def formate_message(self):
        all_messages = []
        for contact in self.contacts : 
            message = self.template.message.replace(self.template.code_to_replace, contact.first_name)
            all_messages.append(message)
        return all_messages