from TricountV2.activity import Activity
from TricountV2.MoneyLogic.money import Money

class Participant : 
    def __init__(self, name, rounded_type):
        self.name = name
        self.activites = []
        self.balance = 0
        self.money = Money(rounded_type)

    def add_activities(self, name, price, number_participants, role):
        self.activites.append(Activity.create(name, price, number_participants, role))
        return self
        
    def get_balance(self):
        for activity in self.activites :
            if activity.role == "Payer" :  
                self.balance += activity.calculate_balance_payer_activity(self.money)
            elif activity.role == "Freeloader" : 
                self.balance -= activity.calculate_balance_freeloader_activity(self.money)
        return str(self.balance)