from BirthdayGreetings.Contact import Contact
from BirthdayGreetings.ContactMapper import json_to_contacts, txt_to_contacts

def test_map_contacts_from_txt_file_to_list_contact():
    text = "Matt|Damon|1970/10/8\nTom|Holland|1996/6/1\nAnne|Hathaway|1982/11/12\nRobert|Pattinson|1986/5/13\nLupita|Nyong'o|1983/3/1\nSamantha|Morton|1977/5/13\n"
    assert([Contact("Matt", "Damon", "1970/10/8"), Contact("Tom", "Holland", "1996/6/1"), Contact("Anne", "Hathaway", "1982/11/12"),
            Contact("Robert", "Pattinson", "1986/5/13"), Contact("Lupita", "Nyong'o", "1983/3/1"), 
            Contact("Samantha", "Morton", "1977/5/13")] == txt_to_contacts(text))

def test_map_contacts_from_json_file_to_list_contact():
    text = '[{"firstname":"Matt", "lastname":"Damon", "date of birth":"1970/10/8"},\n{"firstname":"Tom", "lastname":"Holland", "date of birth":"1996/6/1"},\n{"firstname":"Anne", "lastname":"Hathaway", "date of birth":"1982/11/12"},\n{"firstname":"Robert", "lastname":"Pattinson", "date of birth":"1986/5/13"},\n{"firstname":"Lupita", "lastname":"Nyong\'o", "date of birth":"1983/3/1"},\n{"firstname":"Samantha", "lastname":"Morton", "date of birth":"1977/5/13"}\n]'
    assert([Contact("Matt", "Damon", "1970/10/8"), Contact("Tom", "Holland", "1996/6/1"), Contact("Anne", "Hathaway", "1982/11/12"),
            Contact("Robert", "Pattinson", "1986/5/13"), Contact("Lupita", "Nyong'o", "1983/3/1"), 
            Contact("Samantha", "Morton", "1977/5/13")] == json_to_contacts(text))