import math

def test_manage_bob_and_tome_expenses(): 
    expenses = { "bob": [45, 32.6, 24], "tom": [9.99, 3.54, 41.2, 6.35, 24.3,6.66, 1.01]}
    refund = Refund("tom", "bob", 4.27)
    assert(manage_expense(expenses) == refund)

def test_manage_amandhi_and_feng_expenses(): 
    expenses = {"amandhi" : [9.66, 3.24, 6.2], "feng": [4.35, 28.9]}
    refund = Refund("amandhi", "feng", 7.07)
    assert(manage_expense(expenses) == refund)


def manage_expense(expenses):
    expenses_by_person ={} 
    for person in expenses: 
        expenses_by_person[person] = 0
        for value_expense in expenses[person] : 
            expenses_by_person[person] += value_expense
    less_expense = 0
    more_expense = 0
    debtor = ""
    refunded_person = ""
    for person in expenses_by_person: 
        if expenses_by_person[person] < less_expense or less_expense == 0: 
            less_expense = expenses_by_person[person]
            debtor = person
        if expenses_by_person[person] > more_expense :
            more_expense = expenses_by_person[person] 
            refunded_person = person
    amount_refund = (more_expense - less_expense) / 2
    refund = Refund(debtor, refunded_person, round(amount_refund, 2))
    return refund


class Refund : 
    def __init__(self, debtor, refunded_person, amount):
        self.debtor= debtor
        self.refunded_person = refunded_person
        self.amount = amount        

    def __eq__(self, other):
        return self.debtor == other.debtor and self.refunded_person == other.refunded_person and self.amount == other.amount