from TricountV2.MoneyLogic.rounded_type import RoundedType
from TricountV2.participant import Participant
from TricountV2.participation import Participation, ParticipationType


def test_1():
    participants = (ActivityDriver()
                    .add_activities("bar", 23.5, ["harry", "hermione"], "harry")
                    .get_participants_with_balance_calculated())

    assert(is_participant_are_equal(Participant.create_participant("harry", "11.75", [Participation.create("bar", 23.5, 2, ParticipationType.PAYER)], RoundedType.BELOW), participants[0])== True)
    assert(is_participant_are_equal(Participant.create_participant("hermione", "-11.75", [Participation.create("bar", 23.5, 2, ParticipationType.FREELOADER)], RoundedType.BELOW), participants[1]) == True)

# def test_2():
#     participants = (ActivityDriver()
#                     .add_activities("bar", 23.5, ["harry", "hermione"], "harry")
#                     .add_activities("restaurant", 50.7, ["harry", "hermione"], "hermione")
#                     .add_activities("bowling", 12, ["harry", "hermione"], "harry")
#                     .get_participants_with_balance_calculated())

#     harry_participations = [Participation.create("bar", 23.5, 2, ParticipationType.PAYER), Participation.create("restaurant", 50.7, 2, ParticipationType.FREELOADER), Participation.create("bowling", 12, 2, ParticipationType.PAYER)]
#     hermione_participations = [Participation.create("bar", 23.5, 2, ParticipationType.FREELOADER), Participation.create("restaurant", 50.7, 2, ParticipationType.PAYER), Participation.create("bowling", 12, 2, ParticipationType.FREELOADER)]
#     assert(is_participant_are_equal(Participant.create_participant("harry", "-7.6", harry_participations, RoundedType.BELOW), participants[0]) == True)
#     assert(is_participant_are_equal(Participant.create_participant("hermione", "7.6", hermione_participations, RoundedType.BELOW), participants[1]) == True)

# def test_3(): 
#     participants = (ActivityDriver()
#                     .add_activities("bar", 23.5, ["harry", "hermione"], "harry")
#                     .add_activities("restaurant", 50.7, ["hermione", "ron"], "hermione")
#                     .add_activities("bowling", 12, ["ron", "harry"], "ron")
#                     .get_participants_with_balance_calculated())

#     harry_participations = [Participation.create("bar", 23.5, 2, ParticipationType.PAYER), Participation.create("bowling", 12, 2, ParticipationType.FREELOADER)]
#     hermione_participations = [Participation.create("restaurant", 50.7, 2, ParticipationType.PAYER), Participation.create("bar", 23.5, 2, ParticipationType.FREELOADER)]
#     ron_participations = [Participation.create("restaurant", 50.7, 2, ParticipationType.FREELOADER), Participation.create("bowling", 12, 2, ParticipationType.PAYER)]
#     assert(is_participant_are_equal(Participant.create_participant("harry", 5.75, harry_participations, RoundedType.BELOW), participants[0]) == True)
#     assert(is_participant_are_equal(Participant.create_participant("hermione", 13.6, hermione_participations, RoundedType.BELOW), participants[1]) == True)
#     assert(is_participant_are_equal(Participant.create_participant("ron", -19.35, ron_participations, RoundedType.BELOW), participants[2]) == True)

