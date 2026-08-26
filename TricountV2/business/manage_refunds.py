from TricountV2.business.participant import Participant 
from TricountV2.business.refund_between_participants import RefundBetweenParticipants

class ManageRefunds : 
    def __init__(self):
        self.participants = []
        
    def add_participant(self, participant : Participant) :
        self.participants.append(participant)
    
    def calculate_all_refunds(self):
        payer_participants = self.__get_payer_participants()
        recipient_participants = self.__get_recipient_participants()
        all_refunds = []
        while (len(payer_participants)>0 and len(recipient_participants)>0):
            refund = self.__manage_refund_between_payer_and_recipiant(payer_participants, recipient_participants)
            all_refunds.append(refund)
        return all_refunds
    
    def __manage_refund_between_payer_and_recipiant(self, payer_participants, recipient_participants):
        first_payer = payer_participants[0]
        first_recipient = recipient_participants[0]
        refund_between_participants = RefundBetweenParticipants(first_payer, first_recipient)
        refund = refund_between_participants.calculate_refund_between_payer_and_recipient()
        if first_payer.balance == "0": 
            payer_participants.remove(first_payer)
        if first_recipient.balance == "0" : 
            recipient_participants.remove(first_recipient)
        return refund
    
    def __get_payer_participants(self): 
        payer_participants = []
        for participant in self.participants : 
            balance_participant = float(participant.balance)
            if balance_participant < 0 : 
                payer_participants.append(participant)
        participants_sorted =  sorted(payer_participants, key =lambda x:float(x.balance))
        return participants_sorted
    
    def __get_recipient_participants(self): 
            recipient_participants = []
            for participant in self.participants : 
                balance_participant = float(participant.balance)
                if balance_participant > 0 : 
                    recipient_participants.append(participant)
            participants_sorted =  sorted(recipient_participants, key =lambda x:float(x.balance), reverse= True)
            return participants_sorted