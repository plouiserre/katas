from Tricount.business.balance_calculator import BalanceCalculator
from Tricount.MoneyLogic.rounded_type import RoundedType
from Tricount.business.participant import Participant
from Tricount.business.participation import Participation, ParticipationType

def test_get_balance_for_two_participants_in_one_activity():
    participants = (ActivityDriver()
                    .add_activity("bar", 23.5, ["harry", "hermione"], "harry")
                    .get_participants_with_balance_calculated())

    assert(is_participant_are_equal(Participant.create("harry", "11.75", [Participation.create("bar", 23.5, 2, ParticipationType.PAYER)], RoundedType.BELOW), participants[0])== True)
    assert(is_participant_are_equal(Participant.create("hermione", "-11.75", [Participation.create("bar", 23.5, 2, ParticipationType.FREELOADER)], RoundedType.BELOW), participants[1]) == True)

def test_get_balance_for_two_participants_in_three_activities():
    participants = (ActivityDriver()
                    .add_activity("bar", 23.5, ["harry", "hermione"], "harry")
                    .add_activity("restaurant", 50.7, ["harry", "hermione"], "hermione")
                    .add_activity("bowling", 12, ["harry", "hermione"], "harry")
                    .get_participants_with_balance_calculated())

    harry_participations = [Participation.create("bar", "23.5", 2, ParticipationType.PAYER), Participation.create("restaurant", "50.7", 2, ParticipationType.FREELOADER), Participation.create("bowling", "12", 2, ParticipationType.PAYER)]
    hermione_participations = [Participation.create("bar", "23.5", 2, ParticipationType.FREELOADER), Participation.create("restaurant", "50.7", 2, ParticipationType.PAYER), Participation.create("bowling", "12", 2, ParticipationType.FREELOADER)]
    assert(is_participant_are_equal(Participant.create("harry", "-7.6", harry_participations, RoundedType.BELOW), participants[0]) == True)
    assert(is_participant_are_equal(Participant.create("hermione", "7.6", hermione_participations, RoundedType.BELOW), participants[1]) == True)

def test_get_balance_for_three_participants_in_three_activities(): 
    participants = (ActivityDriver()
                    .add_activity("bar", 23.5, ["harry", "hermione"], "harry")
                    .add_activity("restaurant", 50.7, ["hermione", "ron"], "hermione")
                    .add_activity("bowling", 12, ["ron", "harry"], "ron")
                    .get_participants_with_balance_calculated())

    harry_participations = [Participation.create("bar", "23.5", 2, ParticipationType.PAYER), Participation.create("bowling", "12", 2, ParticipationType.FREELOADER)]
    hermione_participations = [Participation.create("bar", "23.5", 2, ParticipationType.FREELOADER), Participation.create("restaurant", "50.7", 2, ParticipationType.PAYER)]
    ron_participations = [Participation.create("restaurant", "50.7", 2, ParticipationType.FREELOADER), Participation.create("bowling", "12", 2, ParticipationType.PAYER)]
    assert(is_participant_are_equal(Participant.create("harry", "5.75", harry_participations, RoundedType.BELOW), participants[0]) == True)
    assert(is_participant_are_equal(Participant.create("hermione", "13.6", hermione_participations, RoundedType.BELOW), participants[1]) == True)
    assert(is_participant_are_equal(Participant.create("ron", "-19.35", ron_participations, RoundedType.BELOW), participants[2]) == True)

def test_get_balance_for_five_participants_in_six_activities(): 
    participants = (ActivityDriver()
                    .add_activity("bar", 23.5, ["harry", "hermione", "ron"], "harry")
                    .add_activity("restaurant", 50.7, ["hermione", "ron", "ginny", "hagrid"], "hermione")
                    .add_activity("bowling", 12, ["ron", "ginny"], "ron")
                    .add_activity("plane tickets", 1200, ["harry", "hermione", "ron", "ginny", "hagrid"], "ginny")
                    .add_activity("hotel", 615, ["harry", "hermione", "ron", "ginny","hagrid"], "hagrid")
                    .add_activity("spa day", 120, ["hermione", "ginny"], "hermione")
                    .get_participants_with_balance_calculated())
    harry_participations = [Participation.create( "bar", "23.5", 3, ParticipationType.PAYER), Participation.create("plane tickets", "1200", 5, ParticipationType.FREELOADER), Participation.create("hotel", "615", 5, ParticipationType.FREELOADER)]
    hermione_participations = [Participation.create( "bar", "23.5", 3, ParticipationType.FREELOADER), Participation.create("restaurant", "50.7", 4, ParticipationType.PAYER), Participation.create("plane tickets", "1200", 5, ParticipationType.FREELOADER), Participation.create("hotel", "615", 5, ParticipationType.FREELOADER), Participation.create("spa day", "120", 2, ParticipationType.PAYER)]
    ron_participations = [Participation.create("bar", "23.5", 3, ParticipationType.FREELOADER), Participation.create("restaurant", "50.7", 4, ParticipationType.FREELOADER), Participation.create("bowling", "12", 2, ParticipationType.PAYER), Participation.create("plane tickets", "1200", 5, ParticipationType.FREELOADER), Participation.create("hotel", "615", 5, ParticipationType.FREELOADER)]
    ginny_participations = [Participation.create("restaurant", "50.7", 4, ParticipationType.FREELOADER), Participation.create("bowling", "12", 2, ParticipationType.FREELOADER), Participation.create("plane tickets", "1200", 5, ParticipationType.PAYER), Participation.create("hotel", "615", 5, ParticipationType.FREELOADER), Participation.create("spa day", "120", 2, ParticipationType.FREELOADER)]
    hagrid_participations = [Participation.create("restaurant", "50.7", 4, ParticipationType.FREELOADER), Participation.create("plane tickets", "1200", 5, ParticipationType.FREELOADER), Participation.create("hotel", "615", 5, ParticipationType.PAYER)]
    assert(is_participant_are_equal(Participant.create("harry", "-347.34", harry_participations, RoundedType.BELOW), participants[0]) == True)
    assert(is_participant_are_equal(Participant.create("hermione", "-272.81", hermione_participations, RoundedType.BELOW), participants[1]) == True)
    assert(is_participant_are_equal(Participant.create("ron", "-377.51", ron_participations, RoundedType.BELOW), participants[2]) == True)
    assert(is_participant_are_equal(Participant.create("ginny", "758.32", ginny_participations, RoundedType.BELOW), participants[3]) == True)
    assert(is_participant_are_equal(Participant.create("hagrid", "239.32", hagrid_participations, RoundedType.BELOW), participants[4]) == True)

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
        self.balance_calculator = BalanceCalculator()

    def add_activity(self, name_activity, price, participants_name, payer):
        self.balance_calculator.add_activity(name_activity, price, participants_name, payer)
        return self

    def get_participants_with_balance_calculated(self):
        return self.balance_calculator.calculate_participants_balance_from_activities()