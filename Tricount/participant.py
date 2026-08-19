from Tricount.MoneyLogic.money import Money
from Tricount.MoneyLogic.Operation.last_result_needed import LastResultNeeded
from Tricount.MoneyLogic.rounded_type import RoundedType
from Tricount.refund import Refund
DEBTOR = 0
CREDITOR = 1

class Participant : 
    def __init__(self,name, balance, participant_type):
        self.name = name 
        self.balance = balance
        self.participant_type = participant_type

    def __eq__(self, other):
        if other == None : 
            return False
        return self.name == other.name and self.balance == other.balance    
    
    def add_activity_you_paid(self, activity): 
        self.balance = round(self.balance + activity.price, 2)
        if self.balance > 0 : 
            self.participant_type = CREDITOR

    def add_activity_you_participe(self, activity):
        money_activity = Money(RoundedType.BELOW)
        money_activity.divide_two_money(str(activity.price), str(len(activity.participants)), LastResultNeeded.NotNeeded)
        money_activity.substract_two_money(str(self.balance), None, LastResultNeeded.SecondMember)
        balance_str = money_activity.display_final_result()
        self.balance = float(balance_str)
        
        if self.balance < 0 : 
            self.participant_type = DEBTOR

    def paid_generous_friends(self, generous_participants) : 
        refunds = []
        idx = 0
        while self.balance < -0.03 and idx < 20: 
            value_to_refund = round(0 - self.balance, 2)
            for generous_participant in generous_participants : 
                if value_to_refund == 0 : 
                    break
                if generous_participant.balance == 0 :
                    continue
                if value_to_refund > generous_participant.balance : 
                    value_to_refund = generous_participant.balance 
                refunds.append(Refund(self.name, generous_participant.name, value_to_refund))
                generous_participant.balance = round(generous_participant.balance - value_to_refund, 2)
                self.balance = round(self.balance + value_to_refund, 2)
                value_to_refund = round(0 - self.balance, 2)
        idx += 1
        return refunds