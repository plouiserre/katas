from datetime import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class Contact : 
    first_name : str
    last_name : str
    birthday :str

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name and self.birthday == other.birthday

    def is_birthday_today(self, date_to_study, is_leap_year):
        date_to_celebrate = datetime.strptime(date_to_study, '%Y/%m/%d').date()
        birthday_date = datetime.strptime(self.birthday, '%Y/%m/%d').date()               
        if birthday_date.day == 29 and birthday_date.month == 2 and date_to_celebrate.day == 28 and date_to_celebrate.month == 2 and is_leap_year == False :
            return True
        elif date_to_celebrate.day == birthday_date.day and date_to_celebrate.month == birthday_date.month : 
            return True
        else : 
            return False