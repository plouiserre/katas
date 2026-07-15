import json
from typing import Iterator

from BirthdayGreetings.Contact import Contact
def test_1():
    text = "Matt|Damon|1970/10/8\nTom|Holland|1996/6/1\nAnne|Hathaway|1982/11/12\nRobert|Pattinson|1986/5/13\nLupita|Nyong'o|1983/3/1\nSamantha|Morton|1977/5/13\n"
    assert([Contact("Matt", "Damon", "1970/10/8"), Contact("Tom", "Holland", "1996/6/1"), Contact("Anne", "Hathaway", "1982/11/12"),
            Contact("Robert", "Pattinson", "1986/5/13"), Contact("Lupita", "Nyong'o", "1983/3/1"), 
            Contact("Samantha", "Morton", "1977/5/13")] == transform_text_from_txt_to_list_contact(text))


def transform_text_from_txt_to_list_contact(text : str) -> Iterator[Contact]:
    lines = text.split("\n") 
    contacts = []
    for line in lines : 
        if line != '':
            elements = line.split("|")
            new_contact = Contact(elements[0],elements[1], elements[2])
            contacts.append(new_contact)
    return contacts

def test_2():
    text = '[{"firstname":"Matt", "lastname":"Damon", "date of birth":"1970/10/8"},\n{"firstname":"Tom", "lastname":"Holland", "date of birth":"1996/6/1"},\n{"firstname":"Anne", "lastname":"Hathaway", "date of birth":"1982/11/12"},\n{"firstname":"Robert", "lastname":"Pattinson", "date of birth":"1986/5/13"},\n{"firstname":"Lupita", "lastname":"Nyong\'o", "date of birth":"1983/3/1"},\n{"firstname":"Samantha", "lastname":"Morton", "date of birth":"1977/5/13"}\n]'
    assert([Contact("Matt", "Damon", "1970/10/8"), Contact("Tom", "Holland", "1996/6/1"), Contact("Anne", "Hathaway", "1982/11/12"),
            Contact("Robert", "Pattinson", "1986/5/13"), Contact("Lupita", "Nyong'o", "1983/3/1"), 
            Contact("Samantha", "Morton", "1977/5/13")] == transform_text_from_json_to_list_contact(text))

def transform_text_from_json_to_list_contact(text : str) -> Iterator[Contact]:
    contacts = []
    clean_txt = text.replace("\n", "")
    datas = json.loads(clean_txt)
    for data_contact in datas : 
        contacts.append(Contact(data_contact["firstname"], data_contact["lastname"], data_contact["date of birth"]))
    return contacts