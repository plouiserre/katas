class Refund : 
    def __init__(self, debtor, refunded_person, amount):
        self.debtor= debtor
        self.refunded_person = refunded_person
        self.amount = amount        

    def __eq__(self, other):
        return self.debtor == other.debtor and self.refunded_person == other.refunded_person and self.amount == other.amount