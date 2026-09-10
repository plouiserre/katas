from PokerHandsV2.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHandsV2.card import Card, CardValue
from PokerHandsV2.manipulating_cards import ManipulatingCards
from PokerHandsV2.detector.quinte_detector import QuinteDetector
from PokerHandsV2.detector.quinte_flush_detector import QuinteFlushDetector
from PokerHandsV2.tests.random_cards import get_all_values, get_random_card, get_colors_random, get_shuffle_hand, remove_cards

def test_find_quinte_flush_diamonds_with_nine_value():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_hand("9♦")
            .add_card_in_hand("7♦")
            .add_card_in_hand("8♦")
            .add_card_in_hand("6♦")
            .add_card_in_hand("5♦")
            .calculate_hand()
            .is_valid_quinte_flush_figure("9", "♦")
    )

def test_find_quinte_flush_spades_started_ace_value():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_hand("4♠")
            .add_card_in_hand("2♠")
            .add_card_in_hand("A♠")
            .add_card_in_hand("5♠")
            .add_card_in_hand("3♠")
            .calculate_hand()
            .is_valid_quinte_flush_figure("5", "♠")
    )

def test_find_quinte_flush_diamonds_from_texas_holdem_game():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_hand("K♦")
            .add_card_in_hand("Q♦")
            .add_card_in_hand("A♦")
            .add_card_in_hand("10♦")
            .add_card_in_hand("9♦")
            .add_card_in_hand("8♦")
            .add_card_in_hand("J♦")
            .calculate_hand()
            .is_valid_quinte_flush_figure("A", "♦")
    )

#à la fin faire un test parfait complexe mais y a une couleur qui n'est pas commune
    
def test_find_quinte_flush_random_colors__with_six_value():
    color_value = get_colors_random()
    all_cards_values = get_all_values()
    remove_cards(all_cards_values, [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE])
    top_quinte_flush = get_random_card(all_cards_values)
    second_card = top_quinte_flush - 1
    third_card = top_quinte_flush - 2
    fourth_card = top_quinte_flush - 3
    fifth_card = top_quinte_flush - 4
    hand = [Card(top_quinte_flush, color_value), Card(second_card, color_value), Card(third_card, color_value), Card(fourth_card, color_value), Card(fifth_card, color_value)]
    get_shuffle_hand(hand)
    assert(__find_quinte_flush(hand) == QuinteFlushFigure(top_quinte_flush, color_value))

def __find_quinte_flush(hand):
    manipulating_cards = ManipulatingCards()
    quinte_detector = QuinteDetector(manipulating_cards)
    quinte_flush_detector = QuinteFlushDetector(manipulating_cards, quinte_detector)
    return quinte_flush_detector.find_quinte_flush(hand)

class QuinteFlushDetectorDriver : 
    def __init__(self):
        self.hand = []
        self.quinte_flush_figure = None

    def add_card_in_hand(self, card_crypted):
        card = Card.parse(card_crypted)
        self.hand.append(card)
        return self
    
    def calculate_hand(self):
        manipulating_cards = ManipulatingCards()
        quinte_detector = QuinteDetector(manipulating_cards)
        quinte_flush_detector = QuinteFlushDetector(manipulating_cards, quinte_detector)
        self.quinte_flush_figure = quinte_flush_detector.find_quinte_flush(self.hand)
        return self

    def is_valid_quinte_flush_figure(self, card_value_crypted, card_color_crypted):
        card_value = Card.parse_value(card_value_crypted)
        card_color = Card.parse_color(card_color_crypted)
        assert(QuinteFlushFigure(card_value, card_color) == self.quinte_flush_figure)

    def is_not_valid_quinte_figure(self): 
        assert(self.quinte_flush_figure == None) 