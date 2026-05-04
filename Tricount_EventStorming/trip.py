from Tricount_EventStorming.participant import CREDITOR, DEBTOR, Participant

class Trip : 
    def __init__(self):
        self.participants = []

    def add_activity(self, activity):
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

    def __get_participant(self, name): 
        for participant in self.participants : 
            if participant.name == name : 
                return participant
        return None