from TricountV2.activity import Activity
from TricountV2.MoneyLogic.rounded_type import RoundedType
from TricountV2.participant import Participant

def test1():
    balance_participant = (ParticipantDriver("Peter")
                           .add_activities("bar", 23, 2, "Payer")
                           .get_balance())
    assert("11.5" == balance_participant)
    
def test2():
    balance_participant = (ParticipantDriver("MJ")
                           .add_activities("massages", 120, 3, "Payer")
                           .add_activities("restaurant", 150, 5, "Payer")
                           .get_balance())
    assert("200.0" == balance_participant)
    
def test3(): 
    balance_participant = (ParticipantDriver("Ned")
                           .add_activities("rent a car", 500, 3, "Payer")
                           .add_activities("jet ski", 99, 4, "Payer")
                           .add_activities("room", 100, 2, "Payer")
                           .get_balance()
                           )
    assert("457.58" == balance_participant)
    
def test4():
    balance_participant = (ParticipantDriver("Harry")
                           .add_activities("bar", 23, 2, "Freeloader")
                           .get_balance())
    assert("-11.5" == balance_participant)
    
def test5():
    balance_participant = (ParticipantDriver("Gwen")
                           .add_activities("massages", 120, 3, "Freeloader")
                           .add_activities("restaurant", 150, 5, "Freeloader")
                           .get_balance())
    assert("-70.0" == balance_participant)
    
def test6(): 
    balance_participant = (ParticipantDriver("Norman")
                           .add_activities("rent a car", 500, 3, "Freeloader")
                           .add_activities("jet ski", 99, 4, "Freeloader")
                           .add_activities("room", 100, 2, "Freeloader")
                           .get_balance()
                           )
    assert("-241.41" == balance_participant)
    
def test7():
    balance_participant = (ParticipantDriver("May")
                          .add_activities("bar", 23, 2, "Freeloader")
                          .add_activities("buy cake", 30, 3, "Payer")
                          .get_balance()
                          )
    assert("8.5" == balance_participant)
    
def test8():
    balance_participant = (ParticipantDriver("Flash")
                           .add_activities("restaurant", 150, 5, "Payer")
                           .add_activities("jet ski", 99, 4, "Freeloader")
                           .add_activities("massages", 120, 3, "Freeloader")
                           .add_activities("icecram", 40, 6, "Payer")
                           .get_balance())
    assert("88.58" == balance_participant)

def test9():
    balance_participant = (ParticipantDriver("Miles")
                          .add_activities("bottle club", 200, 4, "Payer")
                          .add_activities("restaurant", 66.78, 5, "Freeloader")
                          .add_activities("rent car", 500, 3, "Freeloader")
                          .add_activities("airbnb", 1200, 7, "Freeloader")
                          .add_activities("plane tickets", 1500, 4, "Payer")
                          .add_activities("museum", 20, 5, "Freeloader")
                          .add_activities("bar", 88, 7, "Freeloader")
                          .add_activities("bus", 24, 6, "Freeloader")
                          .add_activities("Uber", 51, 4, "Payer")
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