from dataclasses import dataclass
from Tricount.MoneyLogic.operand import Operand

@dataclass
class Operation(): 
    first_number : str
    second_number : str
    operand : Operand
    is_last_result_needed : bool