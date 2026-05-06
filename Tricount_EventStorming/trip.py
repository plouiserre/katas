import copy
from Tricount_EventStorming.participant import CREDITOR, DEBTOR, Participant
from Tricount_EventStorming.refund import Refund

class Trip : 
    def __init__(self):
        self.participants = []
        self.debt_participants = []
        self.generous_participants = []
        self.refunds = []

    def add_activity(self, activity):
        self.__update_participants_activity(activity)
        self.__calculate_refunds_from_trip()

    def __get_participant(self, name): 
        for participant in self.participants : 
            if participant.name == name : 
                return participant
        return None
    
    def __update_participants_activity(self, activity):
        price_by_participant = round(activity.price / len(activity.participants), 2)
        participant_paymaster = self.__get_participant(activity.paymaster)
        if participant_paymaster == None : 
            self.participants.append(Participant(activity.paymaster, activity.price, CREDITOR))
        else : 
            participant_paymaster.add_activity_you_paid(activity)
        for participant_name in activity.participants : 
            participant_activity = self.__get_participant(participant_name)
            if participant_activity == None : 
                self.participants.append(Participant(participant_name, - price_by_participant, DEBTOR))
            else :
                participant_activity.add_activity_you_participe(activity)

    def __calculate_refunds_from_trip(self):
        self.refunds = []        
        self.__sorted_friends()
        for debt_participant in self.debt_participants :
            refunds = debt_participant.paid_generous_friends(self.generous_participants)
            for refund in refunds : 
                self.refunds.append(refund)
    
    def __sorted_friends(self): 
        self.debt_participants = []
        self.generous_participants = []        
        all_participants = copy.deepcopy(self.participants)
        for participant in all_participants : 
            if participant.balance < 0 : 
                self.debt_participants.append(participant)
            else : 
                self.generous_participants.append(participant)
        self.debt_participants = sorted(self.debt_participants, key=lambda x:x.balance)
        self.generous_participants = sorted(self.generous_participants, key=lambda x:x.balance, reverse= True )
        