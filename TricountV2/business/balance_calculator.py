from TricountV2.business.activity import Activity
from TricountV2.MoneyLogic.rounded_type import RoundedType
from TricountV2.business.participant import Participant
from TricountV2.business.participation import Participation, ParticipationType

class BalanceCalculator:
    def __init__(self):
        self.activities = []
        self.participants = []
        
    def add_activity(self, name_activity, price, participants_name, payer):
        self.activities.append(Activity.create(name_activity, str(price), participants_name, payer))
        return self
      
    def calculate_participants_balance_from_activities(self):
        participants = []
        participations = self.__get_all_participations_from_activities()
        for participant_name in participations :
            all_participations_for_participant = participations[participant_name]
            participant = Participant.create(participant_name, "0", all_participations_for_participant, RoundedType.BELOW)
            balance = participant.get_balance()
            participant.balance = balance
            participants.append(participant)
        return participants
    
    def __get_all_participations_from_activities(self):
        participations = {}
        for activity in self.activities :
            for participant_name in activity.participants_name :
                if participant_name not in participations :
                    participations[participant_name] = []
                participation_type = ParticipationType.PAYER if participant_name == activity.payer else ParticipationType.FREELOADER
                participations[participant_name].append(Participation.create(activity.name, activity.price, len(activity.participants_name), participation_type))
        return participations