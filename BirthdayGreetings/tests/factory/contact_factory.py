import random
from BirthdayGreetings.domain.Contact import Contact

class ContactFactory : 
    first_name_female_possibility = ["Anne", "Emily", "Elizabeth", "Demi", "Diana", "Emma", "Maggie", "Jessica"]

    @staticmethod
    def create_contact_male_random(last_name, datebirthday):
        first_name_male_possibility = ["John", "Peter", "Tom", "Daniel", "Coltrane", "Rupert", "Cillian", "Robert", "John-David", "Fionn", "Jack", "Leonardo", 
                                       "Clark", "Bruce", "Matthew", "Michael", "Christian", "Gary"]
        first_name_choosen = random.randint(0, len(first_name_male_possibility) - 1)
        return Contact(first_name_choosen, last_name, datebirthday)

    @staticmethod
    def create_contact_female_random(last_name, datebirthday):
        first_name_female_possibility = ["Anne", "Emily", "Elizabeth", "Demi", "Diana", "Emma", "Maggie", "Jessica"]
        first_name_choosen = random.randint(0, len(first_name_female_possibility) - 1)
        return Contact(first_name_choosen, last_name, datebirthday)