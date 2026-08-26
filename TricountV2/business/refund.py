from dataclasses import dataclass
@dataclass(frozen=True)
class Refund : 
    payer : str
    recipient : str
    amount :str
    
    @staticmethod
    def create_refund(payer : str, recipient : str, amount : str):
        return Refund(payer, recipient, amount)    