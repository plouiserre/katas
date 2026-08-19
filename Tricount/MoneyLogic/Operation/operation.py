from decimal import Decimal

from abc import ABC, abstractmethod
from Tricount.MoneyLogic.operand import Operand

class Operation(ABC): 
    def __init__(self, first_number, second_number, operand, is_last_result_needed):
        self.first_number = first_number
        self.second_number = second_number
        self.operand = operand
        self.is_last_result_needed = is_last_result_needed
        self.last_result = 0
    
    @abstractmethod
    def calculate(last_result : Decimal):
        pass