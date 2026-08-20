from TricountV2.activity import ActivityType
from TricountV2.MoneyLogic.rounded_type import RoundedType
from TricountV2.participant import Participant

def test_peter_paid_one_activity_for_his_friends():
    balance_participant = (ParticipantDriver("Peter")
                           .add_activities("bar", 23, 2, ActivityType.PAYER)
                           .get_balance())
    assert("11.5" == balance_participant)
    
def test_mj_paid_two_activities_for_his_friends():
    balance_participant = (ParticipantDriver("MJ")
                           .add_activities("massages", 120, 3, ActivityType.PAYER)
                           .add_activities("restaurant", 150, 5, ActivityType.PAYER)
                           .get_balance())
    assert("200.0" == balance_participant)
    
def test_ned_paid_three_activities_for_his_friends(): 
    balance_participant = (ParticipantDriver("Ned")
                           .add_activities("rent a car", 500, 3, ActivityType.PAYER)
                           .add_activities("jet ski", 99, 4, ActivityType.PAYER)
                           .add_activities("room", 100, 2, ActivityType.PAYER)
                           .get_balance()
                           )
    assert("457.58" == balance_participant)
    
def test_harry_participate_in_freeloader_mode_in_one_activity():
    balance_participant = (ParticipantDriver("Harry")
                           .add_activities("bar", 23, 2, ActivityType.FREELOADER)
                           .get_balance())
    assert("-11.5" == balance_participant)
    
def test_gwen_participate_in_freeloader_mode_in_two_activities():
    balance_participant = (ParticipantDriver("Gwen")
                           .add_activities("massages", 120, 3, ActivityType.FREELOADER)
                           .add_activities("restaurant", 150, 5, ActivityType.FREELOADER)
                           .get_balance())
    assert("-70.0" == balance_participant)
    
def test_norman_participate_in_freeloader_mode_in_three_activities(): 
    balance_participant = (ParticipantDriver("Norman")
                           .add_activities("rent a car", 500, 3, ActivityType.FREELOADER)
                           .add_activities("jet ski", 99, 4, ActivityType.FREELOADER)
                           .add_activities("room", 100, 2, ActivityType.FREELOADER)
                           .get_balance()
                           )
    assert("-241.41" == balance_participant)
    
def test_may_paid_and_participate_in_two_activities():
    balance_participant = (ParticipantDriver("May")
                          .add_activities("bar", 23, 2, ActivityType.FREELOADER)
                          .add_activities("buy cake", 30, 3, ActivityType.PAYER)
                          .get_balance()
                          )
    assert("8.5" == balance_participant)
    
def test_flash_paid_and_participate_in_four_activities():
    balance_participant = (ParticipantDriver("Flash")
                           .add_activities("restaurant", 150, 5, ActivityType.PAYER)
                           .add_activities("jet ski", 99, 4, ActivityType.FREELOADER)
                           .add_activities("massages", 120, 3, ActivityType.FREELOADER)
                           .add_activities("icecram", 40, 6, ActivityType.PAYER)
                           .get_balance())
    assert("88.58" == balance_participant)

def test_miles_paid_and_participate_in_nine_activities():
    balance_participant = (ParticipantDriver("Miles")
                          .add_activities("bottle club", 200, 4, ActivityType.PAYER)
                          .add_activities("restaurant", 66.78, 5, ActivityType.FREELOADER)
                          .add_activities("rent car", 500, 3, ActivityType.FREELOADER)
                          .add_activities("airbnb", 1200, 7, ActivityType.FREELOADER)
                          .add_activities("plane tickets", 1500, 4, ActivityType.PAYER)
                          .add_activities("museum", 20, 5, ActivityType.FREELOADER)
                          .add_activities("bar", 88, 7, ActivityType.FREELOADER)
                          .add_activities("bus", 24, 6, ActivityType.FREELOADER)
                          .add_activities("Uber", 51, 4, ActivityType.PAYER)
                          .get_balance())
    assert("941.25"== balance_participant)
    
class ParticipantDriver : 
    def __init__(self, name):
        self.participant = Participant(name, RoundedType.BELOW)
    
    def add_activities(self, name, price, number_participants, role):
        self.participant.add_activities(name, price, number_participants, role)
        return self
    
    def get_balance(self):
        return self.participant.get_balance()  