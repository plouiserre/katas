from Tricount_EventStorming.activity_event import ActivityEvent 
from Tricount_EventStorming.participant import Participant, CREDITOR, DEBTOR
from Tricount_EventStorming.trip import Trip

def test_count_all_expenses_trip_ninja_turtles(): 
    trip = Trip()
    trip.add_activity(ActivityEvent("Restaurant", "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"], 65.2)) 
    trip.add_activity(ActivityEvent("Verres", "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"], 22.4)) 
    trip.add_activity(ActivityEvent("Bowling", "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"], 24.2))
    trip.add_activity(ActivityEvent("Glaces", "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"], 13.6))
    trip.add_activity(ActivityEvent("Café", "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"], 9.1))
    trip.add_activity(ActivityEvent("Location surfs", "Donatello", ["Raphaël", "Léonardo","Michelangelo", "Donatello"], 106))
    trip.add_activity(ActivityEvent("Bonbons", "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"], 3.4))
    trip.add_activity(ActivityEvent("Sucettes", "Michelangelo", ["Donatello","Raphaël", "Léonardo", "Michelangelo"], 6.8))
    trip.add_activity(ActivityEvent("Achat ballon plages", "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"], 14.99))

    assert(trip.participants[0] == Participant("Léonardo", 21.18, CREDITOR))
    assert(trip.participants[1] == Participant("Michelangelo", -41.23, DEBTOR))
    assert(trip.participants[2] == Participant("Donatello", 39.58, CREDITOR))
    assert(trip.participants[3] == Participant("Raphaël", -19.52, DEBTOR))

def test_count_all_expenses_trip_dream_team(): 
    trip = Trip()
    trip.add_activity(ActivityEvent("Glaces", "Jordan", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"], 12.3))
    trip.add_activity(ActivityEvent("Verres", "Johnson", ["Jordan", "Johnson", "Pippen"], 98.5))
    trip.add_activity(ActivityEvent("Champagnes", "Bird", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"], 146.9))
    trip.add_activity(ActivityEvent("Khebab", "Barkley", ["Bird", "Barkley", "Pippen"], 49.4))
    trip.add_activity(ActivityEvent("Uber", "Pippen", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"], 75.6))
    trip.add_activity(ActivityEvent("Second champagne bottle", "Jordan", ["Jordan", "Barkley", "Pippen"], 186.6))

    assert(trip.participants[0] == Participant("Jordan", 56.91, CREDITOR))
    assert(trip.participants[1] == Participant("Johnson", 18.71, CREDITOR))
    assert(trip.participants[2] == Participant("Bird", 83.47, CREDITOR))
    assert(trip.participants[3] == Participant("Barkley", -76.23, DEBTOR))
    assert(trip.participants[4] == Participant("Pippen", -82.86, DEBTOR))

class Refund : 
    def __init__(self, debtor, refunded_person, amount):
        self.debtor= debtor
        self.refunded_person = refunded_person
        self.amount = amount        

    def __eq__(self, other):
        return self.debtor == other.debtor and self.refunded_person == other.refunded_person and self.amount == other.amount