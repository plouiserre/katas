from datetime import datetime

from BirthdayGreetings.domain.ContactManager import ContactManager

class AddressBook : 
    def __init__(self, contact_manager : ContactManager):
        self.contact_manager = contact_manager

    def search_birthday_persons_with_this_date(self, date_str) -> list: 
        birthday_contacts = []
        self.all_contacts = self.contact_manager.get_all_contacts()
        for contact in self.all_contacts :
            it_is_birthday_contact = contact.is_birthday_today(date_str)
            if it_is_birthday_contact : 
                birthday_contacts.append(contact)
        return birthday_contacts