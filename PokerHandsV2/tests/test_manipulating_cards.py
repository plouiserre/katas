import copy

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

#♦♥♠♣
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



#TODO tests à faire 
# 1 - tout de suits dans l'ordre 
# 2 - tout se suit dans le désordre 
# 3 - tout se suit mélangé
# 4 - des trous
# 5 - plusieurs cartes avec la même valeur

class ManipulatingCardDriver(): 
    def __init__(self):
        self.hand = []
        self.hand_ordered = []
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

    def sorted_card(self): 
        all_cards = copy.deepcopy(self.hand)
        self.hand_ordered = []
        while(len(self.hand_ordered) < len(all_cards)) :
            min_card = Card(CardValue.UNDEFINED, CardColor.UNDEFINED)
            for idx, card_in_hand in enumerate(self.hand) : 
                card = self.hand[idx]
                if min_card == Card(CardValue.UNDEFINED, CardColor.UNDEFINED) :
                    min_card = card
                    continue
                else : 
                    if min_card.value > card.value : 
                        min_card = card
            self.hand_ordered.append(min_card)
            self.hand.remove(min_card) 
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