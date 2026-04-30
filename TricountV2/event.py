from TricountV2.participant import CREDITOR, DEBTOR, Participant

class Event : 
    def __init__(self, expenses):
        self.expenses = expenses
        self.participants = []

    def get_participants_from_expenses(self):
        for expense in self.expenses :         
            participant = self.__get_participant(expense.paymaster)
            if participant != None : 
                participant.balance += round(expense.price,2)
                if participant.balance > 0 : 
                    participant.participant_type = CREDITOR
            else : 
                new_participant  = Participant(expense.paymaster, expense.price, CREDITOR)
                self.participants.append(new_participant)
            for participant_expense in expense.participants : 
                participant_find = self.__get_participant(participant_expense)
                if participant_find != None : 
                    participant_find.balance -= round(expense.price / len(expense.participants), 2)
                    if participant_find.balance  < 0 : 
                        participant_find.participant_type = DEBTOR
                else : 
                    new_participant  = Participant(participant_expense, -round(expense.price / len(expense.participants), 2), DEBTOR)
                    self.participants.append(new_participant)
        
        return self.participants


    def __get_participant(self, name):
        participant_find = None 
        for participant in self.participants : 
            if participant.name == name : 
                participant_find = participant
                break
        return participant_find