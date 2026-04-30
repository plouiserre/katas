DEBTOR = 0
CREDITOR = 0

class Participant :
    def __init__(self, name, balance, participant_type):
        self.name = name
        self.balance = balance
        self.participant_type = participant_type   

    def __eq__(self, other):
         if other != None : 
            return self.name == other.name and round(self.balance,2) == round(other.balance,2) and self.participant_type == other.participant_type
         else : 
            return False

    def determinate_all_datas_participant_from_expenses(self, participant_name, expenses): 
        balance_from_all_expenses = 0
        self.name = participant_name
        for expense in expenses : 
            if expense.paymaster == participant_name : 
                balance_from_all_expenses += round(expense.price, 2)
            for participant in expense.participants: 
                 if participant == participant_name : 
                      balance_from_all_expenses -= round(expense.price / len(expense.participants),2)
        if self.balance > 0 : 
            self.participant_type = CREDITOR
        else : 
            self.participant_type = DEBTOR
        self.balance = round(balance_from_all_expenses, 2)