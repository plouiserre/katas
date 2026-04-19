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
        self.average_expense = 0
        self.positifs_friends = {}
        self.negatifs_friends = {}
        self.refunds = []

    def manage_expenses(self):
        self.__calculate_each_expense_by_friend() 
        self.__identify_each_element_of_refund()   
        self.__calculate_average_expense()   
        self.__categorizes_friends_by_expenses()  
        self.__sorted_friends()
        refunds = self.__create_refunds()
        # refunds = []
        # refund = Refund(self.debtor, self.refunded_person, round(self.amount_refund, 2))
        # refunds.append(refund)
        return refunds   
    
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

    def __calculate_average_expense(self): 
        all_expenses = 0
        for person in self.expenses_by_person :
            all_expenses += self.expenses_by_person[person]
        self.average_expense =  round(all_expenses / len(self.expenses_by_person),2)

    def __categorizes_friends_by_expenses(self): 
        for person in self.expenses_by_person : 
            expenses = self.expenses_by_person[person]
            if expenses < self.average_expense : 
                self.negatifs_friends[person] = expenses
            else : 
                self.positifs_friends[person] = expenses

    def __sorted_friends(self): 
        self.negatifs_friends = dict(sorted(self.negatifs_friends.items(), key = lambda item : item[1] ))
        self.positifs_friends = dict(sorted(self.positifs_friends.items(), key = lambda item : item[1], reverse = True ))

    def __create_refunds(self): 
        for positif_friend in self.positifs_friends: 
            value_to_refund = round(self.positifs_friends[positif_friend] - self.average_expense, 2)
            turn = 0
            while(value_to_refund > 1 and turn < 20) :
                first_negatif_friend = next(iter(self.negatifs_friends))
                value_can_be_refund = round(self.average_expense - self.negatifs_friends[first_negatif_friend],2)
                if value_can_be_refund < value_to_refund : 
                    new_refund = Refund(first_negatif_friend, positif_friend, value_can_be_refund)
                    self.refunds.append(new_refund)
                    del self.negatifs_friends[first_negatif_friend]
                    value_to_refund = round(value_to_refund - value_can_be_refund,2)
                else : 
                    new_refund = Refund(first_negatif_friend, positif_friend, value_to_refund)
                    self.refunds.append(new_refund)
                    self.negatifs_friends[first_negatif_friend] = round(self.negatifs_friends[first_negatif_friend] + value_to_refund,2)
                    value_to_refund = 0
                turn += 1
        return self.refunds
