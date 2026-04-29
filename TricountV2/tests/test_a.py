from TricountV2.expense import Expense

DEBTOR = 0
CREDITOR = 0

class Participant :
    def __init__(self, name, balance, participant_type):
        self.name = name
        self.balance = balance
        self.participant_type = participant_type    

    def __eq__(self, other):
         return self.name == other.name and self.balance == other.balance and self.participant_type == other.participant_type

expenses = [Expense(65.2, "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"]), Expense(22.4, "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"]), 
                Expense(24.2, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), Expense(13.6, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), 
                Expense(9.1, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), Expense(106, "Donatello", ["Raphaël", "Léonardo","Michelangelo", "Donatello"]), 
                Expense(3.4, "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"]), Expense(6.8, "Michelangelo", ["Donatello","Raphaël", "Léonardo", "Michelangelo"]), 
                Expense(14.99, "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"])]

def test_1():   
    participant_name =  "Léonardo"
    assert(Participant(participant_name, 21.18, CREDITOR) == calculate_balance_and_participant_type(expenses, participant_name))

def test_2():   
    participant_name =  "Raphaël"
    assert(Participant(participant_name, -19.52, DEBTOR) == calculate_balance_and_participant_type(expenses, participant_name))

def calculate_balance_and_participant_type(expenses, participant_name):
        balance = 0
        participant_type = ""
        for expense in expenses : 
            if expense.paymaster == participant_name : 
                balance += expense.price
            for participant in expense.participants: 
                 if participant == participant_name : 
                      balance -= round(expense.price / len(expense.participants),2)
        if balance > 0 : 
             participant_type = CREDITOR
        else : 
              participant_type = DEBTOR
        return Participant(participant_name, round(balance,2), participant_type)

