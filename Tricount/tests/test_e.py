import math

from  decimal import Decimal
from enum import Enum

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


class MoneyDriver : 
    def __init__(self, rounded_type):
        self.final_result = Decimal("0.0")
        self.rounded_type = rounded_type

    def add(self, first_number_str : str, second_number_str : str): 
        first_number = Decimal(first_number_str)
        second_number = Decimal(second_number_str)
        self.final_result = first_number + second_number
        return self

    def substract(self, first_number_str : str, second_number_str : str): 
        first_number = Decimal(first_number_str)
        second_number = Decimal(second_number_str)
        self.final_result = first_number - second_number
        return self

    def multiply(self, first_number_str : str, second_number_str : str): 
        first_number = Decimal(first_number_str)
        second_number = Decimal(second_number_str)
        self.final_result = first_number * second_number
        return self

    def divide(self, first_number_str : str, second_number_str : str):
        first_number = Decimal(first_number_str)
        second_number = Decimal(second_number_str)
        self.final_result = first_number / second_number
        return self

    def display_final_result(self): 
        display = ""
        if self.rounded_type == RoundedType.BELOW  : 
            display = str(math.floor(self.final_result * 100)/100.0)
        else : 
            display = str(math.ceil(self.final_result * 100)/100.0)
        return display

class RoundedType(Enum):
    BELOW = -1
    UP = 1