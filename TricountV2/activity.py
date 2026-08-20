from decimal import Decimal
from TricountV2.MoneyLogic.Operation.last_result_needed import LastResultNeeded

class Activity : 
    def __init__(self, name, price, number_participants, role):
        self.name = name
        self.price = price
        self.number_participants = number_participants
        self.role = role
    
    
    @staticmethod
    def create(name : str, price : str, number_participants : int, role : str):
        return Activity(name, Decimal(price), number_participants, role)

    def calculate_balance_payer_activity(self, money): 
        money.divide_two_money(self.price, self.number_participants, LastResultNeeded.NotNeeded)
        money.substract_two_money(str(self.price), None, LastResultNeeded.SecondMember)
        return float(money.display_final_result())

    def calculate_balance_freeloader_activity(self, money):
        money.divide_two_money(self.price, self.number_participants, LastResultNeeded.NotNeeded)
        return float(money.display_final_result())