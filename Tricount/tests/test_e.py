from dataclasses import dataclass

import math
import pytest

from  decimal import Decimal
from enum import Enum

from Tricount.cannot_divide_by_zero_exception import CannotDivideByZeroException

def test_1(): 
    final_money = (MoneyDriver(RoundedType.BELOW)
             .add("5.3", "6.5")
             .display_final_result())

    assert("11.8" == final_money)

def test_2(): 
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .substract("11.9", "4.3")
                   .display_final_result())

    assert("7.6" == final_money)

def test_3(): 
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .multiply("33.4", "0.2")
                   .display_final_result())
    assert("6.68" == final_money)

def test_4(): 
    final_money = (MoneyDriver(RoundedType.BELOW)
                       .multiply("33.4", "0.21")
                       .display_final_result())
    assert("7.01" == final_money)

def test_5(): 
    final_money = (MoneyDriver(RoundedType.UP)
                       .multiply("33.4", "0.21")
                       .display_final_result())
    assert("7.02" == final_money)

def test_6(): 
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .divide("8", "2.5")
                   .display_final_result())
    assert("3.2" == final_money)

def test_7(): 
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .divide("20", "2.54")
                   .display_final_result())
    assert("7.87" == final_money)

def test_8(): 
    final_money = (MoneyDriver(RoundedType.UP)
                   .divide("20", "2.54")
                   .display_final_result())
    assert("7.88" == final_money)
    
def test_9():
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .add("9.87", "2.32")
                   .substract(None, "43.23")
                   .multiply(None, "93.23")
                   .divide(None, "7.3")
                   .display_final_result())
    assert("-396.42" == final_money)

def test_10():
    final_money = (MoneyDriver(RoundedType.UP)
                   .add("9.87", "2.32")
                   .substract(None, "43.23")
                   .multiply(None, "93.23")
                   .divide(None, "7.3")
                   .display_final_result())
    assert("-396.41" == final_money)
    
def test_11():
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .add("9.87", "2.32")
                   .substract(None, "3.23")
                   .multiply(None, "93.23")
                   .divide(None, "7.3")
                   .display_final_result())
    assert("114.43" == final_money)

def test_12():
    final_money = (MoneyDriver(RoundedType.UP)
                   .add("9.87", "2.32")
                   .substract(None, "3.23")
                   .multiply(None, "93.23")
                   .divide(None, "7.3")
                   .display_final_result())
    assert("114.44" == final_money)

def test_13():
    with pytest.raises(CannotDivideByZeroException) :
        (MoneyDriver(RoundedType.BELOW)
                   .divide("89.2", "0"))
def test_14():
    with pytest.raises(CannotDivideByZeroException) :
        (MoneyDriver(RoundedType.BELOW)
                   .add("93", "2")
                   .divide("89.2", "0"))

class MoneyDriver : 
    def __init__(self, rounded_type):
        self.final_result = Decimal("0.0")
        self.rounded_type = rounded_type
        self.all_ops = []

    def add(self, first_number_str : str, second_number_str : str): 
        if first_number_str != None : 
            self.all_ops.append(Operation(first_number_str, second_number_str, Operand.Add, False))
        else : 
            self.all_ops.append(Operation(None, second_number_str, Operand.Add, True))
        return self

    def substract(self, first_number_str : str, second_number_str : str): 
        if first_number_str != None : 
            self.all_ops.append(Operation(first_number_str, second_number_str, Operand.Soustract, False))
        else : 
            self.all_ops.append(Operation(None, second_number_str, Operand.Soustract, True))      
        return self

    def multiply(self, first_number_str : str, second_number_str : str): 
        if first_number_str != None : 
            self.all_ops.append(Operation(first_number_str, second_number_str, Operand.Multiply, False))
        else : 
            self.all_ops.append(Operation(None, second_number_str, Operand.Multiply, True))      
        return self

    def divide(self, first_number_str : str, second_number_str : str):
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
                

class RoundedType(Enum):
    BELOW = -1
    UP = 1
    
class Operand(Enum): 
    Add = 1
    Soustract = 2
    Multiply = 3
    Divide = 4
    
@dataclass
class Operation(): 
    first_number : str
    second_number : str
    operand : Operand
    is_last_result_needed : bool