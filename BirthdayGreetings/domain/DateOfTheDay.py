from datetime import datetime

class DateOfTheDay :
    def __init__(self, date_to_evaluate_str):
        self.date_to_evaluate_str = date_to_evaluate_str

    def is_date_belongs_to_a_leap_of_year(self):
        date_to_evaluate = datetime.strptime(self.date_to_evaluate_str, '%Y/%m/%d').date()
        year = date_to_evaluate.year
        if year % 4 == 0 and year % 100 != 0 : 
            return True
        elif year %4 == 0 and year % 100 == 0 and year % 400 == 0 : 
            return True
        else :
            return False