import math

from  decimal import Decimal

from TricountV2.MoneyLogic.cannot_divide_by_zero_exception import CannotDivideByZeroException
from TricountV2.MoneyLogic.Operation.last_result_needed import LastResultNeeded
from TricountV2.MoneyLogic.operand import Operand
from TricountV2.MoneyLogic.Operation.addition import Addition
from TricountV2.MoneyLogic.Operation.division import Division
from TricountV2.MoneyLogic.Operation.multiplication import Multiplication
from TricountV2.MoneyLogic.Operation.substraction import Substraction
from TricountV2.MoneyLogic.rounded_type import RoundedType

class Money: 
    def __init__(self, rounded_type):
        self.final_result = Decimal("0.0")
        self.rounded_type = rounded_type
        self.all_ops = []
        
    def add_two_money(self, first_number_str: str, second_number_str: str, last_result_needed : LastResultNeeded):
        self.all_ops.append(Addition(first_number_str, second_number_str, Operand.Add, last_result_needed))
        
    def substract_two_money(self, first_number_str: str, second_number_str: str, last_result_needed : LastResultNeeded):
        self.all_ops.append(Substraction(first_number_str, second_number_str, Operand.Soustract, last_result_needed))
        
    def multiply_two_money(self, first_number_str: str, second_number_str: str, last_result_needed : LastResultNeeded):
        self.all_ops.append(Multiplication(first_number_str, second_number_str, Operand.Multiply, last_result_needed))
        
    def divide_two_money(self, first_number_str: str, second_number_str: str, last_result_needed : LastResultNeeded):
        if second_number_str == "0":
            raise CannotDivideByZeroException("Cannot divide by 0")
        else:
            self.all_ops.append(Division(first_number_str, second_number_str, Operand.Divide, last_result_needed)) 

    def calculate_all_op_with_not_display(self):
        return self.__calculate_all_operations()

    def display_final_result_from_all_operations(self, result_to_display): 
        if self.rounded_type == RoundedType.BELOW  : 
            display = str(math.floor(result_to_display * 100)/100.0)
        else : 
            display = str(math.ceil(result_to_display * 100)/100.0)
        return display        
    
    def display_final_result(self):
        display = ""
        last_result = self.__calculate_all_operations()
        if self.rounded_type == RoundedType.BELOW  : 
            display = str(math.floor(last_result * 100)/100.0)
        else : 
            display = str(math.ceil(last_result * 100)/100.0)
        return display
    
    def __calculate_all_operations(self):
        last_result = Decimal("0")
        for op in self.all_ops : 
            last_result = op.calculate(last_result)
        return last_result