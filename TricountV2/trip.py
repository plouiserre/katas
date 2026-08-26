from TricountV2.activity import Activity
from TricountV2.balance_calculator import BalanceCalculator
from TricountV2.manage_refunds import ManageRefunds


class Trip : 
    def __init__(self):
        self.activities = []
    
    def add_activity(self, name_activity, price, participants, payer):
        activity  = Activity.create(name_activity, price, participants, payer)
        self.activities.append(activity)
    
    def calculate_refunds(self):
        balance_calculator = BalanceCalculator()
        manage_refunds = ManageRefunds()
        for activity in self.activities :
            balance_calculator.add_activity(activity.name, activity.price, activity.participants_name, activity.payer)
        participants = balance_calculator.calculate_participants_balance_from_activities()
        for participant in participants : 
            manage_refunds.add_participant(participant)
        return manage_refunds.calculate_all_refunds()