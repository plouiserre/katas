from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Activity : 
    name : str
    price : Decimal
    number_participants : int 
    role : str
    
    @staticmethod
    def create(name : str, price : str, number_participants : int, role : str):
        return Activity(name, Decimal(price), number_participants, role)