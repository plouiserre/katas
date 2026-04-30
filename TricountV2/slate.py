from Tricount.refund import Refund

class Slate:
    def __init__(self, expenses, event):
        self.expenses = expenses
        self.event = event
        self.expenses_by_person = {}
        self.generous_friends = []
        self.debt_friends = []
        self.participants = []
        self.refunds = []

    def manage_expenses(self):
        self.participants = self.event.get_participants_from_expenses()
        self.__sorted_friends()
        refunds = self.__create_refunds()
        return refunds   
    
    def __sorted_friends(self): 
        debt_friends = []
        generous_friends = []
        for participant in self.participants :
            if participant.balance < 0 : 
                debt_friends.append(participant)
            else : 
                generous_friends.append(participant)
        self.debt_friends = sorted(self.debt_friends, key=lambda x:x.balance)
        self.generous_friends = sorted(self.generous_friends, key=lambda x:x.balance, reverse= True )

    def __create_refunds(self): 
        for generous_friend in self.generous_friends: 
            value_to_refund = round(0 - generous_friend.balance, 2)
            turn = 0
            while(value_to_refund > 1 and turn < 20) :
                value_to_refund = self.__refund_generous_friend(generous_friend, value_to_refund)
                turn += 1
        return self.refunds
    
    def __refund_generous_friend(self, generous_friend, value_to_refund):
        first_debt_friend = next(iter(self.debt_friends))
        value_can_be_refund = - round(self.debt_friends.balance,2)
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