from  decimal import Decimal

from TricountV2.MoneyLogic.Operation.last_result_needed import LastResultNeeded
from TricountV2.MoneyLogic.Operation.operation import Operation

class Substraction(Operation):
    def __init__(self, first_number, second_number, operand, last_result_needed):
        super().__init__(first_number, second_number, operand, last_result_needed)
        
    def calculate(self, last_result : Decimal):
        if self.last_result_needed == LastResultNeeded.NotNeeded : 
            last_result = Decimal(self.first_number) - Decimal(self.second_number) 
        elif self.last_result_needed == LastResultNeeded.SecondMember :
            last_result = Decimal(self.first_number) -  last_result
        elif self.last_result_needed == LastResultNeeded.FirstMember : 
            last_result = last_result - Decimal(self.second_number)
        return last_result