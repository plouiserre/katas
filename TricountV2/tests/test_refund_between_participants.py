from TricountV2.MoneyLogic.rounded_type import RoundedType
from TricountV2.participant import Participant
from TricountV2.refund import Refund
from TricountV2.refund_between_participants import RefundBetweenParticipants

def test_refund_when_payer_and_recipient_have_opposite_balance() : 
    refund_between_participants_calculated =(ParticipantDriver()
              .add_payer(Participant.create("Jean", "-50.35", None, RoundedType.BELOW))
              .add_participant_to_refund(Participant.create("Fantine", "50.35", None, RoundedType.BELOW))
              .get_refund_and_participants_updated())
    refund_expected = Refund.create_refund("Jean", "Fantine", "50.35")
    refund_between_participants_expected = RefundBetweenParticipants.create(refund_expected, Participant.create("Jean", "0", None, RoundedType.BELOW), Participant.create("Fantine", "0", None, RoundedType.BELOW))
    assert(compare_refund(refund_between_participants_expected, refund_between_participants_calculated))  

def test_refund_when_recipient_balance_is_more_important() : 
    refund_between_participants_calculated =(ParticipantDriver()
              .add_payer(Participant.create("Jean", "-50.35", None, RoundedType.BELOW))
              .add_participant_to_refund(Participant.create("Fantine", "100.66", None, RoundedType.BELOW))
              .get_refund_and_participants_updated())
    refund_expected = Refund.create_refund("Jean", "Fantine", "50.35")
    refund_between_participants_expected = RefundBetweenParticipants.create(refund_expected, Participant.create("Jean", "0", None, RoundedType.BELOW), Participant.create("Fantine", "50.31", None, RoundedType.BELOW))
    assert(compare_refund(refund_between_participants_expected, refund_between_participants_calculated))  

def test_refund_when_payer_balance_is_more_important() : 
    refund_between_participants_calculated =(ParticipantDriver()
              .add_payer(Participant.create("Jean", "-157.17", None, RoundedType.BELOW))
              .add_participant_to_refund(Participant.create("Fantine", "100.66", None, RoundedType.BELOW))
              .get_refund_and_participants_updated())
    refund_expected = Refund.create_refund("Jean", "Fantine", "100.66")
    refund_between_participants_expected = RefundBetweenParticipants.create(refund_expected, Participant.create("Jean", "-56.51", None, RoundedType.BELOW), Participant.create("Fantine", "0", None, RoundedType.BELOW))
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

    def get_refund_and_participants_updated(self):
        refund_between_participants = RefundBetweenParticipants(self.payer, self.recipient)
        refund_between_participants.calculate_refund_between_payer_and_recipient()
        return refund_between_participants

