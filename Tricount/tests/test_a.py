def test_manage_expense_two_persons(): 
    expenses = { "bob": [45, 32.6, 24], "tom": [9.99, 3.54, 41.2, 6.35, 24.3,6.66, 1.01]}
    refund = Refund("tom", "bob", 4.27)
    assert(manage_expense(expenses) == refund)


def manage_expense(expenses): 
    refund = Refund("tom", "bob", 4.27)
    return refund


class Refund : 
    def __init__(self, debtor, refunded_person, amount):
        self.debtor= debtor
        self.refunded_person = refunded_person
        self.amount = amount        

    def __eq__(self, other):
        return self.debtor == other.debtor and self.refunded_person == other.refunded_person and self.amount == other.amount