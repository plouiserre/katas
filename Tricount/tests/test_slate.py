from Tricount.expense import Expense
from Tricount.refund import Refund
from Tricount.slate import Slate

def test_manage_bob_and_tome_expenses(): 
    first_expense = Expense(45, "bob", ["tom", "bob"])
    second_expense = Expense(32.6, "bob", ["tom", "bob"])
    third_expense = Expense(24, "bob", ["tom", "bob"])
    fourth_expense = Expense(9.99, "tom", ["bob", "tom"])
    fifth_expense = Expense(3.54, "tom", ["bob", "tom"])
    sixth_expense = Expense(41.2, "tom", ["bob", "tom"])
    seventh_expense = Expense(6.35, "tom", ["bob", "tom"])
    eighth_expense = Expense(24.3, "tom", ["bob", "tom"])
    nineth_expense = Expense(6.66, "tom", ["bob", "tom"])
    tenth_expense = Expense(1.01, "tom", ["bob", "tom"])
    expenses = [first_expense, second_expense, third_expense, fourth_expense, fifth_expense, 
                sixth_expense, seventh_expense, eighth_expense, nineth_expense, tenth_expense]
    refund = Refund("tom", "bob", 4.27)
    refunds = [refund]
    are_refunds_equals(refunds, expenses)

def test_manage_amandhi_and_feng_expenses(): 
    first_expense = Expense(9.66, "amandhi", ["feng", "amandhi"])
    second_expense = Expense(3.24, "amandhi", ["feng", "amandhi"])
    third_expense = Expense(6.2, "amandhi", ["feng", "amandhi"])
    fourth_expense = Expense(4.35, "feng", ["amandhi", "feng"])
    fifth_expense = Expense(28.9, "feng", ["amandhi", "feng"])
    expenses = [first_expense, second_expense, third_expense, fourth_expense, fifth_expense]
    refund = Refund("amandhi", "feng", 7.07)
    refunds = [refund]
    are_refunds_equals(refunds, expenses)

def test_manage_three_friends_expenses_simple(): 
    expenses = { "Newton": [321.12,2.65,78.66], "Darwin": [466.98], "Einstein":[123.6,241.98,196.7]}
    first_expense = Expense(321.12, "Newton", ["Einstein","Darwin", "Newton"])
    second_expense = Expense(2.65, "Newton", ["Einstein","Darwin", "Newton"])
    third_expense = Expense(78.66, "Newton", ["Einstein","Darwin", "Newton"])
    fourth_expense = Expense(466.98, "Darwin", ["Newton", "Einstein", "Darwin"])
    fifth_expense = Expense(123.6, "Einstein", ["Darwin", "Newton", "Einstein"])
    sixth_expense = Expense(241.98, "Einstein", ["Darwin", "Newton", "Einstein"])
    seventh_expense = Expense(196.7, "Einstein", ["Darwin", "Newton", "Einstein"])
    expenses = [first_expense, second_expense, third_expense, fourth_expense, fifth_expense, sixth_expense, seventh_expense]
    first_refund = Refund("Newton", "Einstein", 74.8)
    second_refund = Refund("Darwin", "Einstein", 10.25)
    refunds = [first_refund, second_refund]
    are_refunds_equals(refunds, expenses)

def test_manage_four_friends_expenses_simple(): 
    first_expense = Expense(65.2, "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"])
    second_expense = Expense(22.4, "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"])
    third_expense = Expense(24.2, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"])
    fourth_expense = Expense(13.6, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"])
    fifth_expense = Expense(9.1, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"])
    sixth_expense = Expense(106, "Donatello", ["Raphaël", "Léonardo","Michelangelo", "Donatello"])
    seventh_expense = Expense(3.4, "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"])
    eighth_expense = Expense(6.8, "Michelangelo", ["Donatello","Raphaël", "Léonardo", "Michelangelo"])
    nineth_expense = Expense(14.99, "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"])
    expenses = [first_expense, second_expense, third_expense, fourth_expense, fifth_expense, 
                sixth_expense, seventh_expense, eighth_expense, nineth_expense]
    first_refund = Refund("Michelangelo", "Donatello", 39.58)
    second_refund = Refund("Michelangelo", "Léonardo", 1.65)
    third_refund = Refund("Raphaël", "Léonardo", 19.52)
    refunds = [first_refund, second_refund, third_refund]
    are_refunds_equals(refunds, expenses)

def are_refunds_equals(expected_refunds, expenses):
    refunds = manage_expense(expenses)
    for idx, refund in enumerate(refunds):
        assert(refund == expected_refunds[idx])

def manage_expense(expenses):
    slate = Slate(expenses)
    return slate.manage_expenses()   