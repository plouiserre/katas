from PokerHandsV2.card import Card
from PokerHandsV2.manipulating_cards import ManipulatingCards
from PokerHandsV2.AllFigures.QuinteFigure import QuinteFigure
from PokerHandsV2.detector.quinte_detector import QuinteDetector

def test_find_quinte_finish_six():
    (
        QuinteDetectorDriver()
            .add_card_in_hand("2♣")
            .add_card_in_hand("6♦")
            .add_card_in_hand("4♥")
            .add_card_in_hand("5♠")
            .add_card_in_hand("3♠")
            .calculate_hand()
            .is_valid_quinte_figure("6")
    )

def test_find_quinte_finish_jack():
    (
        QuinteDetectorDriver()
            .add_card_in_hand("J♣")
            .add_card_in_hand("7♦")
            .add_card_in_hand("8♥")
            .add_card_in_hand("10♠")
            .add_card_in_hand("9♠")
            .calculate_hand()
            .is_valid_quinte_figure("J")
    )

def test_find_quinte_finish_ace():
    (
        QuinteDetectorDriver()
            .add_card_in_hand("A♣")
            .add_card_in_hand("K♦")
            .add_card_in_hand("10♥")
            .add_card_in_hand("Q♠")
            .add_card_in_hand("J♠")
            .calculate_hand()
            .is_valid_quinte_figure("A")
    )

def test_find_quinte_started_ace():
    (
        QuinteDetectorDriver()
            .add_card_in_hand("4♣")
            .add_card_in_hand("2♦")
            .add_card_in_hand("A♥")
            .add_card_in_hand("5♠")
            .add_card_in_hand("3♠")
            .calculate_hand()
            .is_valid_quinte_figure("5")
    )

def test_find_quinte_from_7_cards_from_texas_holdem_game():
    (
        QuinteDetectorDriver()
            .add_card_in_hand("K♠")
            .add_card_in_hand("Q♥")
            .add_card_in_hand("A♦")
            .add_card_in_hand("10♣")
            .add_card_in_hand("9♠")
            .add_card_in_hand("8♥")
            .add_card_in_hand("J♦")
            .calculate_hand()
            .is_valid_quinte_figure("A")
    )

def test_find_quinte_from_7_cards_from_texas_holdem_game_with_outside_cards():
    (
        QuinteDetectorDriver()
            .add_card_in_hand("Q♥")
            .add_card_in_hand("A♦")
            .add_card_in_hand("Q♠")            
            .add_card_in_hand("K♠")
            .add_card_in_hand("10♣")
            .add_card_in_hand("2♥")
            .add_card_in_hand("J♦")
            .calculate_hand()
            .is_valid_quinte_figure("A")
    )

def test_find_quinte_from_7_small_cards_from_texas_holdem_game_with_outside_cards():
    (
        QuinteDetectorDriver()
            .add_card_in_hand("3♥")
            .add_card_in_hand("6♦")
            .add_card_in_hand("Q♠")            
            .add_card_in_hand("5♠")
            .add_card_in_hand("10♣")
            .add_card_in_hand("2♥")
            .add_card_in_hand("4♦")
            .calculate_hand()
            .is_valid_quinte_figure("6")
    )

def test_find_quinte_from_7_started_finished_by_seven_and_two_wrongs_cards():
    (
        QuinteDetectorDriver()
            .add_card_in_hand("3♥")
            .add_card_in_hand("6♦")
            .add_card_in_hand("7♠")            
            .add_card_in_hand("5♠")
            .add_card_in_hand("10♣")
            .add_card_in_hand("2♥")
            .add_card_in_hand("4♦")
            .calculate_hand()
            .is_valid_quinte_figure("7")
    )

def test_find_quinte_from_7_started_with_double():
    (
        QuinteDetectorDriver()
            .add_card_in_hand("3♥")
            .add_card_in_hand("6♦")
            .add_card_in_hand("7♠")            
            .add_card_in_hand("5♠")
            .add_card_in_hand("6♣")
            .add_card_in_hand("2♥")
            .add_card_in_hand("4♦")
            .calculate_hand()
            .is_valid_quinte_figure("7")
    )

def test_cannot_find_quinte_from_7_started_with_double():
    (
        QuinteDetectorDriver()
            .add_card_in_hand("3♥")
            .add_card_in_hand("6♦")
            .add_card_in_hand("7♠")            
            .add_card_in_hand("5♠")
            .add_card_in_hand("6♣")
            .add_card_in_hand("2♥")
            .add_card_in_hand("K♦")
            .calculate_hand()
            .is_not_valid_quinte_figure()
    )

class QuinteDetectorDriver : 
    def __init__(self):
        self.hand = []
        self.quinte_figure = None

    def add_card_in_hand(self, card_crypted):
        card = Card.parse(card_crypted)
        self.hand.append(card)
        return self

    def calculate_hand(self):
        manipulating_cards = ManipulatingCards()
        quinte_detector = QuinteDetector(manipulating_cards)
        self.quinte_figure = quinte_detector.find_quinte(self.hand)
        return self

    def is_valid_quinte_figure(self, card_value_crypted):
        card_value = Card.parse_value(card_value_crypted)
        assert(QuinteFigure(card_value) == self.quinte_figure)

    def is_not_valid_quinte_figure(self): 
        assert(self.quinte_figure == None)
