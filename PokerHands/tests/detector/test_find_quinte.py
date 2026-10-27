from PokerHands.card import Card
from PokerHands.manipulating_cards import ManipulatingCards
from PokerHands.AllFigures.QuinteFigure import QuinteFigure
from PokerHands.detector.quinte_detector import QuinteDetector

def test_find_quinte_finish_six():
    (
        QuinteDetectorDriver()
            .add_card_in_combination("2♣")
            .add_card_in_combination("6♦")
            .add_card_in_combination("4♥")
            .add_card_in_combination("5♠")
            .add_card_in_combination("3♠")
            .calculate_combination()
            .is_valid_quinte_figure("6")
    )

def test_find_quinte_finish_jack():
    (
        QuinteDetectorDriver()
            .add_card_in_combination("J♣")
            .add_card_in_combination("7♦")
            .add_card_in_combination("8♥")
            .add_card_in_combination("10♠")
            .add_card_in_combination("9♠")
            .calculate_combination()
            .is_valid_quinte_figure("J")
    )

def test_find_quinte_finish_ace():
    (
        QuinteDetectorDriver()
            .add_card_in_combination("A♣")
            .add_card_in_combination("K♦")
            .add_card_in_combination("10♥")
            .add_card_in_combination("Q♠")
            .add_card_in_combination("J♠")
            .calculate_combination()
            .is_valid_quinte_figure("A")
    )

def test_find_quinte_started_ace():
    (
        QuinteDetectorDriver()
            .add_card_in_combination("4♣")
            .add_card_in_combination("2♦")
            .add_card_in_combination("A♥")
            .add_card_in_combination("5♠")
            .add_card_in_combination("3♠")
            .calculate_combination()
            .is_valid_quinte_figure("5")
    )

def test_find_quinte_from_7_cards_from_texas_holdem_game():
    (
        QuinteDetectorDriver()
            .add_card_in_combination("K♠")
            .add_card_in_combination("Q♥")
            .add_card_in_combination("A♦")
            .add_card_in_combination("10♣")
            .add_card_in_combination("9♠")
            .add_card_in_combination("8♥")
            .add_card_in_combination("J♦")
            .calculate_combination()
            .is_valid_quinte_figure("A")
    )

def test_find_quinte_from_7_cards_from_texas_holdem_game_with_outside_cards():
    (
        QuinteDetectorDriver()
            .add_card_in_combination("Q♥")
            .add_card_in_combination("A♦")
            .add_card_in_combination("Q♠")            
            .add_card_in_combination("K♠")
            .add_card_in_combination("10♣")
            .add_card_in_combination("2♥")
            .add_card_in_combination("J♦")
            .calculate_combination()
            .is_valid_quinte_figure("A")
    )

def test_find_quinte_from_7_small_cards_from_texas_holdem_game_with_outside_cards():
    (
        QuinteDetectorDriver()
            .add_card_in_combination("3♥")
            .add_card_in_combination("6♦")
            .add_card_in_combination("Q♠")            
            .add_card_in_combination("5♠")
            .add_card_in_combination("10♣")
            .add_card_in_combination("2♥")
            .add_card_in_combination("4♦")
            .calculate_combination()
            .is_valid_quinte_figure("6")
    )

def test_find_quinte_from_7_started_finished_by_seven_and_two_wrongs_cards():
    (
        QuinteDetectorDriver()
            .add_card_in_combination("3♥")
            .add_card_in_combination("6♦")
            .add_card_in_combination("7♠")            
            .add_card_in_combination("5♠")
            .add_card_in_combination("10♣")
            .add_card_in_combination("2♥")
            .add_card_in_combination("4♦")
            .calculate_combination()
            .is_valid_quinte_figure("7")
    )

def test_find_quinte_from_7_started_with_double():
    (
        QuinteDetectorDriver()
            .add_card_in_combination("3♥")
            .add_card_in_combination("6♦")
            .add_card_in_combination("7♠")            
            .add_card_in_combination("5♠")
            .add_card_in_combination("6♣")
            .add_card_in_combination("2♥")
            .add_card_in_combination("4♦")
            .calculate_combination()
            .is_valid_quinte_figure("7")
    )

def test_cannot_find_quinte_from_7_started_with_double():
    (
        QuinteDetectorDriver()
            .add_card_in_combination("3♥")
            .add_card_in_combination("6♦")
            .add_card_in_combination("7♠")            
            .add_card_in_combination("5♠")
            .add_card_in_combination("6♣")
            .add_card_in_combination("2♥")
            .add_card_in_combination("K♦")
            .calculate_combination()
            .is_not_valid_quinte_figure()
    )

def test_cannot_find_quinte_from_7_contains_double():
    (
        QuinteDetectorDriver()
            .add_card_in_combination("3♥")
            .add_card_in_combination("Q♦")
            .add_card_in_combination("4♠")            
            .add_card_in_combination("4♣")
            .add_card_in_combination("5♣")
            .add_card_in_combination("6♥")
            .add_card_in_combination("K♦")
            .calculate_combination()
            .is_not_valid_quinte_figure()
    )

class QuinteDetectorDriver : 
    def __init__(self):
        self.combination = []
        self.quinte_figure = None

    def add_card_in_combination(self, card_crypted):
        card = Card.parse(card_crypted)
        self.combination.append(card)
        return self

    def calculate_combination(self):
        manipulating_cards = ManipulatingCards()
        quinte_detector = QuinteDetector(manipulating_cards)
        self.quinte_figure = quinte_detector.find_quinte(self.combination)
        return self

    def is_valid_quinte_figure(self, card_value_crypted):
        card_value = Card.parse_value(card_value_crypted)
        assert(QuinteFigure(card_value) == self.quinte_figure)

    def is_not_valid_quinte_figure(self): 
        assert(self.quinte_figure == None)
