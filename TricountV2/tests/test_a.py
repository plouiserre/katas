from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal

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
    assert("200" == balance_participant)
    
    
class ParticipantDriver : 
    def __init__(self, name):
        self.name = name
        self.activites = []
        self.balance = 0
    
    def add_activities(self, name, price, number_participants, role):
        self.activites.append(Activity.create(name, price, number_participants, role))
        return self
    
    def get_balance(self):
        for activity in self.activites : 
            own_share = self.__get_own_share(activity)
            self.balance += activity.price - own_share
        return str(self.balance)
    
    def __get_own_share(self, activity : Activity):
        return activity.price / activity.number_participants
    
@dataclass
class Activity : 
    name : str
    price : Decimal
    number_participants : int 
    role : str
    
    @staticmethod
    def create(name : str, price : str, number_participants : int, role : str):
        return Activity(name, Decimal(price), number_participants, role)