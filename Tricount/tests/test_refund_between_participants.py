from Tricount.MoneyLogic.rounded_type import RoundedType
from Tricount.business.participant import Participant
from Tricount.business.refund import Refund
from Tricount.business.refund_between_participants import RefundBetweenParticipants

def test_refund_when_payer_and_recipient_have_opposite_balance() : 
    (ParticipantDriver()
              .add_payer("Jean_-50.35")
              .add_participant_to_refund("Fantine_50.35")
              .calculate_refund_and_participants_updated()
              .valid_refund("Jean_Fantine_50.35")
              .valid_payer("Jean_0")
              .valid_recipient("Fantine_0"))
    
def test_refund_when_recipient_balance_is_more_important() : 
    (ParticipantDriver()
              .add_payer("Jean_-50.35")
              .add_participant_to_refund("Fantine_100.66")
              .calculate_refund_and_participants_updated()
              .valid_refund("Jean_Fantine_50.35")
              .valid_payer("Jean_0")
              .valid_recipient("Fantine_50.31"))
    
def test_refund_when_payer_balance_is_more_important() : 
    (ParticipantDriver()
              .add_payer("Jean_-157.17")
              .add_participant_to_refund("Fantine_100.66")
              .calculate_refund_and_participants_updated()
              .valid_refund("Jean_Fantine_100.66")
              .valid_payer("Jean_-56.51")
              .valid_recipient("Fantine_0"))

class ParticipantDriver(): 
    def __init__(self):
        self.payer = None
        self.recipient = None
        self.refund_between_participants = None

    def add_payer(self, participant_datas): 
        self.payer = self.__create_participant_from_datas(participant_datas)
        return self

    def add_participant_to_refund(self, participant_datas):
        self.recipient = self.__create_participant_from_datas(participant_datas)
        return self

    def __create_participant_from_datas(self, participant_datas):
        all_participant_datas = participant_datas.split("_")
        participant = Participant.create(all_participant_datas[0], all_participant_datas[1], None, RoundedType.BELOW)
        return participant        

    def calculate_refund_and_participants_updated(self):
        self.refund_between_participants = RefundBetweenParticipants(self.payer, self.recipient)
        self.refund_between_participants.calculate_refund_between_payer_and_recipient()
        return self

    def valid_refund(self, refund_expected_datas):
        refund_datas = refund_expected_datas.split("_")
        refund_expected = Refund.create_refund(refund_datas[0], refund_datas[1], refund_datas[2])
        refund_calculated = self.refund_between_participants.refund
        is_valid = refund_expected.payer == refund_calculated.payer and refund_expected.recipient == refund_calculated.recipient and refund_expected.amount == refund_calculated.amount
        assert(is_valid)
        return self

    def valid_payer(self, payer_expected):
        payer_expected_datas = payer_expected.split("_")
        payer_expected = Participant.create(payer_expected_datas[0], payer_expected_datas[1], None, RoundedType.BELOW)
        is_valid = payer_expected.name == self.refund_between_participants.payer.name and payer_expected.balance == self.refund_between_participants.payer.balance
        assert(is_valid)
        return self

    def valid_recipient(self, recipient_expected):
        recipient_expected_datas = recipient_expected.split("_")
        recipient_expected = Participant.create(recipient_expected_datas[0], recipient_expected_datas[1], None, RoundedType.BELOW)
        is_valid = recipient_expected.name == self.refund_between_participants.recipient.name and recipient_expected.balance == self.refund_between_participants.recipient.balance
        assert(is_valid)
        return self