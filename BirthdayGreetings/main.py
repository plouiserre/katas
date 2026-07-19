from BirthdayGreetings.domain.BirthdayCollaborators import BirthdayCollaborators
from BirthdayGreetings.domain.DateOfTheDay import DateOfTheDay

birthday_collaborators = BirthdayCollaborators()

with open("BirthdayGreetings/data/contacts.txt", "r") as file : 
    content = file.read()
    print(content)

with open("BirthdayGreetings/data/contacts.json", "r") as file : 
    content = file.read()
    print(content)

with open("BirthdayGreetings/data/template.txt", "r") as file : 
    content = file.read()
    print(content)

with open("BirthdayGreetings/data/template.json", "r") as file : 
    content = file.read()
    print(content)