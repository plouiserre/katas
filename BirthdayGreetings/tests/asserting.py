from BirthdayGreetings.domain.Contact import Contact

def assert_contact(contact: Contact, last_name:str, birthday:str):
    assert (last_name == contact.last_name)
    assert (birthday == contact.birthday)