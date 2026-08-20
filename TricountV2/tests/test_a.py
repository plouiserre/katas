from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from TricountV2.MoneyLogic.money import Money
from TricountV2.MoneyLogic.Operation.last_result_needed import LastResultNeeded
from TricountV2.MoneyLogic.rounded_type import RoundedType

def test1():
    balance_participant = (ParticipantDriver("Peter")
                           .add_activities("bar", 23, 2, "Payer")
                           .get_balance())
    assert("11.5" == balance_participant)
    
def test2():
    balance_participant = (ParticipantDriver("MJ")
                           .add_activities("massages", 120, 3, "Payer")
                           .add_activities("restaurant", 150, 5, "Payer")
                           .get_balance())
    assert("200.0" == balance_participant)
    
def test3(): 
    balance_participant = (ParticipantDriver("Ned")
                           .add_activities("rent a car", 500, 3, "Payer")
                           .add_activities("jet ski", 99, 4, "Payer")
                           .add_activities("room", 100, 2, "Payer")
                           .get_balance()
                           )
    assert("457.58" == balance_participant)
    
def test4():
    balance_participant = (ParticipantDriver("Harry")
                           .add_activities("bar", 23, 2, "Freeloader")
                           .get_balance())
    assert("-11.5" == balance_participant)
    
def test5():
    balance_participant = (ParticipantDriver("Gwen")
                           .add_activities("massages", 120, 3, "Freeloader")
                           .add_activities("restaurant", 150, 5, "Freeloader")
                           .get_balance())
    assert("-200.0" == balance_participant)
    
def test6(): 
    balance_participant = (ParticipantDriver("Norman")
                           .add_activities("rent a car", 500, 3, "Freeloader")
                           .add_activities("jet ski", 99, 4, "Freeloader")
                           .add_activities("room", 100, 2, "Freeloader")
                           .get_balance()
                           )
    assert("-457.58" == balance_participant)
    
def test7():
    balance_participant = (ParticipantDriver("May")
                          .add_activities("bar", 23, 2, "Freeloader")
                          .add_activities("buy cake", 30, 3, "Payer")
                          .get_balance()
                          )
    assert("8.5" == balance_participant)
    
def test8():
    balance_participant = (ParticipantDriver("Norman")
                           .add_activities("restaurant", 150, 5, "Payer")
                           .add_activities("jet ski", 99, 4, "Freeloader")
                           .add_activities("massages", 120, 3, "Freeloader")
                           .add_activities("icecram", 40, 6, "Payer"))
    assert("" == balance_participant)
    
class ParticipantDriver : 
    def __init__(self, name):
        self.name = name
        self.activites = []
        self.balance = 0
        self.money = Money(RoundedType.BELOW)
    
    def add_activities(self, name, price, number_participants, role):
        self.activites.append(Activity.create(name, price, number_participants, role))
        return self
    
    #TODO optimise
    def get_balance(self):
        for activity in self.activites :
            self.money.divide_two_money(activity.price, activity.number_participants, LastResultNeeded.NotNeeded)
            self.money.substract_two_money(str(activity.price), None, LastResultNeeded.SecondMember)
            if activity.role == "Payer" :  
                self.balance += float(self.money.display_final_result())
            elif activity.role == "Freeloader" : 
                self.balance -= float(self.money.display_final_result())
        return str(self.balance)
    
@dataclass
class Activity : 
    name : str
    price : Decimal
    number_participants : int 
    role : str
    
    @staticmethod
    def create(name : str, price : str, number_participants : int, role : str):
        return Activity(name, Decimal(price), number_participants, role)