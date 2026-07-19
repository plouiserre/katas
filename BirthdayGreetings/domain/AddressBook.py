from datetime import datetime

from BirthdayGreetings.domain.ContactManager import ContactManager

class AddressBook : 
    def __init__(self, contact_manager : ContactManager, date_of_the_day : str):
        self.contact_manager = contact_manager
        self.date_of_the_day = date_of_the_day

    def search_birthday_persons_in_this_date(self, date_str : str) -> list: 
        date_to_celebrate = datetime.strptime(date_str, '%Y/%m/%d').date()
        is_leap_year_problem = self.__is_a_leap_year()
        birthday_contacts = []
        self.all_contacts = self.contact_manager.get_all_contacts()
        for contact in self.all_contacts :
            birthday_date = datetime.strptime(contact.birthday, '%Y/%m/%d').date()
            if birthday_date.day == 29 and birthday_date.month == 2 and date_to_celebrate.day == 28 and date_to_celebrate.month == 2 and is_leap_year_problem == False :
                birthday_contacts.append(contact)
            elif date_to_celebrate.day == birthday_date.day and date_to_celebrate.month == birthday_date.month : 
                birthday_contacts.append(contact)
        return birthday_contacts
    
    def __is_a_leap_year(self):
        return self.date_of_the_day.is_date_belongs_to_a_leap_of_year()