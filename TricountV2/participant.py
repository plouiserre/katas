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