from TricountV2.expense import Expense
from TricountV2.refund import Refund
from TricountV2.slate import Slate

def test_manage_bob_and_tome_expenses(): 
    expenses = [Expense(45, "bob", ["tom", "bob"]), Expense(32.6, "bob", ["tom", "bob"]), Expense(24, "bob", ["tom", "bob"]), 
                Expense(9.99, "tom", ["bob", "tom"]), Expense(3.54, "tom", ["bob", "tom"]), Expense(41.2, "tom", ["bob", "tom"]), 
                Expense(6.35, "tom", ["bob", "tom"]), Expense(24.3, "tom", ["bob", "tom"]), Expense(6.66, "tom", ["bob", "tom"]), 
                Expense(1.01, "tom", ["bob", "tom"])]
    refunds = [Refund("tom", "bob", 4.27)]
    are_refunds_equals(refunds, expenses)

def test_manage_amandhi_and_feng_expenses(): 
    expenses = [Expense(9.66, "amandhi", ["feng", "amandhi"]), Expense(3.24, "amandhi", ["feng", "amandhi"]), Expense(6.2, "amandhi", ["feng", "amandhi"]), 
                Expense(4.35, "feng", ["amandhi", "feng"]), Expense(28.9, "feng", ["amandhi", "feng"])]
    refunds = [Refund("amandhi", "feng", 7.07)]
    are_refunds_equals(refunds, expenses)

def test_manage_three_friends_expenses_simple(): 
    expenses = [Expense(321.12, "Newton", ["Einstein","Darwin", "Newton"]), Expense(2.65, "Newton", ["Einstein","Darwin", "Newton"]), 
                Expense(78.66, "Newton", ["Einstein","Darwin", "Newton"]), Expense(466.98, "Darwin", ["Newton", "Einstein", "Darwin"]), 
                Expense(123.6, "Einstein", ["Darwin", "Newton", "Einstein"]), Expense(241.98, "Einstein", ["Darwin", "Newton", "Einstein"]), 
                Expense(196.7, "Einstein", ["Darwin", "Newton", "Einstein"])]
    refunds = [Refund("Newton", "Einstein", 74.8), Refund("Darwin", "Einstein", 10.25)]
    are_refunds_equals(refunds, expenses)

def test_manage_four_friends_expenses_simple(): 
    expenses = [Expense(65.2, "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"]), Expense(22.4, "Léonardo", ["Michelangelo", "Donatello", "Raphaël", "Léonardo"]), 
                Expense(24.2, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), Expense(13.6, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), 
                Expense(9.1, "Raphaël", ["Léonardo","Michelangelo", "Donatello", "Raphaël"]), Expense(106, "Donatello", ["Raphaël", "Léonardo","Michelangelo", "Donatello"]), 
                Expense(3.4, "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"]), Expense(6.8, "Michelangelo", ["Donatello","Raphaël", "Léonardo", "Michelangelo"]), 
                Expense(14.99, "Michelangelo", ["Donatello", "Raphaël", "Léonardo", "Michelangelo"])]
    refunds = [Refund("Michelangelo", "Donatello", 39.58), Refund("Michelangelo", "Léonardo", 1.65), Refund("Raphaël", "Léonardo", 19.52)]
    are_refunds_equals(refunds, expenses)

def test_manage_five_friends_complexes(): 
    expenses = [Expense(12.3, "Jordan", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"]), Expense(98.5, "Johnson", ["Jordan", "Johnson", "Pippen"]), 
                Expense(146.9, "Bird", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"]), Expense(49.4, "Barkley",["Bird", "Barkley", "Pippen"]), 
                Expense(75.6, "Pippen", ["Jordan", "Johnson", "Bird", "Barkley", "Pippen"]), Expense(186.6, "Jordan", ["Jordan", "Barkley", "Pippen"])]
    first_refund = Refund("Pippen", "Bird", 82.86)
    third_refund = Refund("Barkley", "Jordan", 56.91)
    fourth_refund = Refund("Barkley", "Johnson", 18.71)
    refunds = [first_refund, third_refund, fourth_refund]
    are_refunds_equals(refunds, expenses)
    

def are_refunds_equals(expected_refunds, expenses):
    slate = Slate(expenses)    
    refunds = slate.manage_expenses()
    for idx, refund in enumerate(refunds):
        assert(refund == expected_refunds[idx])