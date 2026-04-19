from Tricount.refund import Refund
from Tricount.slate import Slate

def test_manage_bob_and_tome_expenses(): 
    expenses = { "bob": [45, 32.6, 24], "tom": [9.99, 3.54, 41.2, 6.35, 24.3,6.66, 1.01]}
    refund = Refund("tom", "bob", 4.27)
    refunds = [refund]
    are_refunds_equals(refunds, expenses)

def test_manage_amandhi_and_feng_expenses(): 
    expenses = {"amandhi" : [9.66, 3.24, 6.2], "feng": [4.35, 28.9]}
    refund = Refund("amandhi", "feng", 7.07)
    refunds = [refund]
    are_refunds_equals(refunds, expenses)

def test_manage_four_friends_expenses_simple(): 
    expenses = {"Léonardo": [65.2,22.4], "Raphaël":[24.2,13.6,9.1], "Donatello":[106], "Michelangelo":[3.4,6.8,14.99]}
    first_refund = Refund("Michelangelo", "Donatello", 39.58)
    second_refund = Refund("Michelangelo", "Léonardo", 1.65)
    third_refund = Refund("Raphaël", "Léonardo", 19.52)
    refunds = [first_refund, second_refund, third_refund]
    are_refunds_equals(refunds, expenses)

def are_refunds_equals(expected_refunds, expenses):
    refunds = manage_expense(expenses)
    for idx, refund in enumerate(refunds):
        assert(refund == expected_refunds[idx])

def manage_expense(expenses):
    slate = Slate(expenses)
    return slate.manage_expenses()   