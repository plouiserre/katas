from BirthdayGreetings.adapters.Mapper.ContactMapper import json_to_contacts
from BirthdayGreetings.domain.ContactManager import ContactManager
from typing import Iterator

from BirthdayGreetings.domain.Contact import Contact

class ContactManagerJson(ContactManager):
    def get_all_contacts(self) -> Iterator[Contact]:
        all_contacts = []
        with open("BirthdayGreetings/data/contacts.json", "r") as file : 
            content = file.read()
            all_contacts = json_to_contacts(content)
        return all_contacts