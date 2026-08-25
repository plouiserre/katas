from __future__ import annotations
from dataclasses import dataclass
from TricountV2.MoneyLogic.rounded_type import RoundedType
from TricountV2.participant import Participant 
from TricountV2.participation import Participation, ParticipationType
from TricountV2.refund_between_participants import RefundBetweenParticipants

def test_1():
    refunds_calculated = (RefundDriver()
               .add_participant(Participant.create("harry", "11.75", [Participation.create("bar", 23.5, 2, ParticipationType.PAYER)], RoundedType.BELOW))
               .add_participant(Participant.create("hermione", "-11.75", [Participation.create("bar", 23.5, 2, ParticipationType.FREELOADER)], RoundedType.BELOW))
               .get_refunds())
    refunds_expected = [Refund.create_refund("hermione", "harry", "11.75")]
    assert(len(refunds_calculated) == 1)
    assert(compare_all_refunds(refunds_expected, refunds_calculated))  
    
def test_2():
    harry_participations = [Participation.create("bar", "23.5", 2, ParticipationType.PAYER), Participation.create("bowling", "12", 2, ParticipationType.FREELOADER)]
    hermione_participations = [Participation.create("bar", "23.5", 2, ParticipationType.FREELOADER), Participation.create("restaurant", "50.7", 2, ParticipationType.PAYER)]
    ron_participations = [Participation.create("restaurant", "50.7", 2, ParticipationType.FREELOADER), Participation.create("bowling", "12", 2, ParticipationType.PAYER)]
    refunds_calculated = (RefundDriver()
                        .add_participant(Participant.create("harry", "5.75", harry_participations, RoundedType.BELOW))
                        .add_participant(Participant.create("hermione", "13.6", hermione_participations, RoundedType.BELOW))
                        .add_participant(Participant.create("ron", "-19.35", ron_participations, RoundedType.BELOW))
                        .get_refunds())
    refunds_expected = [Refund.create_refund("ron", "hermione", "13.6"), Refund.create_refund("ron", "harry", "5.75")]
    assert(len(refunds_calculated) == 2)
    assert(compare_all_refunds(refunds_expected, refunds_calculated))  
    
    
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
    
    #TODO reprendre ce code et l'améliorer
    def get_refunds(self):
        payer_participants = self.__get_payer_participants()
        recipient_participants = self.__get_recipient_participants()
        all_refunds = []
        while (len(payer_participants)>0 and len(recipient_participants)>0):
            first_payer = payer_participants[0]
            first_recipient = recipient_participants[0]
            refund_between_participants = RefundBetweenParticipants(first_payer, first_recipient)
            refund = refund_between_participants.calculate_refund_between_payer_and_recipient()
            if first_payer.balance == "0": 
                payer_participants.remove(first_payer)
            if first_recipient.balance == "0" : 
                recipient_participants.remove(first_recipient)
            all_refunds.append(refund)
        return all_refunds
    
    def __get_payer_participants(self): 
        payer_participants = []
        for participant in self.participants : 
            balance_participant = float(participant.balance)
            if balance_participant < 0 : 
                payer_participants.append(participant)
        return sorted(payer_participants, key =lambda x:x.balance)
    
    def __get_recipient_participants(self): 
            recipient_participants = []
            for participant in self.participants : 
                balance_participant = float(participant.balance)
                if balance_participant > 0 : 
                    recipient_participants.append(participant)
            return sorted(recipient_participants, key =lambda x:x.balance)
                
    #  self.debt_participants = sorted(self.debt_participants, key=lambda x:x.balance)
    #  self.generous_participants = sorted(self.generous_participants, key=lambda x:x.balance, reverse= True )
                       
    
@dataclass(frozen=True)
class Refund : 
    payer : str
    recipient : str
    amount :str
    
    @staticmethod
    def create_refund(payer : str, recipient : str, amount : str):
        return Refund(payer, recipient, amount)
