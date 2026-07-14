from datetime import datetime
from typing import Iterator

from BirthdayGreetings.Contact import Contact

class AddressBook : 
    def __init__(self, all_contacts : Iterator[Contact]):
        self.all_contacts = all_contacts

    def search_birthday_persons_in_this_date(self, date_str : str): 
        date_to_celebrate = datetime.strptime(date_str, '%m/%d').date()
        birthday_contacts = []
        for contact in self.all_contacts :
            birthday_date = datetime.strptime(contact.birthday, '%Y/%m/%d').date()
            if date_to_celebrate.day == birthday_date.day and date_to_celebrate.month == birthday_date.month : 
                birthday_contacts.append(contact)
        return birthday_contacts