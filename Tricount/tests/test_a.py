from Tricount.refund import Refund
from Tricount.slate import Slate

def test_manage_bob_and_tome_expenses(): 
    expenses = { "bob": [45, 32.6, 24], "tom": [9.99, 3.54, 41.2, 6.35, 24.3,6.66, 1.01]}
    refund = Refund("tom", "bob", 4.27)
    assert(manage_expense(expenses) == refund)

def test_manage_amandhi_and_feng_expenses(): 
    expenses = {"amandhi" : [9.66, 3.24, 6.2], "feng": [4.35, 28.9]}
    refund = Refund("amandhi", "feng", 7.07)
    assert(manage_expense(expenses) == refund)

def manage_expense(expenses):
    slate = Slate(expenses)
    return slate.manage_expenses()   