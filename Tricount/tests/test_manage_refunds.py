from decimal import Decimal

from Tricount.business.manage_refunds import ManageRefunds
from Tricount.MoneyLogic.rounded_type import RoundedType
from Tricount.business.participant import Participant 
from Tricount.business.participation import Participation, ParticipationType
from Tricount.business.refund import Refund

def test_calculate_refunds_for_two_participants_in_one_activity():
    (RefundDriver()
               .add_participant_with_participation("harry_11.75|bar_23.5_2_Payer")
               .add_participant_with_participation("hermione_-11.75|bar_23.5_2_Freeloader")
               .calculate_refunds()
               .valid_refund("hermione_harry_11.75"))
    
    
def test_calculate_refunds_for_three_participants_in_three_activities():
    (RefundDriver()
                .add_participant_with_participation("harry_5.75|bar_23.5_2_Payer|bowling_12_2_Freeloader")
                .add_participant_with_participation("hermione_13.6|bar_23.5_2_Freeloader|restaurant_50.7_2_Payer")
                .add_participant_with_participation("ron_-19.35|restaurant_50.7_2_Freeloader|bowling_12_2_Payer")
                .calculate_refunds()
                .valid_refund("ron_hermione_13.6")
                .valid_refund("ron_harry_5.75"))
    
def test_calculate_refunds_for_five_participants_in_six_activities() :  
    (RefundDriver()
                .add_participant_with_participation("harry_-347.34|bar_23.5_3_Payer|plane tickets_1200_5_Freeloader|hotel_615_5_Freeloader")
                .add_participant_with_participation("hermione_-272.91|bar_23.5_3_Freeloader|restaurant_50.4_4_Payer|plane tickets_1200_5_Freeloader|hotel_615_5_Freeloader|spa day_120_2_Payer")
                .add_participant_with_participation("ron_-377.51|bar_23.5_3_Freeloader|restaurant_50.4_4_Freeloader|bowling_12_2_Payer|plane tickets_1200_5_Freeloader|hotel_615_5_Freeloader")
                .add_participant_with_participation("ginny_758.32|restaurant_50.4_4_Freeloader|bowling_12_2_Freeloader|plane tickets_1200_5_Payer|hotel_615_5_Freeloader|spa day_120_2_Freeloader")
                .add_participant_with_participation("hagrid_239.32|restaurant_50.4_4_Freeloader|plane tickets_1200_5_Freeloader|hotel_615_5_Payer")
                .calculate_refunds()
                .valid_refund("ron_ginny_377.51")
                .valid_refund("harry_ginny_347.34")
                .valid_refund("hermione_ginny_33.47")
                .valid_refund("hermione_hagrid_239.32"))    
    
class RefundDriver : 
    def __init__(self):
        self.participants = []
        self.manage_refunds = ManageRefunds()
        self.refunds = []
    
    def add_participant(self, participant : Participant) :
        self.manage_refunds.add_participant(participant)
        return self

    def add_participant_with_participation(self, datas_participant):
        all_participations = []
        datas_split = datas_participant.split("|")
        data_only_participant = datas_split.pop(0).split("_")
        for data_split in datas_split:
            data_participation = data_split.split("_")
            participation_type = ParticipationType.PAYER if data_participation[3] == "Payer" else ParticipationType.FREELOADER
            participation = Participation.create(data_participation[0], Decimal(data_participation[1]), int(data_participation[2]), participation_type)
            all_participations.append(participation)
        self.manage_refunds.add_participant(Participant.create(data_only_participant[0], data_only_participant[1], all_participations, RoundedType.BELOW))
        return self
    
    def calculate_refunds(self):
        self.refunds = self.manage_refunds.calculate_all_refunds()
        return self

    def valid_refund(self, refund_data_expected):
        is_valid = False
        for refund in self.refunds : 
            refund_datas_calculated = str(refund.payer)+"_"+str(refund.recipient)+"_"+str(refund.amount)
            if refund_datas_calculated == refund_data_expected : 
                is_valid = True
                break
        assert(is_valid)
        return self  