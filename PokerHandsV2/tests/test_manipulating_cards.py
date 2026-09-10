import copy

from PokerHandsV2.card import Card, CardColor, CardValue
from PokerHandsV2.manipulating_cards import ManipulatingCards

def test_count_each_where_different_cards():
    (ManipulatingCardDriver()
            .add_all_cards_crypted(["Q♦", "J♥", "6♠", "A♣", "4♦"])
            .count_card()
            .is_valid_number_card("Q", "1")
            .is_valid_number_card("J", "1")
            .is_valid_number_card("6", "1")
            .is_valid_number_card("A", "1")            
            .is_valid_number_card("4", "1"))      

def test_count_each_where_two_same_cards(): 
    (ManipulatingCardDriver()
            .add_all_cards_crypted(["Q♦", "J♥", "6♠", "4♣", "Q♦"] )
            .count_card()
            .is_valid_number_card("Q", "2")
            .is_valid_number_card("J", "1")
            .is_valid_number_card("6", "1")
            .is_valid_number_card("4", "1"))   

def test_count_each_where_three_same_cards():
    (ManipulatingCardDriver()
                .add_all_cards_crypted(["A♦", "10♥", "A♠", "A♣", "6♦"])
                .count_card()
                .is_valid_number_card("A", "3")
                .is_valid_number_card("10", "1")
                .is_valid_number_card("6", "1"))

def test_count_each_where_fourth_same_cards():
    (ManipulatingCardDriver()
                    .add_all_cards_crypted(["Q♦", "Q♠", "Q♥", "A♦", "Q♣"])
                    .count_card()
                    .is_valid_number_card("Q", "4")
                    .is_valid_number_card("A", "1"))

def test_sorted_5_cards_following_each_other():
    (ManipulatingCardDriver()
                    .add_all_cards_crypted(["3♦", "4♥", "5♠", "6♣", "7♦"])
                    .sorted_card()
                    .is_valid_order(["3♦", "4♥", "5♠", "6♣", "7♦"]))

def test_sorted_5_differents_cards_in_opposite_order():
    (ManipulatingCardDriver()
                    .add_all_cards_crypted(["7♦", "6♣", "5♠", "4♥","3♦"])
                    .sorted_card()
                    .is_valid_order(["3♦", "4♥", "5♠", "6♣", "7♦"]))

def test_sorted_5_differents_cards_mixed_order():
    (ManipulatingCardDriver()
                        .add_all_cards_crypted(["6♣", "3♦", "5♠", "4♥", "7♦"])
                        .sorted_card()
                        .is_valid_order(["3♦", "4♥", "5♠", "6♣", "7♦"]))

def test_sorted_5_differents_cards_mixed_not_order():
    (ManipulatingCardDriver()
                            .add_all_cards_crypted(["K♣", "3♦", "A♠", "6♥", "10♦"])
                            .sorted_card()
                            .is_valid_order(["3♦", "6♥", "10♦", "K♣", "A♠"]))

def test_sorted_5_cards_some_with_same_values_mixed_not_order():
    (ManipulatingCardDriver()
                            .add_all_cards_crypted(["6♣", "3♦", "A♠", "6♥", "A♦"])
                            .sorted_card()
                            .is_valid_order(["3♦", "6♣", "6♥", "A♠", "A♦"]))

class ManipulatingCardDriver(): 
    def __init__(self):
        self.hand = []
        self.hand_ordered = []
        self.counting_card = {}
        self.manipulating_cards = ManipulatingCards()        

    def add_all_cards_crypted(self, all_cards_crypted):
        for card_crypted in all_cards_crypted : 
            card = Card.parse(card_crypted)
            self.hand.append(card)
        return self

    def count_card(self):
        self.counting_card =  self.manipulating_cards.count_cards(self.hand)
        return self

    def sorted_card(self): 
        self.hand_ordered = self.manipulating_cards.sorted_card(self.hand)
        return self

    def is_valid_number_card(self, card_value_crypted, number):
        is_valid = False
        for card_value in self.counting_card : 
            card_value_asked = Card.parse_value(card_value_crypted)
            if card_value == card_value_asked :
                occurency = self.counting_card[card_value]
                is_valid = occurency == int(number)
                break
        assert(is_valid == True)
        return self

    def is_valid_order(self, ordered_expected_crypted):
        ordered_expected = []
        for card_crypted in ordered_expected_crypted : 
            card = Card.parse(card_crypted)
            ordered_expected.append(card)
        is_valid_ordered = True
        for idx, card_expected in enumerate(ordered_expected):
            card = self.hand_ordered[int(idx)]
            is_valid_ordered = card.value == card_expected.value and card.color == card_expected.color
            if is_valid_ordered == False :
                break
        return is_valid_ordered