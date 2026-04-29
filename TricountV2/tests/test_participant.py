from TricountV2.expense import Expense
from TricountV2.participant import CREDITOR, DEBTOR, Participant

expenses = [Expense(65.2, "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"]), Expense(22.4, "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"]), 
                Expense(24.2, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), Expense(13.6, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), 
                Expense(9.1, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), Expense(106, "Donatello", ["Raphaël", "Léonardo","Michelangelo", "Donatello"]), 
                Expense(3.4, "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"]), Expense(6.8, "Michelangelo", ["Donatello","Raphaël", "Léonardo", "Michelangelo"]), 
                Expense(14.99, "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"])]

def test_calculate_leonardo_balance_and_define_participant_type():   
    participant_name =  "Léonardo"
    assert(__build_participant(participant_name, 21.18, CREDITOR) == __calculate_balance_and_participant_type(expenses, participant_name))

def test_calculate_raphael_balance_and_define_participant_type():   
    participant_name =  "Raphaël"
    assert(__build_participant(participant_name, -19.52, DEBTOR) == __calculate_balance_and_participant_type(expenses, participant_name))

def __build_participant(participant_name, balance, participant_type): 
     participant = Participant()
     participant.name = participant_name
     participant.balance = balance
     participant.participant_type = participant_type
     return participant

def __calculate_balance_and_participant_type(expenses, participant_name):
        participant = Participant()
        participant.determinate_all_datas_participant_from_expenses(participant_name, expenses)
        return participant

