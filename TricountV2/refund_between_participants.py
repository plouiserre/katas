from decimal import Decimal
from TricountV2.MoneyLogic.Operation.last_result_needed import LastResultNeeded
from TricountV2.MoneyLogic.rounded_type import RoundedType
from TricountV2.MoneyLogic.money import Money
from TricountV2.participant import Participant
from TricountV2.refund import Refund

class RefundBetweenParticipants :
    def __init__(self, payer : Participant, recipient : Participant):
        self.refund = None
        self.payer = payer 
        self.recipient = recipient

    def calculate_refund_between_payer_and_recipient(self):
        balance_payer = Decimal(self.payer.balance.replace("-", ""))
        balance_recipient = Decimal(self.recipient.balance)
        money = Money(RoundedType.BELOW)
        if balance_payer == balance_recipient : 
            self.refund = Refund.create_refund(self.payer.name, self.recipient.name, str(balance_payer))
            self.payer.balance = "0"
            self.recipient.balance = "0"
        elif balance_payer < balance_recipient : 
            self.refund = Refund.create_refund(self.payer.name, self.recipient.name, str(balance_payer))
            money.substract_two_money(balance_recipient, balance_payer, LastResultNeeded.NotNeeded)
            self.payer.balance = "0"
            self.recipient.balance = money.display_final_result()
        elif float(balance_payer) > float(self.recipient.balance) : 
            self.refund = Refund.create_refund(self.payer.name, self.recipient.name, str(balance_recipient))
            money.substract_two_money(balance_payer, balance_recipient, LastResultNeeded.NotNeeded)
            self.recipient.balance = "0"
            self.payer.balance = "-"+money.display_final_result()

    @staticmethod
    def create(refund, payer, recipient):
        refund_between_participants =  RefundBetweenParticipants(payer, recipient)
        refund_between_participants.refund = refund
        return refund_between_participants