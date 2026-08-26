from decimal import Decimal
from enum import Enum
from Tricount.MoneyLogic.Operation.last_result_needed import LastResultNeeded

class ParticipationType(Enum) : 
    FREELOADER = 0
    PAYER = 1

class Participation : 
    def __init__(self, name, price, number_participants, role):
        self.name = name
        self.price = price
        self.number_participants = number_participants
        self.role = role
    
    
    @staticmethod
    def create(name : str, price : str, number_participants : int, role : str):
        return Participation(name, Decimal(price), number_participants, role)

    def calculate_balance_payer_participation(self, money): 
        money.divide_two_money(self.price, self.number_participants, LastResultNeeded.NotNeeded)
        money.substract_two_money(str(self.price), None, LastResultNeeded.SecondMember)
        
    def calculate_balance_freeloader_participation(self, money):
        money.divide_two_money(self.price, self.number_participants, LastResultNeeded.NotNeeded)
        