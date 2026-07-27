from BirthdayGreetings.domain.AddressBook import AddressBook
from BirthdayGreetings.domain.Contact import Contact
from BirthdayGreetings.tests.fake.contact_manager_fake import ContactManagerFake

def test_search_contact_with_11_12_birthday_and_return_anne_hathaway():  
    address_book_driver = AddressBookDriver()
    birthdays_persons = (address_book_driver
                         .add_contacts([Contact("Matt", "Damon", "1970/10/08"), Contact("Anne", "Hathaway", "1982/11/12"), 
                                                          Contact("Tom", "Holland", "1996/06/01" )])
                        .add_date_to_study("2026/11/12")
                        .search_birthdays_persons())
    
    assert ([Contact("Anne", "Hathaway", "1982/11/12")] == birthdays_persons)

def test_search_contact_with_05_25_birthday_and_return_cillian_murphy():
    address_book_driver = AddressBookDriver()
    birthdays_persons =  (address_book_driver
                          .add_contacts([Contact("Cillian", "Murphy", "1976/05/25" ), Contact("Emily", "Blunt", "1983/02/23" ),
                                    Contact("Robert", "Downey", "1965/04/04" )])
                            .add_date_to_study("2026/05/25")
                            .search_birthdays_persons())
    
    assert ([Contact("Cillian", "Murphy", "1976/05/25")] == birthdays_persons)

def test_search_contact_with_good_month_and_bad_day_birthday_and_return_no_one():
    address_book_driver = AddressBookDriver()
    birthdays_persons = (address_book_driver
                         .add_contacts([Contact("John-David", "Washington", "1984/07/28" ), Contact("Robert", "Pattinson", "1986/05/13" ),
                                    Contact("Elizabeth", "Debicki", "1990/08/24" )])
                         .add_date_to_study("2026/08/25")
                         .search_birthdays_persons())
    
    assert ([], birthdays_persons)

def test_search_contact_with_bad_month_and_good_day_birthday_and_return_no_one():
    address_book_driver = AddressBookDriver()
    birthdays_persons =  (address_book_driver
                          .add_contacts([Contact("Fionn", "Whitehead", "1997/07/18" ), Contact("Tom", "Glynn-Carney", "1995/02/07" ),
                                    Contact("Jack", "Lowden", "1990/06/02" )])
                            .add_date_to_study("2026/08/18")
                            .search_birthdays_persons())
        
    assert ([], birthdays_persons)    

def test_search_contact_with_11_11_birthday_and_return_demi_moore_and_leonardo_dicaprio():
    address_book_driver = AddressBookDriver()
    birthdays_persons =   (address_book_driver
                           .add_contacts([Contact("Demi", "Moore", "1962/11/11" ), Contact("Tom", "Glynn-Carney", "1995/02/07" ),
                                    Contact("Leonardo", "DiCaprio", "1974/11/11")])
                            .add_date_to_study("2026/11/11")
                            .search_birthdays_persons())
    
    assert ([Contact("Demi", "Moore", "1962/11/11"),Contact("Leonardo", "DiCaprio", "1974/11/11")] == birthdays_persons)    
    
def test_search_contact_with_29_02_birthday_in_a_leap_year_the_28_02():
    address_book_driver = AddressBookDriver()
    birthdays_persons =  (address_book_driver
                          .add_contacts([Contact("Clark", "Kent", "1988/09/30" ), Contact("Diana", "Prince", "1992/02/29" ),
                                    Contact("Bruce", "Wayne", "1989/03/28")])
                          .add_date_to_study("2028/02/28")
                          .search_birthdays_persons())
    
    assert ([] == birthdays_persons)    

def test_search_contact_with_29_02_birthday_in_a_leap_year_the_29_02():
    address_book_driver = AddressBookDriver()
    birthdays_persons = (address_book_driver
                         .add_contacts([Contact("Clark", "Kent", "1988/09/30" ), Contact("Diana", "Prince", "1992/02/29" ),
                                    Contact("Bruce", "Wayne", "1989/03/28")])
                        .add_date_to_study("2028/02/29")
                        .search_birthdays_persons())
    
    assert ([Contact("Diana", "Prince", "1992/02/29" )] == birthdays_persons)  

def test_search_contact_with_29_02_birthday_in_normal_year_the_28_02():
    address_book_driver = AddressBookDriver()
    birthdays_persons = (address_book_driver
                         .add_contacts([Contact("Clark", "Kent", "1988/09/30" ), Contact("Diana", "Prince", "1992/02/29" ),
                                    Contact("Bruce", "Wayne", "1989/03/28")])
                        .add_date_to_study("2026/02/28")
                        .search_birthdays_persons())
    
    assert ([Contact("Diana", "Prince", "1992/02/29" )] == birthdays_persons)  

class AddressBookDriver : 
    def __init__(self):
        self.address_book = None 
        self.contacts = []
        self.date_to_study = ""

    def add_contacts(self, contacts_to_add : list[Contact]):
        for contact in contacts_to_add :
            self.contacts.append(contact)
        return self

    def add_date_to_study(self, date_to_study : str): 
        self.date_to_study = date_to_study
        return self
    
    def search_birthdays_persons(self) -> list[Contact]: 
        contact_manager = ContactManagerFake(self.contacts)
        address_book = AddressBook(contact_manager)
        return address_book.search_birthday_persons_in_this_date(self.date_to_study)