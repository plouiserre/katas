from TricountV2.refund import Refund
from TricountV2.trip import Trip

def test_1():
    refunds_calculated = (TripDriver()
                            .add_activity("bar", 23.5, ["harry", "hermione"], "harry")
                            .calculate_refunds())
    refunds_expected = [Refund.create_refund("hermione", "harry", "11.75")]
    assert(len(refunds_calculated) == 1)
    assert(compare_all_refunds(refunds_expected, refunds_calculated)) 

def test_2():
    refunds_calculated = (TripDriver()
                            .add_activity("bar", 23.5, ["harry", "hermione"], "harry")
                            .add_activity("restaurant", 50.7, ["hermione", "ron"], "hermione")
                            .add_activity("bowling", 12, ["ron", "harry"], "ron")
                            .calculate_refunds()
                            )
    refunds_expected = [Refund.create_refund("ron", "hermione", "13.6"), Refund.create_refund("ron", "harry", "5.75")]
    assert(len(refunds_calculated) == 2)
    assert(compare_all_refunds(refunds_expected, refunds_calculated)) 
    
def test_3():
    refunds_calculated = (TripDriver()
                            .add_activity("bar", 23.5, ["harry", "hermione", "ron"], "harry")
                            .add_activity("restaurant", 50.7, ["hermione", "ron", "ginny", "hagrid"], "hermione")
                            .add_activity("bowling", 12, ["ron", "ginny"], "ron")
                            .add_activity("plane tickets", 1200, ["harry", "hermione", "ron", "ginny", "hagrid"], "ginny")
                            .add_activity("hotel", 615, ["harry", "hermione", "ron", "ginny","hagrid"], "hagrid")
                            .add_activity("spa day", 120, ["hermione", "ginny"], "hermione")
                            .calculate_refunds())
    
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
    
    
class TripDriver : 
    def __init__(self):
        self.trip = Trip()
    
    def add_activity(self, name_activity, price, participants, payer):
        self.trip.add_activity(name_activity, price, participants, payer)
        return self
    
    def calculate_refunds(self):
        return self.trip.calculate_refunds()