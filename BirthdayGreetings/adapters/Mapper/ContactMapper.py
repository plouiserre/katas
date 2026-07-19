import json
from typing import Iterator

from BirthdayGreetings.domain.Contact import Contact

def json_to_contacts(json_contacts :str) ->Iterator[Contact]:
    contacts = []
    clean_txt = json_contacts.replace("\n", "")
    datas = json.loads(clean_txt)
    for data_contact in datas : 
        contacts.append(Contact(data_contact["firstname"], data_contact["lastname"], data_contact["date of birth"]))
    return contacts

def txt_to_contacts(txt_contacts : str) -> Iterator[Contact] :
    lines = txt_contacts.split("\n") 
    contacts = []
    for line in lines : 
        if line != '':
            elements = line.split("|")
            new_contact = Contact(elements[0],elements[1], elements[2])
            contacts.append(new_contact)
    return contacts