import pytest

from TricountV2.MoneyLogic.cannot_divide_by_zero_exception import CannotDivideByZeroException
from TricountV2.MoneyLogic.money import Money
from TricountV2.MoneyLogic.Operation.last_result_needed import LastResultNeeded
from TricountV2.MoneyLogic.rounded_type import RoundedType

def test_add_two_moneys(): 
    final_money = (MoneyDriver(RoundedType.BELOW)
             .add("5.3", "6.5", LastResultNeeded.NotNeeded)
             .display_final_result())

    assert("11.8" == final_money)

def test_substract_two_moneys(): 
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .substract("11.9", "4.3", LastResultNeeded.NotNeeded)
                   .display_final_result())

    assert("7.6" == final_money)

def test_multiply_two_moneys(): 
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .multiply("33.4", "0.2", LastResultNeeded.NotNeeded)
                   .display_final_result())
    assert("6.68" == final_money)

def test_multiply_two_moneys_with_round_below(): 
    final_money = (MoneyDriver(RoundedType.BELOW)
                       .multiply("33.4", "0.21", LastResultNeeded.NotNeeded)
                       .display_final_result())
    assert("7.01" == final_money)

def test_multiply_two_moneys_with_round_up(): 
    final_money = (MoneyDriver(RoundedType.UP)
                       .multiply("33.4", "0.21", LastResultNeeded.NotNeeded)
                       .display_final_result())
    assert("7.02" == final_money)

def test_divide_two_moneys(): 
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .divide("8", "2.5", LastResultNeeded.NotNeeded)
                   .display_final_result())
    assert("3.2" == final_money)

def test_divide_two_moneys_with_round_below(): 
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .divide("20", "2.54", LastResultNeeded.NotNeeded)
                   .display_final_result())
    assert("7.87" == final_money)

def test_divide_two_moneys_with_round_up(): 
    final_money = (MoneyDriver(RoundedType.UP)
                   .divide("20", "2.54", LastResultNeeded.NotNeeded)
                   .display_final_result())
    assert("7.88" == final_money)
    
def test_multiple_operande_with_many_moneys_with_round_below_negative():
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .add("9.87", "2.32", LastResultNeeded.NotNeeded)
                   .substract(None, "43.23", LastResultNeeded.FirstMember)
                   .multiply(None, "93.23", LastResultNeeded.FirstMember)
                   .divide(None, "7.3", LastResultNeeded.FirstMember)
                   .display_final_result())
    assert("-396.42" == final_money)

def test_multiple_operande_with_many_moneys_with_round_up_negative():
    final_money = (MoneyDriver(RoundedType.UP)
                   .add("9.87", "2.32", LastResultNeeded.NotNeeded)
                   .substract(None, "43.23", LastResultNeeded.FirstMember)
                   .multiply(None, "93.23", LastResultNeeded.FirstMember)
                   .divide(None, "7.3", LastResultNeeded.FirstMember)
                   .display_final_result())
    assert("-396.41" == final_money)
    
def test_multiple_operande_with_many_moneys_with_round_below():
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .add("9.87", "2.32", LastResultNeeded.NotNeeded)
                   .substract(None, "3.23", LastResultNeeded.FirstMember)
                   .multiply(None, "93.23", LastResultNeeded.FirstMember)
                   .divide(None, "7.3", LastResultNeeded.FirstMember)
                   .display_final_result())
    assert("114.43" == final_money)

def test_multiple_operande_with_many_moneys_with_round_up():
    final_money = (MoneyDriver(RoundedType.UP)
                   .add("9.87", "2.32", LastResultNeeded.NotNeeded)
                   .substract(None, "3.23", LastResultNeeded.FirstMember)
                   .multiply(None, "93.23", LastResultNeeded.FirstMember)
                   .divide(None, "7.3", LastResultNeeded.FirstMember)
                   .display_final_result())
    assert("114.44" == final_money)
    
def test_last_result_second_member_add():
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .multiply("3.2", "9.54", LastResultNeeded.NotNeeded)
                   .add("32.92", None, LastResultNeeded.SecondMember)
                   .display_final_result())
    assert("63.44" == final_money)
    
def test_last_result_second_member_substract():
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .multiply("3.2", "9.54", LastResultNeeded.NotNeeded)
                   .substract("32.92", None, LastResultNeeded.SecondMember)
                   .display_final_result())
    assert("2.39" == final_money)
    
def test_last_result_second_member_multiply():
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .multiply("3.2", "9.54", LastResultNeeded.NotNeeded)
                   .multiply("3.3", None, LastResultNeeded.SecondMember)
                   .display_final_result())
    assert("100.74" == final_money)
    
def test_last_result_second_member_division():
    final_money = (MoneyDriver(RoundedType.BELOW)
                   .multiply("3.2", "9.54", LastResultNeeded.NotNeeded)
                   .divide("100", None, LastResultNeeded.SecondMember)
                   .display_final_result())
    assert("3.27" == final_money)
    
def test_5():
    final_money = (MoneyDriver(RoundedType.UP)
                    .add("9.87", "2.32", LastResultNeeded.NotNeeded)
                    .substract("16.4", None , LastResultNeeded.SecondMember)
                    .multiply(None, "93.23", LastResultNeeded.FirstMember)
                    .divide("1000", None, LastResultNeeded.SecondMember)
                    .display_final_result())
    assert("2.55" == final_money)
    
def test_6():
    final_money = (MoneyDriver(RoundedType.UP)
                    .add("9.87", "2.32", LastResultNeeded.NotNeeded)
                    .substract(None, "16.4" , LastResultNeeded.FirstMember)
                    .multiply(None, "93.23", LastResultNeeded.FirstMember)
                    .divide("1000", None, LastResultNeeded.SecondMember)
                    .display_final_result())
    assert("-2.54" == final_money)

def test_divide_one_money_by_0():
    with pytest.raises(CannotDivideByZeroException) :
        (MoneyDriver(RoundedType.BELOW)
                   .divide("89.2", "0", LastResultNeeded.NotNeeded))
        
def test_add_two_money_and_divide_one_money_by_0():
    with pytest.raises(CannotDivideByZeroException) :
        (MoneyDriver(RoundedType.UP)
                   .add("93", "2", LastResultNeeded.NotNeeded)
                   .divide(None, "0", LastResultNeeded.FirstMember))

class MoneyDriver : 
    def __init__(self, rounded_type):
        self.money = Money(rounded_type)

    def add(self, first_number_str : str, second_number_str : str, last_result_needed : LastResultNeeded): 
        self.money.add_two_money(first_number_str, second_number_str, last_result_needed)
        return self

    def substract(self, first_number_str : str, second_number_str : str, last_result_needed : LastResultNeeded): 
        self.money.substract_two_money(first_number_str, second_number_str, last_result_needed)
        return self

    def multiply(self, first_number_str : str, second_number_str : str, last_result_needed : LastResultNeeded): 
        self.money.multiply_two_money(first_number_str, second_number_str, last_result_needed)
        return self

    def divide(self, first_number_str : str, second_number_str : str, last_result_needed : LastResultNeeded):
        self.money.divide_two_money(first_number_str, second_number_str, last_result_needed)
        return self

    def display_final_result(self): 
        display = self.money.display_final_result()
        return display