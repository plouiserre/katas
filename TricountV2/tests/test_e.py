from __future__ import annotations
from dataclasses import dataclass
from TricountV2.MoneyLogic.Operation.last_result_needed import LastResultNeeded
from TricountV2.MoneyLogic.rounded_type import RoundedType
from TricountV2.MoneyLogic.money import Money
from TricountV2.participant import Participant

def test_1() : 
    refund_calculated =(ParticipantDriver()
              .add_payer(Participant.create_participant("Jean", "-50.35", None, RoundedType.BELOW))
              .add_participant_to_refund(Participant.create_participant("Fantine", "50.35", None, RoundedType.BELOW))
              .get_refund())
    refund_expected = Refund.create_refund("Jean", "Fantine", "50.35")
    assert(compare_refund(refund_expected, refund_calculated))  

def compare_refund(refund_expected : Refund, refund_calculated : Refund):
    is_equal = refund_expected.amount == refund_calculated.amount and refund_expected.recipient == refund_calculated.recipient and refund_expected.payer == refund_calculated.payer
    return is_equal 

# TODO faire : 
# 1 - payer.balance = refund.balance OK 
# 2 - payer.balance < refund.balance 
# 3 - payer.balance > refund.balance 
# 4 - externaliser code 
# 5 - cleaner test
# 6 - commit
# 7 - merge

class ParticipantDriver(): 
    def __init__(self):
        self.payer = None
        self.participant_to_refund = None

    def add_payer(self, participant : Participant): 
        self.payer = participant
        return self

    def add_participant_to_refund(self, participant : Participant):
        self.participant_to_refund = participant
        return self

    def get_refund(self):
        balance_payer = self.payer.balance.replace("-", "")
        return Refund.create_refund(self.payer.name, self.participant_to_refund.name, balance_payer)

@dataclass(frozen=True)
class Refund : 
    payer : str
    recipient : str
    amount :str
    
    @staticmethod
    def create_refund(payer : str, recipient : str, amount : str):
        return Refund(payer, recipient, amount)

    