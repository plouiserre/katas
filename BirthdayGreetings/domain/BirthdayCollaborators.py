from BirthdayGreetings.domain.AddressBook import AddressBook
from BirthdayGreetings.domain.DateOfTheDay import DateOfTheDay
from BirthdayGreetings.domain.WishingBirthday import WishingBirthday

class BirthdayCollaborators : 
    def __init__(self, contact_manager, template_manager):
        self.contact_manager = contact_manager
        self.template_manager = template_manager

    def GreetingsBirthday(self, date_str): 
        address_book = AddressBook(self.contact_manager)
        persons_to_greet = address_book.search_birthday_persons_with_this_date(date_str)

        template = self.template_manager.get_template_message()

        wishing_birthday = WishingBirthday(persons_to_greet, template)
        messages = wishing_birthday.formate_message()
        return messages