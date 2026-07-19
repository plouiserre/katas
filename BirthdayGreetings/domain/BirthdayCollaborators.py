from BirthdayGreetings.domain.AddressBook import AddressBook
from BirthdayGreetings.domain.WishingBirthday import WishingBirthday

class BirthdayCollaborators : 
    def __init__(self, contact_manager, date_of_the_day, template_manager):
        self.contact_manager = contact_manager
        self.date_of_the_day = date_of_the_day
        self.template_manager = template_manager

    def GreetingsBirthday(self, date_of_the_day): 
        address_book = AddressBook(self.contact_manager, self.date_of_the_day)
        persons_to_greet = address_book.search_birthday_persons_in_this_date(date_of_the_day)

        template = self.template_manager.get_template_message()

        wishing_birthday = WishingBirthday(persons_to_greet, template)
        messages = wishing_birthday.formate_message()
        return messages