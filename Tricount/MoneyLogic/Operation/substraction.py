from  decimal import Decimal

from Tricount.MoneyLogic.Operation.operation import Operation

class Substraction(Operation):
    def __init__(self, first_number, second_number, operand, is_last_result_needed):
        super().__init__(first_number, second_number, operand, is_last_result_needed)
        
    def calculate(self, last_result : Decimal):
        if self.is_last_result_needed == False : 
            last_result = Decimal(self.first_number) - Decimal(self.second_number) 
        else : 
            last_result = last_result - Decimal(self.second_number)
        return last_result