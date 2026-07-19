from BirthdayGreetings.adapters.Mapper.ContactMapper import txt_to_contacts
from BirthdayGreetings.domain.ContactManager import ContactManager
from typing import Iterator

from BirthdayGreetings.domain.Contact import Contact

class ContactManagerTxt(ContactManager):
    def get_all_contacts() ->Iterator[Contact]:
        all_contacts = []
        with open("BirthdayGreetings/data/contacts.txt", "r") as file : 
            content = file.read()
            all_contacts = txt_to_contacts(content)
        return all_contacts