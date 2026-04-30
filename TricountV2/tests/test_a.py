from TricountV2.expense import Expense
from TricountV2.participant import CREDITOR, DEBTOR, Participant

def test_get_ninja_turtles_participants_from_expenses():
    expenses = [Expense(65.2, "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"]), Expense(22.4, "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"]), 
                Expense(24.2, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), Expense(13.6, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), 
                Expense(9.1, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), Expense(106, "Donatello", ["Raphaël", "Léonardo","Michelangelo", "Donatello"]), 
                Expense(3.4, "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"]), Expense(6.8, "Michelangelo", ["Donatello","Raphaël", "Léonardo", "Michelangelo"]), 
                Expense(14.99, "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"])]
    assert (__get_participants(expenses) == [Participant("Léonardo", 21.18, CREDITOR), Participant("Michelangelo", -41.23, DEBTOR) , Participant("Donatello", 39.58, CREDITOR), 
                                             Participant("Raphaël", -19.52, DEBTOR)])    
def test_get_dream_team_participants_from_expenses():
    expenses = [Expense(12.3, "Jordan", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"]), Expense(98.5, "Johnson", ["Jordan", "Johnson", "Pippen"]), 
                Expense(146.9, "Bird", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"]), Expense(49.4, "Barkley",["Bird", "Barkley", "Pippen"]), 
                Expense(75.6, "Pippen", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"]), Expense(186.6, "Jordan", ["Jordan", "Barkley", "Pippen"])]
    assert (__get_participants(expenses) == [Participant("Jordan", 56.91, CREDITOR), Participant("Johnson", 18.71, CREDITOR) , Participant("Bird", 83.47, CREDITOR), 
                                             Participant("Barkley", -76.23, DEBTOR), Participant("Pippen", -82.86, DEBTOR)])  

#     first_refund = Refund("Pippen", "Bird", 82.86)
#     third_refund = Refund("Barkley", "Jordan", 56.91)
#     fourth_refund = Refund("Barkley", "Johnson", 18.71)
#     refunds = [first_refund, third_refund, fourth_refund]
#     are_refunds_equals(refunds, expenses)

def __get_participants(expenses):
    participants = []
    for expense in expenses :         
        participant = __get_participant(expense.paymaster, participants)
        if participant != None : 
            participant.balance += round(expense.price,2)
            if participant.balance > 0 : 
                participant.participant_type = CREDITOR
        else : 
            new_participant  = Participant(expense.paymaster, expense.price, CREDITOR)
            participants.append(new_participant)
        for participant_expense in expense.participants : 
            participant_find = __get_participant(participant_expense, participants)
            if participant_find != None : 
                participant_find.balance -= round(expense.price / len(expense.participants), 2)
                if participant_find.balance  < 0 : 
                    participant_find.participant_type = DEBTOR
            else : 
                new_participant  = Participant(participant_expense, -round(expense.price / len(expense.participants), 2), DEBTOR)
                participants.append(new_participant)
    return participants


def __get_participant(name, participants):
    participant_find = None 
    for participant in participants : 
        if participant.name == name : 
            participant_find = participant
            break
    return participant_find