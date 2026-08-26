from Tricount.business.manage_refunds import ManageRefunds
from Tricount.MoneyLogic.rounded_type import RoundedType
from Tricount.business.participant import Participant 
from Tricount.business.participation import Participation, ParticipationType
from Tricount.business.refund import Refund

def test_calculate_refunds_for_two_participants_in_one_activity():
    refunds_calculated = (RefundDriver()
               .add_participant(Participant.create("harry", "11.75", [Participation.create("bar", 23.5, 2, ParticipationType.PAYER)], RoundedType.BELOW))
               .add_participant(Participant.create("hermione", "-11.75", [Participation.create("bar", 23.5, 2, ParticipationType.FREELOADER)], RoundedType.BELOW))
               .get_refunds())
    refunds_expected = [Refund.create_refund("hermione", "harry", "11.75")]
    assert(len(refunds_calculated) == 1)
    assert(compare_all_refunds(refunds_expected, refunds_calculated))  
    
def test_calculate_refunds_for_three_participants_in_three_activities():
    harry_participations = [Participation.create("bar", "23.5", 2, ParticipationType.PAYER), Participation.create("bowling", "12", 2, ParticipationType.FREELOADER)]
    hermione_participations = [Participation.create("bar", "23.5", 2, ParticipationType.FREELOADER), Participation.create("restaurant", "50.7", 2, ParticipationType.PAYER)]
    ron_participations = [Participation.create("restaurant", "50.7", 2, ParticipationType.FREELOADER), Participation.create("bowling", "12", 2, ParticipationType.PAYER)]
    refunds_calculated = (RefundDriver()
                        .add_participant(Participant.create("harry", "5.75", harry_participations, RoundedType.BELOW))
                        .add_participant(Participant.create("hermione", "13.6", hermione_participations, RoundedType.BELOW))
                        .add_participant(Participant.create("ron", "-19.35", ron_participations, RoundedType.BELOW))
                        .get_refunds())
    refunds_expected = [Refund.create_refund("ron", "hermione", "13.6"), Refund.create_refund("ron", "harry", "5.75")]
    assert(len(refunds_calculated) == 2)
    assert(compare_all_refunds(refunds_expected, refunds_calculated)) 
    
def test_calculate_refunds_for_five_participants_in_six_activities() :  
    harry_participations = [Participation.create( "bar", "23.5", 3, ParticipationType.PAYER), Participation.create("plane tickets", "1200", 5, ParticipationType.FREELOADER), Participation.create("hotel", "615", 5, ParticipationType.FREELOADER)]
    hermione_participations = [Participation.create( "bar", "23.5", 3, ParticipationType.FREELOADER), Participation.create("restaurant", "50.7", 4, ParticipationType.PAYER), Participation.create("plane tickets", "1200", 5, ParticipationType.FREELOADER), Participation.create("hotel", "615", 5, ParticipationType.FREELOADER), Participation.create("spa day", "120", 2, ParticipationType.PAYER)]
    ron_participations = [Participation.create("bar", "23.5", 3, ParticipationType.FREELOADER), Participation.create("restaurant", "50.7", 4, ParticipationType.FREELOADER), Participation.create("bowling", "12", 2, ParticipationType.PAYER), Participation.create("plane tickets", "1200", 5, ParticipationType.FREELOADER), Participation.create("hotel", "615", 5, ParticipationType.FREELOADER)]
    ginny_participations = [Participation.create("restaurant", "50.7", 4, ParticipationType.FREELOADER), Participation.create("bowling", "12", 2, ParticipationType.FREELOADER), Participation.create("plane tickets", "1200", 5, ParticipationType.PAYER), Participation.create("hotel", "615", 5, ParticipationType.FREELOADER), Participation.create("spa day", "120", 2, ParticipationType.FREELOADER)]
    hagrid_participations = [Participation.create("restaurant", "50.7", 4, ParticipationType.FREELOADER), Participation.create("plane tickets", "1200", 5, ParticipationType.FREELOADER), Participation.create("hotel", "615", 5, ParticipationType.PAYER)]
    
    refunds_calculated = (RefundDriver()
                            .add_participant(Participant.create("harry", "-347.34", harry_participations, RoundedType.BELOW))
                            .add_participant(Participant.create("hermione", "-272.81", hermione_participations, RoundedType.BELOW))
                            .add_participant(Participant.create("ron", "-377.51", ron_participations, RoundedType.BELOW))
                            .add_participant(Participant.create("ginny", "758.32", ginny_participations, RoundedType.BELOW))
                            .add_participant(Participant.create("hagrid", "239.32", hagrid_participations, RoundedType.BELOW))
                            .get_refunds())
    
    refunds_expected = [Refund.create_refund("ron", "ginny", "377.51"), Refund.create_refund("harry", "ginny", "347.34"),
                        Refund.create_refund("hermione", "ginny", "33.47"), Refund.create_refund("hermione", "hagrid", "239.32")]
    assert(len(refunds_calculated) == 4)
    assert(compare_all_refunds(refunds_expected, refunds_calculated)) 
    
    
def compare_all_refunds(refunds_expected : Refund, refunds_calculated : Refund):
    is_equal = True
    for idx, _ in enumerate(refunds_expected): 
        refund_expected = refunds_expected[idx]
        refund_calculated = refunds_calculated[idx]
        is_equal = refund_expected.amount == refund_calculated.amount and refund_expected.recipient == refund_calculated.recipient and refund_expected.payer == refund_calculated.payer
        if is_equal == False : 
            break
    return is_equal 
    
class RefundDriver : 
    def __init__(self):
        self.participants = []
        self.manage_refunds = ManageRefunds()   
    
    def add_participant(self, participant : Participant) :
        self.manage_refunds.add_participant(participant)
        return self
    
    #TODO reprendre ce code et l'améliorer
    def get_refunds(self):
        return self.manage_refunds.calculate_all_refunds()