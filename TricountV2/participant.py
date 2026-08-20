from TricountV2.activity import Activity
from TricountV2.MoneyLogic.money import Money
from TricountV2.MoneyLogic.Operation.last_result_needed import LastResultNeeded


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
                self.money.divide_two_money(activity.price, activity.number_participants, LastResultNeeded.NotNeeded)
                self.money.substract_two_money(str(activity.price), None, LastResultNeeded.SecondMember)
                self.balance += float(self.money.display_final_result())
            elif activity.role == "Freeloader" : 
                self.money.divide_two_money(activity.price, activity.number_participants, LastResultNeeded.NotNeeded)
                self.balance -= float(self.money.display_final_result())
        return str(self.balance)