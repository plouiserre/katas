from decimal import Decimal

from abc import ABC, abstractmethod

class Operation(ABC): 
    def __init__(self, first_number, second_number, operand, last_result_needed):
        self.first_number = first_number
        self.second_number = second_number
        self.operand = operand
        self.last_result_needed = last_result_needed
        self.last_result = 0
    
    @abstractmethod
    def calculate(last_result : Decimal):
        pass