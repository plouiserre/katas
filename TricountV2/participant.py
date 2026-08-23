from TricountV2.participation import Participation, ParticipationType
from TricountV2.MoneyLogic.money import Money

from decimal import Decimal

class Participant : 
    def __init__(self, name, rounded_type):
        self.name = name
        self.participations = []
        self.balance = 0
        self.money = Money(rounded_type)

    @staticmethod
    def create_participant(name, balance, participations, rounded_type): 
        participant = Participant(name, rounded_type)
        participant.balance = balance
        participant.participations = participations
        return participant

    def add_participation(self, name, price, number_participants, role):
        self.participations.append(Participation.create(name, str(price), number_participants, role))
        return self
        
    def get_balance(self):
        balance_decimal = Decimal(0)
        for participation in self.participations :
            if participation.role == ParticipationType.PAYER :  
                participation.calculate_balance_payer_participation(self.money)
                balance_decimal += self.money.calculate_all_op_with_not_display()
            elif participation.role == ParticipationType.FREELOADER : 
                participation.calculate_balance_freeloader_participation(self.money)
                balance_decimal -= self.money.calculate_all_op_with_not_display()
        self.balance = self.money.display_final_result_from_all_operations(balance_decimal)
        return self.balance