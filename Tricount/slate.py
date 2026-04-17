from Tricount.refund import Refund

class Slate:
    def __init__(self, expenses):
        self.expenses = expenses

    def manage_expenses(self):
        expenses_by_person ={} 
        for person in self.expenses: 
            expenses_by_person[person] = 0
            for value_expense in self.expenses[person] : 
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