# def test_4(): 
#     participants = (ActivityDriver()
#                     .add_activities("bar", 23.5, ["harry", "hermione", "ron"], "harry")
#                     .add_activities("restaurant", 50.7, ["hermione", "ron", "ginny", "hagrid"], "hermione")
#                     .add_activities("bowling", 12, ["ron", "ginny"], "ron")
#                     .add_activities("plane tickets", 1200, ["harry", "hermione", "ron", "ginny", "hagrid"], "ginny")
#                     .add_activities("hotel", 615, ["harry", "hermione", "ron", "ginny","hagrid"], "hagrid")
#                     .add_activities("spa day", 120, ["hermione", "ginny"], "hermione")
#                     .get_participants_with_balance_calculated())
#     harry_participations = [Participation.create( "bar", 23.5, 3, ParticipationType.PAYER), Participation.create("plane tickets", 1200, 5, ParticipationType.FREELOADER), Participation.create("hotel", 615, 5, ParticipationType.FREELOADER)]
#     hermione_participations = [Participation.create( "bar", 23.5, 3, ParticipationType.FREELOADER), Participation.create("restaurant", 50.7, 4, ParticipationType.PAYER), Participation.create("plane tickets", 1200, 5, ParticipationType.FREELOADER), Participation.create("hotel", 615, 5, ParticipationType.FREELOADER), Participation.create("spa day", 120, 2, ParticipationType.PAYER)]
#     ron_participations = [Participation.create("bar", 23.5, 3, ParticipationType.FREELOADER), Participation.create("restaurant", 50.7, 4, ParticipationType.FREELOADER), Participation.create("bowling", 12, 2, ParticipationType.PAYER), Participation.create("plane tickets", 1200, 5, ParticipationType.FREELOADER), Participation.create("hotel", 615, 5, ParticipationType.FREELOADER)]
#     ginny_participations = [Participation.create("restaurant", 50.7, 4, ParticipationType.FREELOADER), Participation.create("bowling", 12, 2, ParticipationType.FREELOADER), Participation.create("plane tickets", 1200, 5, ParticipationType.PAYER), Participation.create("hotel", 615, 5, ParticipationType.FREELOADER), Participation.create("spa day", 120, 2, ParticipationType.FREELOADER)]
#     hagrid_participations = [Participation.create("restaurant", 50.7, 4, ParticipationType.FREELOADER), Participation.create("plane tickets", 1200, 5, ParticipationType.FREELOADER), Participation.create("hotel", 615, 5, ParticipationType.PAYER)]
#     assert(is_participant_are_equal(Participant.create_participant("harry", -344.2, harry_participations, RoundedType.BELOW), participants[0]) == True)
#     assert(is_participant_are_equal(Participant.create_participant("hermione", -269.67, hermione_participations, RoundedType.BELOW), participants[1]) == True)
#     assert(is_participant_are_equal(Participant.create_participant("ron", -374.37, ron_participations, RoundedType.BELOW), participants[2]) == True)
#     assert(is_participant_are_equal(Participant.create_participant("ginny", 760.33, ginny_participations, RoundedType.BELOW), participants[3]) == True)
#     assert(is_participant_are_equal(Participant.create_participant("hagrid", 239.33, hagrid_participations, RoundedType.BELOW), participants[4]) == True)
        
#TODO
# - faire un test avec trois personnes et trois activités qui ne font pas la même chose OK 
# - faire un test avec six personnes et cinq activités qui ne font pas la même chose 
# - commiter 
# - externaliser le code 
# - commiter 
# - renommer les tests

def is_participant_are_equal(participant_expected : Participant, participant_calculated : Participant):
    is_participations_equal  = True
    for idx, _ in enumerate(participant_expected.participations):
        partipation_expected = participant_expected.participations[idx]
        partipation_calculated = participant_calculated.participations[idx]
        if partipation_expected.name != partipation_calculated.name or partipation_expected.price != partipation_calculated.price or partipation_expected.number_participants != partipation_calculated.number_participants or partipation_calculated.role != partipation_expected.role :
            is_participations_equal = False
            break        
    return participant_expected.name == participant_calculated.name and participant_expected.balance == participant_calculated.balance and is_participations_equal == True


class ActivityDriver :
    def __init__(self):
        self.activities = []
        self.participants = []

    def add_activities(self, name_activity, price, participants_name, payer):
        self.activities.append(Activity.create(name_activity, price, participants_name, payer))
        return self

    def get_participants_with_balance_calculated(self):
        participants = []
        participations = self.__get_all_participations_from_activities()
        for participant_name in participations :
            all_participations_for_participant = participations[participant_name]
            participant = Participant.create_participant(participant_name, 0, all_participations_for_participant, RoundedType.BELOW)
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

    def __get_participant_by_name(self, name):
        find_participant = None
        for participant in self.participants :
            if participant.name == name :
                find_participant = participant
                break
        return find_participant


class Activity :
    def __init__(self, name, price, participants_name, payer):
        self.name = name
        self.price = price
        self.participants_name = participants_name
        self.payer = payer

    @staticmethod
    def create(name, price, participants_name, payer):
        return Activity(name, price, participants_name, payer)