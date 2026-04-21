from Tricount.refund import Refund

class Slate:
    def __init__(self, expenses):
        self.expenses = expenses
        self.expenses_by_person = {}
        self.generous_friends = {}
        self.debt_friends = {}
        self.refunds = []

    def manage_expenses(self):
        self.__calculate_each_expense_by_friend() 
        self.__categorizes_friends_by_expenses()  
        self.__sorted_friends()
        refunds = self.__create_refunds()
        return refunds   
    
    def __calculate_each_expense_by_friend(self) : 
        self.expenses_by_person ={} 
        for expense in self.expenses: 
            if (expense.paymaster in self.expenses_by_person) == False : 
                self.expenses_by_person[expense.paymaster] = 0
            self.expenses_by_person[expense.paymaster] -= expense.price
            for participant in expense.participants : 
                if (participant in self.expenses_by_person) == False : 
                    self.expenses_by_person[participant] = 0
                self.expenses_by_person[participant] += round(expense.price / len(expense.participants), 2) 
        return self.expenses_by_person
    
    def __categorizes_friends_by_expenses(self): 
        for person in self.expenses_by_person : 
            debt = self.expenses_by_person[person]
            if debt > 0 : 
                self.debt_friends[person] = debt
            else : 
                self.generous_friends[person] = debt

    def __sorted_friends(self): 
        self.debt_friends = dict(sorted(self.debt_friends.items(), key = lambda item : item[1], reverse = True ))
        self.generous_friends = dict(sorted(self.generous_friends.items(), key = lambda item : item[1] ))

    def __create_refunds(self): 
        for generous_friend in self.generous_friends: 
            value_to_refund = round(0 - self.generous_friends[generous_friend], 2)
            turn = 0
            while(value_to_refund > 1 and turn < 20) :
                value_to_refund = self.__refund_generous_friend(generous_friend, value_to_refund)
                turn += 1
        return self.refunds
    
    def __refund_generous_friend(self, generous_friend, value_to_refund):
        first_debt_friend = next(iter(self.debt_friends))
        value_can_be_refund = round(self.debt_friends[first_debt_friend],2)
        if value_can_be_refund < value_to_refund : 
            new_refund = Refund(first_debt_friend, generous_friend, value_can_be_refund)
            self.refunds.append(new_refund)
            del self.debt_friends[first_debt_friend]
            value_to_refund = round(value_to_refund - value_can_be_refund,2)
        else : 
            new_refund = Refund(first_debt_friend, generous_friend, value_to_refund)
            self.refunds.append(new_refund)
            self.debt_friends[first_debt_friend] = round(self.debt_friends[first_debt_friend] - value_to_refund,2)
            value_to_refund = 0
        return value_to_refund