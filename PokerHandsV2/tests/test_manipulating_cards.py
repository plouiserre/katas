from PokerHandsV2.card import Card, CardColor, CardValue
from PokerHandsV2.manipulating_cards import ManipulatingCards

def test_count_each_where_different_cards():
    (ManipulatingCardDriver()
            .add_all_cards_crypted(["Q♦", "J♥", "6♠", "A♣", "4♦"])
            .count_card()
            .validate_number_card("Q", "1")
            .validate_number_card("J", "1")
            .validate_number_card("6", "1")
            .validate_number_card("A", "1")            
            .validate_number_card("4", "1"))      

def test_count_each_where_two_same_cards(): 
    (ManipulatingCardDriver()
            .add_all_cards_crypted(["Q♦", "J♥", "6♠", "4♣", "Q♦"] )
            .count_card()
            .validate_number_card("Q", "2")
            .validate_number_card("J", "1")
            .validate_number_card("6", "1")
            .validate_number_card("4", "1"))   

def test_count_each_where_three_same_cards():
    (ManipulatingCardDriver()
                .add_all_cards_crypted(["A♦", "10♥", "A♠", "A♣", "6♦"])
                .count_card()
                .validate_number_card("A", "3")
                .validate_number_card("10", "1")
                .validate_number_card("6", "1"))

def test_count_each_where_fourth_same_cards():
    (ManipulatingCardDriver()
                    .add_all_cards_crypted(["Q♦", "Q♠", "Q♥", "A♦", "Q♣"])
                    .count_card()
                    .validate_number_card("Q", "4")
                    .validate_number_card("A", "1"))

class ManipulatingCardDriver(): 
    def __init__(self):
        self.hand = []
        self.counting_card = {}        

    def add_all_cards_crypted(self, all_cards_crypted):
        for card_crypted in all_cards_crypted : 
            card = Card.parse(card_crypted)
            self.hand.append(card)
        return self

    def count_card(self):
        manipulating_cards = ManipulatingCards()
        self.counting_card =  manipulating_cards.Count(self.hand)
        return self

    def validate_number_card(self, card_value_crypted, number):
        is_valid = False
        for card_value in self.counting_card : 
            card_value_asked = Card.parse_value(card_value_crypted)
            if card_value == card_value_asked :
                occurency = self.counting_card[card_value]
                is_valid = occurency == int(number)
                break
        assert(is_valid == True)
        return self