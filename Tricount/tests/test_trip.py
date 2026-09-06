from Tricount.business.refund import Refund
from Tricount.business.trip import Trip

def test_calculate_all_trip_with_one_activity_and_two_persons():
    (TripDriver()
            .add_activity("bar", 23.5, ["harry", "hermione"], "harry")
            .calculate_refunds()
            .valid_refund("hermione_harry_11.75"))

def test_calculate_all_trip_with_three_activities_and_three_persons():
    (TripDriver()
            .add_activity("bar", 23.5, ["harry", "hermione"], "harry")
            .add_activity("restaurant", 50.7, ["hermione", "ron"], "hermione")
            .add_activity("bowling", 12, ["ron", "harry"], "ron")
            .calculate_refunds()
            .valid_refund("ron_hermione_13.6")
            .valid_refund("ron_harry_5.75")
            )
    
def test_calculate_all_trip_with_six_activities_and_five_persons():
    (TripDriver()
            .add_activity("bar", 23.5, ["harry", "hermione", "ron"], "harry")
            .add_activity("restaurant", 50.7, ["hermione", "ron", "ginny", "hagrid"], "hermione")
            .add_activity("bowling", 12, ["ron", "ginny"], "ron")
            .add_activity("plane tickets", 1200, ["harry", "hermione", "ron", "ginny", "hagrid"], "ginny")
            .add_activity("hotel", 615, ["harry", "hermione", "ron", "ginny","hagrid"], "hagrid")
            .add_activity("spa day", 120, ["hermione", "ginny"], "hermione")
            .calculate_refunds()
            .valid_refund("ron_ginny_377.51")
            .valid_refund("harry_ginny_347.34")
            .valid_refund("hermione_ginny_33.47")
            .valid_refund("hermione_hagrid_239.32"))    
    
class TripDriver : 
    def __init__(self):
        self.trip = Trip()
        self.refunds = []
    
    def add_activity(self, name_activity, price, participants, payer):
        self.trip.add_activity(name_activity, price, participants, payer)
        return self

    def calculate_refunds(self):
        self.refunds = self.trip.calculate_refunds()
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