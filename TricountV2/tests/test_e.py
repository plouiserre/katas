from __future__ import annotations
from dataclasses import dataclass
from TricountV2.MoneyLogic.Operation.last_result_needed import LastResultNeeded
from TricountV2.MoneyLogic.rounded_type import RoundedType
from TricountV2.MoneyLogic.money import Money
from TricountV2.participant import Participant

def test_1() : 
    refund_between_participants_calculated =(ParticipantDriver()
              .add_payer(Participant.create_participant("Jean", "-50.35", None, RoundedType.BELOW))
              .add_participant_to_refund(Participant.create_participant("Fantine", "50.35", None, RoundedType.BELOW))
              .get_refund_and_participants_updated())
    refund_expected = Refund.create_refund("Jean", "Fantine", "50.35")
    refund_between_participants_expected = RefundBetweenParticipants.create(refund_expected, Participant.create_participant("Jean", "0", None, RoundedType.BELOW), Participant.create_participant("Fantine", "0", None, RoundedType.BELOW))
    assert(compare_refund(refund_between_participants_expected, refund_between_participants_calculated))  

def test_2() : 
    refund_between_participants_calculated =(ParticipantDriver()
              .add_payer(Participant.create_participant("Jean", "-50.35", None, RoundedType.BELOW))
              .add_participant_to_refund(Participant.create_participant("Fantine", "100.66", None, RoundedType.BELOW))
              .get_refund_and_participants_updated())
    refund_expected = Refund.create_refund("Jean", "Fantine", "50.35")
    refund_between_participants_expected = RefundBetweenParticipants.create(refund_expected, Participant.create_participant("Jean", "0", None, RoundedType.BELOW), Participant.create_participant("Fantine", "50.31", None, RoundedType.BELOW))
    assert(compare_refund(refund_between_participants_expected, refund_between_participants_calculated))  

def test_3() : 
    refund_between_participants_calculated =(ParticipantDriver()
              .add_payer(Participant.create_participant("Jean", "-157.17", None, RoundedType.BELOW))
              .add_participant_to_refund(Participant.create_participant("Fantine", "100.66", None, RoundedType.BELOW))
              .get_refund_and_participants_updated())
    refund_expected = Refund.create_refund("Jean", "Fantine", "100.66")
    refund_between_participants_expected = RefundBetweenParticipants.create(refund_expected, Participant.create_participant("Jean", "-56.51", None, RoundedType.BELOW), Participant.create_participant("Fantine", "0", None, RoundedType.BELOW))
    assert(compare_refund(refund_between_participants_expected, refund_between_participants_calculated))  

def compare_refund(refund_between_participants_expected : RefundBetweenParticipants, refund_between_participants_calculated : RefundBetweenParticipants):
    refund_expected = refund_between_participants_expected.refund
    refund_calculated = refund_between_participants_calculated.refund
    payer_expected = refund_between_participants_expected.payer
    payer_calculated = refund_between_participants_calculated.payer
    recipiant_expected = refund_between_participants_expected.recipient
    recipiant_calculated = refund_between_participants_calculated.recipient
    is_equal_refund = refund_expected.amount == refund_calculated.amount and refund_expected.recipient == refund_calculated.recipient and refund_expected.payer == refund_calculated.payer
    is_equal_payer = payer_expected.name == payer_calculated.name and payer_expected.balance == payer_calculated.balance
    is_equal_recipiant = recipiant_expected.name == recipiant_calculated.name and recipiant_calculated.balance == recipiant_expected.balance
    return is_equal_refund and  is_equal_payer and is_equal_recipiant

# TODO faire : 
# 1 - payer.balance = refund.balance  DID 
# 2 - payer.balance < refund.balance  DID
# 3 - payer.balance > refund.balance 
# 4 - Decimal
# 5 - externaliser code 
# 6 - cleaner test
# 7 - commit
# 8 - merge

class ParticipantDriver(): 
    def __init__(self):
        self.payer = None
        self.recipient = None

    def add_payer(self, participant : Participant): 
        self.payer = participant
        return self

    def add_participant_to_refund(self, participant : Participant):
        self.recipient = participant
        return self

    #TODO try with decimal 
    def get_refund_and_participants_updated(self):
        refund = None
        balance_payer = self.payer.balance.replace("-", "")
        money = Money(RoundedType.BELOW)
        if balance_payer == self.recipient.balance : 
            refund = Refund.create_refund(self.payer.name, self.recipient.name, balance_payer)
            self.payer.balance = "0"
            self.recipient.balance = "0"
        elif float(balance_payer) < float(self.recipient.balance) : 
            refund = Refund.create_refund(self.payer.name, self.recipient.name, balance_payer)
            money.substract_two_money(self.recipient.balance, balance_payer, LastResultNeeded.NotNeeded)
            self.payer.balance = "0"
            self.recipient.balance = money.display_final_result()
        elif float(balance_payer) > float(self.recipient.balance) : 
            refund = Refund.create_refund(self.payer.name, self.recipient.name, self.recipient.balance)
            money.substract_two_money(balance_payer, self.recipient.balance, LastResultNeeded.NotNeeded)
            self.recipient.balance = "0"
            self.payer.balance = "-"+money.display_final_result()
        return RefundBetweenParticipants.create(refund, self.payer, self.recipient)

@dataclass
class RefundBetweenParticipants :
    refund : Refund
    payer : Participant 
    recipient : Participant

    @staticmethod
    def create(refund, payer, recipient):
        return RefundBetweenParticipants(refund, payer, recipient)

@dataclass(frozen=True)
class Refund : 
    payer : str
    recipient : str
    amount :str
    
    @staticmethod
    def create_refund(payer : str, recipient : str, amount : str):
        return Refund(payer, recipient, amount)

    