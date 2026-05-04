import pytest
from Tricount_EventStorming.activity_event import ActivityEvent
from Tricount_EventStorming.tests.test_trip import Trip, Participant
from dataclasses import FrozenInstanceError, dataclass
# expenses = [Expense(65.2, "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"]), Expense(22.4, "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"]), 
#                 Expense(24.2, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), Expense(13.6, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), 
#                 Expense(9.1, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), Expense(106, "Donatello", ["Raphaël", "Léonardo","Michelangelo", "Donatello"]), 
#                 Expense(3.4, "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"]), Expense(6.8, "Michelangelo", ["Donatello","Raphaël", "Léonardo", "Michelangelo"]), 
#                 Expense(14.99, "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"])]
#     assert (__get_participants(expenses) == [Participant("Léonardo", 21.18, CREDITOR), Participant("Michelangelo", -41.23, DEBTOR) , Participant("Donatello", 39.58, CREDITOR), 
#                                              Participant("Raphaël", -19.52, DEBTOR)])    
# def test_get_dream_team_participants_from_expenses():
#     expenses = [Expense(12.3, "Jordan", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"]), Expense(98.5, "Johnson", ["Jordan", "Johnson", "Pippen"]), 
#                 Expense(146.9, "Bird", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"]), Expense(49.4, "Barkley",["Bird", "Barkley", "Pippen"]), 
#                 Expense(75.6, "Pippen", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"]), Expense(186.6, "Jordan", ["Jordan", "Barkley", "Pippen"])]
#     assert (__get_participants(expenses) == [Participant("Jordan", 56.91, CREDITOR), Participant("Johnson", 18.71, CREDITOR) , Participant("Bird", 83.47, CREDITOR), 
#                                              Participant("Barkley", -76.23, DEBTOR), Participant("Pippen", -82.86, DEBTOR)])  

def test_init_good_restaurant_activity(): 
    activity = ActivityEvent("restaurant", "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"], 65.2)
    assert("restaurant" == activity.name)
    assert("Léonardo" == activity.paymaster)
    assert(["Michelangelo", "Donatello", "Raphaël", "Léonardo"] == activity.participants)
    assert(65.2 == activity.price)

def test_cannot_rename_activity(): 
    activity = ActivityEvent("restaurant", "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"], 65.2)
    with pytest.raises(FrozenInstanceError):
        activity.paymaster = "Raphaël"

# class ExpenseEvent:
#     def __init__(self, paymaster, activity) : 
#         self.paymaster = paymaster
#         self.activity = activity


# # class Trip : 
# #     def __init__(self):
# #         self.all_expenses_event = []

# #     def add_expense(self, expense) :
# #         #ici j'ajoute l'évènement
# #         pass 