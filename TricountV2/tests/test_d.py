from __future__ import annotations
from dataclasses import dataclass
from TricountV2.MoneyLogic.rounded_type import RoundedType
from TricountV2.participant import Participant 
from TricountV2.participation import Participation, ParticipationType


def test_1():
    refunds_calculated = (RefundDriver()
               .add_participant(Participant.create("harry", "11.75", [Participation.create("bar", 23.5, 2, ParticipationType.PAYER)], RoundedType.BELOW))
               .add_participant(Participant.create("hermione", "-11.75", [Participation.create("bar", 23.5, 2, ParticipationType.FREELOADER)], RoundedType.BELOW))
               .get_refunds())
    refunds_expected = [Refund.create_refund("hermione", "harry", "11.75")]
    assert(len(refunds_calculated) == 1)
    assert(compare_all_refunds(refunds_expected, refunds_calculated))  
    
# def test_2():
#     harry_participations = [Participation.create("bar", "23.5", 2, ParticipationType.PAYER), Participation.create("bowling", "12", 2, ParticipationType.FREELOADER)]
#     hermione_participations = [Participation.create("bar", "23.5", 2, ParticipationType.FREELOADER), Participation.create("restaurant", "50.7", 2, ParticipationType.PAYER)]
#     ron_participations = [Participation.create("restaurant", "50.7", 2, ParticipationType.FREELOADER), Participation.create("bowling", "12", 2, ParticipationType.PAYER)]
#     refunds_calculated = (RefundDriver()
#                         .add_participant(Participant.create("harry", "5.75", harry_participations, RoundedType.BELOW))
#                         .add_participant(Participant.create("hermione", "13.6", hermione_participations, RoundedType.BELOW))
#                         .add_participant(Participant.create("ron", "-19.35", ron_participations, RoundedType.BELOW))
#                         .get_refunds())
#     refunds_expected = [Refund.create_refund("ron", "hermione", "13.6"), Refund.create_refund("ron", "harry", "5.75")]
#     assert(len(refunds_calculated) == 2)
#     assert(compare_all_refunds(refunds_expected, refunds_calculated))  
    
    
def compare_all_refunds(refunds_expected : Refund, refunds_calculated : Refund):
    is_equal = True
    for idx, _ in enumerate(refunds_expected): 
        refund_expected = refunds_expected[idx]
        refund_calculated = refunds_calculated[idx]
        is_equal = refund_expected.amount == refund_calculated.amount and refund_expected.recipient == refund_calculated.recipient and refund_expected.payer == refund_calculated.payer
        if is_equal == False : 
            break
    return is_equal 
    
class RefundDriver : 
    def __init__(self):
        self.participants = []
    
    def add_participant(self, participant : Participant) :
        self.participants.append(participant)
        return self
    
    def get_refunds(self):
        participant_negative_balance = None 
        for participant in self.participants : 
            balance = float(participant.balance)
            if balance < 0 : 
                participant_negative_balance = participant
                break
        self.participants.remove(participant_negative_balance)
        refunds = []
        refunds.append(Refund(participant_negative_balance.name, self.participants[0].name, self.participants[0].balance))
        return refunds
    
@dataclass(frozen=True)
class Refund : 
    payer : str
    recipient : str
    amount :str
    
    @staticmethod
    def create_refund(payer : str, recipient : str, amount : str):
        return Refund(payer, recipient, amount)
