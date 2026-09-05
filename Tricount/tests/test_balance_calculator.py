from Tricount.business.balance_calculator import BalanceCalculator
from Tricount.business.participant import Participant
from Tricount.business.participation import Participation, ParticipationType
from Tricount.MoneyLogic.rounded_type import RoundedType

def test_get_balance_for_two_participants_in_one_activity():
    (ActivityDriver().add_activity("bar", 23.5, ["harry", "hermione"], "harry")
            .calculate_participants_with_balance()
            .is_valid_participant_with_participations("harry_11.75|bar_23.5_2_Payer")
            .is_valid_participant_with_participations("hermione_-11.75|bar_23.5_2_Freeloader"))
    
def test_get_balance_for_two_participants_in_three_activities():
    (ActivityDriver()
                    .add_activity("bar", 23.5, ["harry", "hermione"], "harry")
                    .add_activity("restaurant", 50.7, ["harry", "hermione"], "hermione")
                    .add_activity("bowling", 12, ["harry", "hermione"], "harry")
                    .calculate_participants_with_balance()
                    .is_valid_participant_with_participations("harry_-7.6|bar_23.5_2_Payer|restaurant_50.7_2_Freeloader|bowling_12_2_Payer")
                    .is_valid_participant_with_participations("hermione_7.6|bar_23.5_2_Freeloader|restaurant_50.7_2_Payer|bowling_12_2_Freeloader"))

def test_get_balance_for_three_participants_in_three_activities(): 
    (ActivityDriver()
                    .add_activity("bar", 23.5, ["harry", "hermione"], "harry")
                    .add_activity("restaurant", 50.7, ["hermione", "ron"], "hermione")
                    .add_activity("bowling", 12, ["ron", "harry"], "ron")
                    .calculate_participants_with_balance()
                    .is_valid_participant_with_participations("harry_5.75|bar_23.5_2_Payer|restaurant_50.7_2_Freeloader|bowling_12_2_Freeloader")
                    .is_valid_participant_with_participations("hermione_13.6|bar_23.5_2_Freeloader|restaurant_50.7_2_Payer|bowling_12_2_Freeloader")
                    .is_valid_participant_with_participations("ron_-19.35|bar_23.5_2_Freeloader|restaurant_50.7_2_Freeloader|bowling_12_2_Payer"))

def test_get_balance_for_five_participants_in_six_activities(): 
    (ActivityDriver()
                    .add_activity("bar", 23.5, ["harry", "hermione", "ron"], "harry")
                    .add_activity("restaurant", 50.7, ["hermione", "ron", "ginny", "hagrid"], "hermione")
                    .add_activity("bowling", 12, ["ron", "ginny"], "ron")
                    .add_activity("plane tickets", 1200, ["harry", "hermione", "ron", "ginny", "hagrid"], "ginny")
                    .add_activity("hotel", 615, ["harry", "hermione", "ron", "ginny","hagrid"], "hagrid")
                    .add_activity("spa day", 120, ["hermione", "ginny"], "hermione")
                    .calculate_participants_with_balance()
                    .is_valid_participant_with_participations("harry_-347.34|bar_23.5_3_Payer|plane tickets_1200_5_Freeloader|hotel_615_5_Freeloader")
                    .is_valid_participant_with_participations("hermione_-272.81|bar_23.5_3_Freeloader|restaurant_50.7_4_Payer|plane tickets_1200_5_Freeloader|hotel_615_5_Freeloader|spa day_120_2_Payer")
                    .is_valid_participant_with_participations("ron_-377.51|bar_23.5_3_Freeloader|restaurant_50.7_4_Freeloader|bowling_12_2_Payer|plane tickets_1200_5_Freeloader|hotel_615_5_Freeloader")
                    .is_valid_participant_with_participations("ginny_758.32|restaurant_50.7_4_Freeloader|bowling_12_2_Freeloader|plane tickets_1200_5_Payer|hotel_615_5_Freeloader|spa day_120_2_Freeloader")
                    .is_valid_participant_with_participations("hagrid_239.32|restaurant_50.7_4_Freeloader|plane tickets_1200_5_Freeloader|hotel_615_5_Payer"))

class ActivityDriver :
    def __init__(self):
        self.balance_calculator = BalanceCalculator()
        self.participants = []

    def add_activity(self, name_activity, price, participants_name, payer):
        self.balance_calculator.add_activity(name_activity, price, participants_name, payer)
        return self

    def calculate_participants_with_balance(self):
        self.participants = self.balance_calculator.calculate_participants_balance_from_activities()
        return self

    def is_valid_participant_with_participations(self, data_participant_participations_candidate):
        is_valid = False
        datas = data_participant_participations_candidate.split("|")
        data_participant = datas.pop(0).split("_")        
        participations_expected = self.__get_all_participations_expected(datas)
        participant_expected = Participant.create(data_participant[0], data_participant[1], participations_expected, RoundedType.BELOW)
        for participant in self.participants : 
            if participant.name == participant_expected.name : 
                is_valid_participant_data = participant.balance == participant_expected.balance 
                is_participations_valid = self.__valid_participations_participant(participant, participant_expected)
                is_valid = is_participations_valid and is_valid_participant_data
                break
        assert(is_valid)
        return self

    def __valid_participations_participant(self, participant, participant_expected):
        all_validation_participation = []
        for participation in participant.participations : 
            for participation_expected in participant_expected.participations : 
                if participation_expected.name == participation.name : 
                    is_valid_participation = participation.price == participation_expected.price and str(participation.number_participants) == participation_expected.number_participants and participation.role == participation_expected.role
                    all_validation_participation.append(is_valid_participation)
        return all(validation is True for validation in all_validation_participation)

    def __get_all_participations_expected(self, datas_participations):
        all_participations_expected = []
        for datas_participation in datas_participations:
            data_participation = datas_participation.split("_")
            role_participation = ParticipationType.PAYER if data_participation[3] == "Payer" else ParticipationType.FREELOADER
            participation_expected = Participation.create(data_participation[0], data_participation[1], data_participation[2], role_participation)
            all_participations_expected.append(participation_expected)
        return all_participations_expected