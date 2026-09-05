from Tricount.business.balance_calculator import BalanceCalculator
from Tricount.MoneyLogic.rounded_type import RoundedType
from Tricount.business.participant import Participant
from Tricount.business.participation import Participation, ParticipationType

def test_get_balance_for_two_participants_in_one_activity():
    (ActivityDriver().add_activity("bar", 23.5, ["harry", "hermione"], "harry")
            .calculate_participants_with_balance()
            .is_valid_participant("harry_11.75")
            .is_valid_participant("hermione_-11.75")
            .is_valid_participation("bar_23.5_2_harry_hermione"))
    
def test_get_balance_for_two_participants_in_three_activities():
    (ActivityDriver()
                    .add_activity("bar", 23.5, ["harry", "hermione"], "harry")
                    .add_activity("restaurant", 50.7, ["harry", "hermione"], "hermione")
                    .add_activity("bowling", 12, ["harry", "hermione"], "harry")
                    .calculate_participants_with_balance()
                    .is_valid_participant("harry_-7.6")
                    .is_valid_participant("hermione_7.6")
                    .is_valid_participation("bar_23.5_2_harry_hermione")
                    .is_valid_participation("restaurant_50.7_2_hermione_harry")
                    .is_valid_participation("bowling_12_2_harry_hermione"))

def test_get_balance_for_three_participants_in_three_activities(): 
    (ActivityDriver()
                    .add_activity("bar", 23.5, ["harry", "hermione"], "harry")
                    .add_activity("restaurant", 50.7, ["hermione", "ron"], "hermione")
                    .add_activity("bowling", 12, ["ron", "harry"], "ron")
                    .calculate_participants_with_balance()
                    .is_valid_participant("harry_5.75")
                    .is_valid_participant("hermione_13.6")
                    .is_valid_participant("ron_-19.35")
                    .is_valid_participation("bar_23.5_2_harry_hermione")
                    .is_valid_participation("restaurant_50.7_2_hermione_ron")
                    .is_valid_participation("bowling_12_2_ron_harry"))

def test_get_balance_for_five_participants_in_six_activities(): 
    (ActivityDriver()
                    .add_activity("bar", 23.5, ["harry", "hermione", "ron"], "harry")
                    .add_activity("restaurant", 50.7, ["hermione", "ron", "ginny", "hagrid"], "hermione")
                    .add_activity("bowling", 12, ["ron", "ginny"], "ron")
                    .add_activity("plane tickets", 1200, ["harry", "hermione", "ron", "ginny", "hagrid"], "ginny")
                    .add_activity("hotel", 615, ["harry", "hermione", "ron", "ginny","hagrid"], "hagrid")
                    .add_activity("spa day", 120, ["hermione", "ginny"], "hermione")
                    .calculate_participants_with_balance()
                    .is_valid_participant("harry_-347.34")
                    .is_valid_participant("hermione_-272.81")
                    .is_valid_participant("ron_-377.51")
                    .is_valid_participant("ginny_758.32")
                    .is_valid_participant("hagrid_239.32")
                    .is_valid_participation("bar_23.5_3_harry_hermione|ron")
                    .is_valid_participation("restaurant_50.7_4_hermione_ron|ginny|hagrid")
                    .is_valid_participation("bowling_12_2_ron_ginny")
                    .is_valid_participation("plane tickets_1200_5_ginny_harry|hermione|ron|hagrid")
                    .is_valid_participation("hotel_615_5_hagrid_harry_hermione|ron|ginny")
                    .is_valid_participation("spa day_120_2_hermione_ginny"))

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
        self.participants = []

    def add_activity(self, name_activity, price, participants_name, payer):
        self.balance_calculator.add_activity(name_activity, price, participants_name, payer)
        return self

    def calculate_participants_with_balance(self):
            self.participants = self.balance_calculator.calculate_participants_balance_from_activities()
            return self

    def get_participants_with_balance_calculated(self):
        self.participants = self.balance_calculator.calculate_participants_balance_from_activities()
        return self.participants

    def is_valid_participant(self, data_participant_candidate):
        is_valid = False
        datas = data_participant_candidate.split("_")
        participant_candidate_name = datas[0]
        participant_candidate_balance = datas[1]
        for participant in self.participants : 
            if participant.name == participant_candidate_name and participant.balance == participant_candidate_balance : 
                is_valid = True
                break
        assert(is_valid)
        return self

    def is_valid_participation(self, data_participation_candidate):
        is_valid = True 
        datas = data_participation_candidate.split("_")
        participation_candidate_name = datas[0]
        participation_candidate_price = datas[1]
        participation_candidate_number_participants = datas[2]
        participation_candidate_payer = datas[3]
        participation_freeloaders = datas[4].split("|")
        for participant in self.participants :
            if participant.name == participation_candidate_payer : 
                is_participation_here = False
                for participation in participant.participations : 
                    if participation.name == participation_candidate_name : 
                        is_participation_here = True
                        if participation_candidate_price == str(participation.price) and participation_candidate_number_participants == str(participation.number_participants) and participation.role == ParticipationType.PAYER :
                            break
                        else : 
                            is_valid = False
                            break
            elif is_valid : 
                for participation in participant.participations :
                    if participation.name == participation_candidate_name : 
                        is_participation_here = True 
                        for freeloader_name in participation_freeloaders : 
                            if participant.name == freeloader_name : 
                                is_participation_here = True 
                                if participation_candidate_price == str(participation.price) and participation_candidate_number_participants == str(participation.number_participants) and participation.role == ParticipationType.FREELOADER :
                                    break
                                else : 
                                    is_valid = False
                                    break 
            else : 
                break
        if is_participation_here == False : 
            is_valid = False
        assert(is_valid)
        return self   