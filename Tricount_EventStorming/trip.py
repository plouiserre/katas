from Tricount_EventStorming.participant import Participant

class Trip : 
    def __init__(self):
        self.participants = []

    def add_activity(self, activity):
        price_by_participant = round(activity.price / len(activity.participants), 2)
        participant_paymaster = self.__get_participant(activity.paymaster)
        if participant_paymaster == None : 
            self.participants.append(Participant(activity.paymaster, activity.price))
        else : 
            participant_paymaster.balance = round(participant_paymaster.balance + activity.price, 2)
        for participant_name in activity.participants : 
            participant_activity = self.__get_participant(participant_name)
            if participant_activity == None : 
                self.participants.append(Participant(participant_name, - price_by_participant))
            else :
                participant_activity.balance = round(participant_activity.balance - price_by_participant, 2)

    def __get_participant(self, name): 
        for participant in self.participants : 
            if participant.name == name : 
                return participant
        return None