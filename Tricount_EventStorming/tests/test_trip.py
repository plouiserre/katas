from Tricount_EventStorming.activity_event import ActivityEvent 
from Tricount_EventStorming.participant import Participant, CREDITOR, DEBTOR
from Tricount_EventStorming.trip import Trip

def __init_ninja_trip_and_add_many_activity():
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
    return ninja_trip

def __init_basket_ball_trip_and_add_many_activity():
    basket_ball_trip = Trip()
    basket_ball_trip.add_activity(ActivityEvent("Glaces", "Jordan", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"], 12.3))
    basket_ball_trip.add_activity(ActivityEvent("Verres", "Johnson", ["Jordan", "Johnson", "Pippen"], 98.5))
    basket_ball_trip.add_activity(ActivityEvent("Champagnes", "Bird", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"], 146.9))
    basket_ball_trip.add_activity(ActivityEvent("Khebab", "Barkley", ["Bird", "Barkley", "Pippen"], 49.4))
    basket_ball_trip.add_activity(ActivityEvent("Uber", "Pippen", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"], 75.6))
    basket_ball_trip.add_activity(ActivityEvent("Second champagne bottle", "Jordan", ["Jordan", "Barkley", "Pippen"], 186.6))
    return basket_ball_trip

def test_count_all_expenses_trip_ninja_turtles(): 
    ninja_trip = __init_ninja_trip_and_add_many_activity()
    assert(ninja_trip.participants[0] == Participant("Léonardo", 21.18, CREDITOR))
    assert(ninja_trip.participants[1] == Participant("Michelangelo", -41.23, DEBTOR))
    assert(ninja_trip.participants[2] == Participant("Donatello", 39.58, CREDITOR))
    assert(ninja_trip.participants[3] == Participant("Raphaël", -19.52, DEBTOR))
    

def test_count_all_expenses_trip_dream_team(): 
    basket_ball_trip = __init_basket_ball_trip_and_add_many_activity()
    assert(basket_ball_trip.participants[0] == Participant("Jordan", 56.91, CREDITOR))
    assert(basket_ball_trip.participants[1] == Participant("Johnson", 18.71, CREDITOR))
    assert(basket_ball_trip.participants[2] == Participant("Bird", 83.47, CREDITOR))
    assert(basket_ball_trip.participants[3] == Participant("Barkley", -76.23, DEBTOR))
    assert(basket_ball_trip.participants[4] == Participant("Pippen", -82.86, DEBTOR))

# def test_calcul_all_refunds_for_trip_ninja_turtles():
#     ninja_trip = __init_ninja_trip_and_add_many_activity()
#     assert(ninja_trip.refunds[0] == Refund("Michelangelo", "Donatello", 39.58))
#     assert(ninja_trip.refunds[1] == Refund("Michelangelo", "Léonardo", 1.65), Refund("Raphaël", "Léonardo", 19.52))

# def test_calcul_all_refunds_for_trip_dream_team():
#     basket_ball_trip = __init_basket_ball_trip_and_add_many_activity()
#     assert(basket_ball_trip.refunds[0] == Refund("Pippen", "Bird", 82.86))
#     assert(basket_ball_trip.refunds[1] == Refund("Barkley", "Jordan", 56.91))
#     assert(basket_ball_trip.refunds[2] == Refund("Barkley", "Johnson", 18.71))