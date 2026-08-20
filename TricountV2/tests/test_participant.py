from TricountV2.participation import ParticipationType
from TricountV2.MoneyLogic.rounded_type import RoundedType
from TricountV2.participant import Participant

def test_peter_paid_one_activity_for_his_friends():
    balance_participant = (ParticipantDriver("Peter")
                           .add_participation("bar", 23, 2, ParticipationType.PAYER)
                           .get_balance())
    assert("11.5" == balance_participant)
    
def test_mj_paid_two_activities_for_his_friends():
    balance_participant = (ParticipantDriver("MJ")
                           .add_participation("massages", 120, 3, ParticipationType.PAYER)
                           .add_participation("restaurant", 150, 5, ParticipationType.PAYER)
                           .get_balance())
    assert("200.0" == balance_participant)
    
def test_ned_paid_three_activities_for_his_friends(): 
    balance_participant = (ParticipantDriver("Ned")
                           .add_participation("rent a car", 500, 3, ParticipationType.PAYER)
                           .add_participation("jet ski", 99, 4, ParticipationType.PAYER)
                           .add_participation("room", 100, 2, ParticipationType.PAYER)
                           .get_balance()
                           )
    assert("457.58" == balance_participant)
    
def test_harry_participate_in_freeloader_mode_in_one_activity():
    balance_participant = (ParticipantDriver("Harry")
                           .add_participation("bar", 23, 2, ParticipationType.FREELOADER)
                           .get_balance())
    assert("-11.5" == balance_participant)
    
def test_gwen_participate_in_freeloader_mode_in_two_activities():
    balance_participant = (ParticipantDriver("Gwen")
                           .add_participation("massages", 120, 3, ParticipationType.FREELOADER)
                           .add_participation("restaurant", 150, 5, ParticipationType.FREELOADER)
                           .get_balance())
    assert("-70.0" == balance_participant)
    
def test_norman_participate_in_freeloader_mode_in_three_activities(): 
    balance_participant = (ParticipantDriver("Norman")
                           .add_participation("rent a car", 500, 3, ParticipationType.FREELOADER)
                           .add_participation("jet ski", 99, 4, ParticipationType.FREELOADER)
                           .add_participation("room", 100, 2, ParticipationType.FREELOADER)
                           .get_balance()
                           )
    assert("-241.41" == balance_participant)
    
def test_may_paid_and_participate_in_two_activities():
    balance_participant = (ParticipantDriver("May")
                          .add_participation("bar", 23, 2, ParticipationType.FREELOADER)
                          .add_participation("buy cake", 30, 3, ParticipationType.PAYER)
                          .get_balance()
                          )
    assert("8.5" == balance_participant)
    
def test_flash_paid_and_participate_in_four_activities():
    balance_participant = (ParticipantDriver("Flash")
                           .add_participation("restaurant", 150, 5, ParticipationType.PAYER)
                           .add_participation("jet ski", 99, 4, ParticipationType.FREELOADER)
                           .add_participation("massages", 120, 3, ParticipationType.FREELOADER)
                           .add_participation("icecram", 40, 6, ParticipationType.PAYER)
                           .get_balance())
    assert("88.58" == balance_participant)

def test_miles_paid_and_participate_in_nine_activities():
    balance_participant = (ParticipantDriver("Miles")
                          .add_participation("bottle club", 200, 4, ParticipationType.PAYER)
                          .add_participation("restaurant", 66.78, 5, ParticipationType.FREELOADER)
                          .add_participation("rent car", 500, 3, ParticipationType.FREELOADER)
                          .add_participation("airbnb", 1200, 7, ParticipationType.FREELOADER)
                          .add_participation("plane tickets", 1500, 4, ParticipationType.PAYER)
                          .add_participation("museum", 20, 5, ParticipationType.FREELOADER)
                          .add_participation("bar", 88, 7, ParticipationType.FREELOADER)
                          .add_participation("bus", 24, 6, ParticipationType.FREELOADER)
                          .add_participation("Uber", 51, 4, ParticipationType.PAYER)
                          .get_balance())
    assert("941.25"== balance_participant)
    
class ParticipantDriver : 
    def __init__(self, name):
        self.participant = Participant(name, RoundedType.BELOW)
    
    def add_participation(self, name, price, number_participants, role):
        self.participant.add_participation(name, price, number_participants, role)
        return self
    
    def get_balance(self):
        return self.participant.get_balance()  