DEBTOR = 0
CREDITOR = 1

class Participant : 
    def __init__(self,name, balance, participant_type):
        self.name = name 
        self.balance = balance
        self.participant_type = participant_type

    def __eq__(self, other):
        if other == None : 
            return False
        return self.name == other.name and self.balance == other.balance    
    
    def add_activity_you_paid(self, activity): 
        self.balance = round(self.balance + activity.price, 2)
        if self.balance > 0 : 
            self.participant_type = CREDITOR

    def add_activity_you_participe(self, activity):
        price_by_participant = round(activity.price / len(activity.participants), 2)
        self.balance = round(self.balance - price_by_participant, 2)
        if self.balance < 0 : 
            self.participant_type = DEBTOR