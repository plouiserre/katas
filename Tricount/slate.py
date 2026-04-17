from Tricount.refund import Refund

class Slate:
    def __init__(self, expenses):
        self.expenses = expenses
        self.less_expense = 0
        self.more_expense = 0
        self.debtor = ""
        self.refunded_person = ""
        self.expenses_by_person = {}
        self.amount_refund = 0

    def manage_expenses(self):
        self.__calculate_each_expense_by_friend() 
        self.__identify_each_element_of_refund()        
        refund = Refund(self.debtor, self.refunded_person, round(self.amount_refund, 2))
        return refund
    
    def __calculate_each_expense_by_friend(self) : 
        self.expenses_by_person ={} 
        for person in self.expenses: 
            self.expenses_by_person[person] = 0
            for value_expense in self.expenses[person] : 
                self.expenses_by_person[person] += value_expense
        return self.expenses_by_person
    
    def __identify_each_element_of_refund(self) :
        for person in self.expenses_by_person: 
            if self.expenses_by_person[person] < self.less_expense or self.less_expense == 0: 
                self.less_expense = self.expenses_by_person[person]
                self.debtor = person
            if self.expenses_by_person[person] >self. more_expense :
                self.more_expense = self.expenses_by_person[person] 
                self.refunded_person = person
        self.amount_refund = (self.more_expense - self.less_expense) / 2