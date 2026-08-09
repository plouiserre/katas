from BirthdayGreetings.domain.AddressBook import AddressBook
from BirthdayGreetings.domain.Contact import Contact
from BirthdayGreetings.tests.asserting import assert_contact
from BirthdayGreetings.tests.factory.contact_factory import ContactFactory
from BirthdayGreetings.tests.fake.contact_manager_fake import ContactManagerFake

def test_search_contact_with_11_12_birthday_and_return_anne_hathaway():  
    address_book_driver = AddressBookDriver()
    birthdays_persons = (address_book_driver
                         .add_contact(ContactFactory.create_contact_male_random("Damon", "1970/10/08"))
                         .add_contact(ContactFactory.create_contact_female_random("Hathaway", "1982/11/12"))
                         .add_contact(ContactFactory.create_contact_male_random("Holland", "1996/06/01" ))
                        .add_date_to_study("2026/11/12")
                        .search_birthdays_persons())
    
    assert_contact(birthdays_persons[0], "Hathaway", "1982/11/12")

def test_search_contact_with_05_25_birthday_and_return_cillian_murphy():
    address_book_driver = AddressBookDriver()
    birthdays_persons =  (address_book_driver
                          .add_contact(ContactFactory.create_contact_male_random("Murphy", "1976/05/25" ))
                          .add_contact(ContactFactory.create_contact_female_random("Blunt", "1983/02/23" ))
                          .add_contact(ContactFactory.create_contact_male_random("Downey", "1965/04/04" ))
                          .add_date_to_study("2026/05/25")
                          .search_birthdays_persons())
    
    assert_contact(birthdays_persons[0], "Murphy", "1976/05/25")

def test_search_contact_with_good_month_and_bad_day_birthday_and_return_no_one():
    address_book_driver = AddressBookDriver()
    birthdays_persons = (address_book_driver
                         .add_contact(ContactFactory.create_contact_male_random("Washington", "1984/07/28" ))
                         .add_contact(ContactFactory.create_contact_male_random("Pattinson", "1986/05/13" ))
                         .add_contact(ContactFactory.create_contact_female_random("Debicki", "1990/08/24" ))
                         .add_date_to_study("2026/08/25")
                         .search_birthdays_persons())
    
    assert ([], birthdays_persons)

def test_search_contact_with_bad_month_and_good_day_birthday_and_return_no_one():
    address_book_driver = AddressBookDriver()
    birthdays_persons =  (address_book_driver
                            .add_contact(ContactFactory.create_contact_male_random("Whitehead", "1997/07/18" ))
                            .add_contact(ContactFactory.create_contact_male_random("Glynn-Carney", "1995/02/07" ))
                            .add_contact(ContactFactory.create_contact_male_random("Lowden", "1990/06/02" ))
                            .add_date_to_study("2026/08/18")
                            .search_birthdays_persons())
        
    assert ([], birthdays_persons)    

def test_search_contact_with_11_11_birthday_and_return_demi_moore_and_leonardo_dicaprio():
    address_book_driver = AddressBookDriver()
    birthdays_persons =   (address_book_driver
                            .add_contact(ContactFactory.create_contact_female_random("Moore", "1962/11/11" ))
                            .add_contact(ContactFactory.create_contact_male_random("Glynn-Carney", "1995/02/07" ))
                            .add_contact(ContactFactory.create_contact_male_random("DiCaprio", "1974/11/11"))
                            .add_date_to_study("2026/11/11")
                            .search_birthdays_persons())
    
    assert_contact(birthdays_persons[0], "Moore", "1962/11/11")
    assert_contact(birthdays_persons[1], "DiCaprio", "1974/11/11") 
    
def test_search_contact_with_29_02_birthday_in_a_leap_year_the_28_02():
    address_book_driver = AddressBookDriver()
    birthdays_persons =  (address_book_driver
                            .add_contact(ContactFactory.create_contact_male_random("Kent", "1988/09/30" ))
                            .add_contact(ContactFactory.create_contact_female_random("Prince", "1992/02/29" ))
                            .add_contact(ContactFactory.create_contact_male_random("Wayne", "1989/03/28"))
                          .add_date_to_study("2028/02/28")
                          .search_birthdays_persons())
    
    assert ([] == birthdays_persons)    

def test_search_contact_with_29_02_birthday_in_a_leap_year_the_29_02():
    address_book_driver = AddressBookDriver()
    birthdays_persons = (address_book_driver
                            .add_contact(ContactFactory.create_contact_male_random("Kent", "1988/09/30" ))
                            .add_contact(ContactFactory.create_contact_female_random("Prince", "1992/02/29" ))
                            .add_contact(ContactFactory.create_contact_male_random("Wayne", "1989/03/28"))
                            .add_date_to_study("2028/02/29")
                            .search_birthdays_persons())

    assert_contact(birthdays_persons[0], "Prince", "1992/02/29")

def test_search_contact_with_29_02_birthday_in_normal_year_the_28_02():
    address_book_driver = AddressBookDriver()
    birthdays_persons = (address_book_driver
                            .add_contact(ContactFactory.create_contact_male_random("Kent", "1988/09/30" ))
                            .add_contact(ContactFactory.create_contact_female_random("Prince", "1992/02/29" ))
                            .add_contact(ContactFactory.create_contact_male_random("Wayne", "1989/03/28"))
                            .add_date_to_study("2026/02/28")
                            .search_birthdays_persons())
    
    assert_contact(birthdays_persons[0], "Prince", "1992/02/29")

class AddressBookDriver : 
    def __init__(self):
        self.address_book = None 
        self.contacts = []
        self.date_to_study = ""
        self.contact_manager = ContactManagerFake()

    def add_contact(self, contact_to_add): 
        self.contact_manager.add_contact(contact_to_add)
        return self

    def add_contacts(self, contacts_to_add : list[Contact]):
        self.contact_manager.add_contacts(contacts_to_add)
        return self

    def add_date_to_study(self, date_to_study : str): 
        self.date_to_study = date_to_study
        return self
    
    def search_birthdays_persons(self) -> list[Contact]: 
        address_book = AddressBook(self.contact_manager)
        return address_book.search_birthday_persons_with_this_date(self.date_to_study)