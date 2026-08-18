import math

from  decimal import Decimal

from Tricount.MoneyLogic.cannot_divide_by_zero_exception import CannotDivideByZeroException
from Tricount.MoneyLogic.operand import Operand
from Tricount.MoneyLogic.operation import Operation
from Tricount.MoneyLogic.rounded_type import RoundedType

class Money: 
    def __init__(self, rounded_type):
        self.final_result = Decimal("0.0")
        self.rounded_type = rounded_type
        self.all_ops = []
        
    def add_two_money(self, first_number_str: str, second_number_str: str):
        if first_number_str != None : 
            self.all_ops.append(Operation(first_number_str, second_number_str, Operand.Add, False))
        else : 
            self.all_ops.append(Operation(None, second_number_str, Operand.Add, True))
        return self
    
    def substract_two_money(self, first_number_str: str, second_number_str: str):
        if first_number_str != None : 
            self.all_ops.append(Operation(first_number_str, second_number_str, Operand.Soustract, False))
        else : 
            self.all_ops.append(Operation(None, second_number_str, Operand.Soustract, True))      
        return self
    
    def multiply_two_money(self, first_number_str: str, second_number_str: str):
        if first_number_str != None : 
            self.all_ops.append(Operation(first_number_str, second_number_str, Operand.Multiply, False))
        else : 
            self.all_ops.append(Operation(None, second_number_str, Operand.Multiply, True))      
        return self
    
    def divide_two_money(self, first_number_str: str, second_number_str: str):
        if second_number_str == "0":
            raise CannotDivideByZeroException("Cannot divide by 0")
        elif first_number_str != None : 
            self.all_ops.append(Operation(first_number_str, second_number_str, Operand.Divide, False))
        else : 
            self.all_ops.append(Operation(None, second_number_str, Operand.Divide, True))      
        return self
    
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
            if op.operand == Operand.Add:
                if op.is_last_result_needed == False : 
                    last_result = Decimal(op.first_number) + Decimal(op.second_number) 
                else : 
                    last_result = last_result + Decimal(op.second_number)
            elif op.operand == Operand.Soustract : 
                if op.is_last_result_needed == False : 
                    last_result = Decimal(op.first_number) - Decimal(op.second_number) 
                else : 
                    last_result = last_result - Decimal(op.second_number)
            elif op.operand == Operand.Multiply : 
                if op.is_last_result_needed == False : 
                    last_result = Decimal(op.first_number) * Decimal(op.second_number) 
                else : 
                    last_result = last_result * Decimal(op.second_number) 
            else : 
                if op.is_last_result_needed == False : 
                    last_result = Decimal(op.first_number) / Decimal(op.second_number) 
                else :
                    last_result = last_result / Decimal(op.second_number)
        return last_result