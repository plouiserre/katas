from Tricount_EventStorming.activity_event import ActivityEvent
from Tricount_EventStorming.refund import Refund
from Tricount_EventStorming.trip import Trip

def test_1(): 
    ninja_trip = Trip()
    ninja_trip.add_activity(ActivityEvent("Restaurant", "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"], 65.2)) 
    refunds_expected = [
        Refund(__get_participant_by_name(ninja_trip, "Michelangelo"), __get_participant_by_name(ninja_trip, "Léonardo"), 16.3),
        Refund(__get_participant_by_name(ninja_trip, "Donatello"), __get_participant_by_name(ninja_trip, "Léonardo"), 16.3),
        Refund(__get_participant_by_name(ninja_trip, "Raphaël"), __get_participant_by_name(ninja_trip, "Léonardo"), 16.3)
    ]
    refunds_calculated = __get_refunds_from_trip(ninja_trip)
    for idx, refund in enumerate(refunds_calculated) : 
        assert(refunds_expected[idx] == refund)


def test_2():
    ninja_trip = Trip()
    ninja_trip.add_activity(ActivityEvent("Restaurant", "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"], 65.2)) 
    ninja_trip.add_activity(ActivityEvent("Verres", "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"], 22.4)) 
    ninja_trip.add_activity(ActivityEvent("Bowling", "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"], 24.2))
    ninja_trip.add_activity(ActivityEvent("Glaces", "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"], 13.6))
    ninja_trip.add_activity(ActivityEvent("Café", "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"], 9.1))
    ninja_trip.add_activity(ActivityEvent("Location surfs", "Donatello", ["Raphaël", "Léonardo","Michelangelo", "Donatello"], 106))
    ninja_trip.add_activity(ActivityEvent("Bonbons", "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"], 3.4))
    ninja_trip.add_activity(ActivityEvent("Sucettes", "Michelangelo", ["Donatello","Raphaël", "Léonardo", "Michelangelo"], 6.8))
    ninja_trip.add_activity(ActivityEvent("Achat ballon plages", "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"], 14.99))
    refunds_expected = [
        Refund(__get_participant_by_name(ninja_trip, "Michelangelo"), __get_participant_by_name(ninja_trip, "Donatello"), 39.58),
        Refund(__get_participant_by_name(ninja_trip, "Michelangelo"), __get_participant_by_name(ninja_trip, "Léonardo"), 1.65),
        Refund(__get_participant_by_name(ninja_trip, "Raphaël"), __get_participant_by_name(ninja_trip, "Léonardo"), 19.52)
    ]
    refunds_calculated = __get_refunds_from_trip(ninja_trip)
    for idx, refund in enumerate(refunds_calculated) : 
        assert(refunds_expected[idx] == refund)

def test_3(): 
    basket_ball_trip = Trip()
    basket_ball_trip.add_activity(ActivityEvent("Glaces", "Jordan", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"], 12.3))
    basket_ball_trip.add_activity(ActivityEvent("Verres", "Johnson", ["Jordan", "Johnson", "Pippen"], 98.5))
    basket_ball_trip.add_activity(ActivityEvent("Champagnes", "Bird", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"], 146.9))
    basket_ball_trip.add_activity(ActivityEvent("Khebab", "Barkley", ["Bird", "Barkley", "Pippen"], 49.4))
    basket_ball_trip.add_activity(ActivityEvent("Uber", "Pippen", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"], 75.6))
    basket_ball_trip.add_activity(ActivityEvent("Second champagne bottle", "Jordan", ["Jordan", "Barkley", "Pippen"], 186.6))
    refunds_expected = [
        Refund(__get_participant_by_name(basket_ball_trip, "Pippen"), __get_participant_by_name(basket_ball_trip, "Bird"), 82.86),
        Refund(__get_participant_by_name(basket_ball_trip, "Barkley"), __get_participant_by_name(basket_ball_trip, "Bird"), 0.61),
        Refund(__get_participant_by_name(basket_ball_trip, "Barkley"), __get_participant_by_name(basket_ball_trip, "Jordan"), 56.91),
        Refund(__get_participant_by_name(basket_ball_trip, "Barkley"), __get_participant_by_name(basket_ball_trip, "Johnson"), 18.71)
    ]
    refunds_calculated = __get_refunds_from_trip(basket_ball_trip)
    for idx, refund in enumerate(refunds_calculated) : 
        assert(refunds_expected[idx] == refund)


def __get_refunds_from_trip(ninja_trip):
    refunds = ninja_trip.calculate_refunds_from_trip()
    return refunds

def __get_participant_by_name(trip, name): 
    for participant in trip.participants : 
        if participant.name == name : 
            return participant