from decimal import Decimal
from Tricount.MoneyLogic.Operation.last_result_needed import LastResultNeeded
from Tricount.MoneyLogic.rounded_type import RoundedType
from Tricount.MoneyLogic.money import Money
from Tricount.business.participant import Participant
from Tricount.business.refund import Refund

class RefundBetweenParticipants :
    def __init__(self, payer : Participant, recipient : Participant):
        self.refund = None
        self.payer = payer 
        self.recipient = recipient

    #TODO reprendre ce test car on renvoie le refund
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
        return self.refund

    @staticmethod
    def create(refund, payer, recipient):
        refund_between_participants =  RefundBetweenParticipants(payer, recipient)
        refund_between_participants.refund = refund
        return refund_between_participants