from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.card import Card, CardValue
from PokerHands.manipulating_cards import ManipulatingCards
from PokerHands.detector.quinte_detector import QuinteDetector
from PokerHands.detector.quinte_flush_detector import QuinteFlushDetector
from PokerHands.tests.random_cards import get_all_values, get_random_card, get_colors_random, get_shuffle_combination, remove_cards

def test_find_quinte_flush_diamonds_with_nine_value():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_combination("9♦")
            .add_card_in_combination("7♦")
            .add_card_in_combination("8♦")
            .add_card_in_combination("6♦")
            .add_card_in_combination("5♦")
            .calculate_combination()
            .is_valid_quinte_flush_figure("9", "♦")
    )

def test_find_quinte_flush_spades_started_ace_value():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_combination("4♠")
            .add_card_in_combination("2♠")
            .add_card_in_combination("A♠")
            .add_card_in_combination("5♠")
            .add_card_in_combination("3♠")
            .calculate_combination()
            .is_valid_quinte_flush_figure("5", "♠")
    )

def test_find_quinte_flush_diamonds_from_texas_holdem_game():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_combination("K♦")
            .add_card_in_combination("Q♦")
            .add_card_in_combination("A♦")
            .add_card_in_combination("10♦")
            .add_card_in_combination("9♦")
            .add_card_in_combination("8♦")
            .add_card_in_combination("J♦")
            .calculate_combination()
            .is_valid_quinte_flush_figure("A", "♦")
    )

def test_find_quinte_flushs_from_7_cards_from_texas_holdem_game_with_outside_cards():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_combination("Q♣")
            .add_card_in_combination("A♣")
            .add_card_in_combination("Q♦")            
            .add_card_in_combination("K♣")
            .add_card_in_combination("10♣")
            .add_card_in_combination("2♣")
            .add_card_in_combination("J♣")
            .calculate_combination()
            .is_valid_quinte_flush_figure("A", "♣")
    )

def test_find_quinte_from_7_small_cards_from_texas_holdem_game_with_outside_cards():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_combination("3♥")
            .add_card_in_combination("6♥")
            .add_card_in_combination("Q♥")            
            .add_card_in_combination("5♥")
            .add_card_in_combination("10♥")
            .add_card_in_combination("2♥")
            .add_card_in_combination("4♥")
            .calculate_combination()
            .is_valid_quinte_flush_figure("6", "♥")
    )

def test_find_quinte_flush_from_7_started_finished_by_seven_and_two_wrongs_cards():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_combination("3♠")
            .add_card_in_combination("6♠")
            .add_card_in_combination("7♠")            
            .add_card_in_combination("5♠")
            .add_card_in_combination("10♠")
            .add_card_in_combination("2♠")
            .add_card_in_combination("4♠")
            .calculate_combination()
            .is_valid_quinte_flush_figure("7", "♠")
    )

def test_find_quinte_flush_from_7_started_with_double():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_combination("3♦")
            .add_card_in_combination("6♠")
            .add_card_in_combination("7♦")            
            .add_card_in_combination("5♦")
            .add_card_in_combination("6♦")
            .add_card_in_combination("2♦")
            .add_card_in_combination("4♦")
            .calculate_combination()
            .is_valid_quinte_flush_figure("7", "♦")
    )

def test_cannot_find_quinte_flush_from_7_started_with_double():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_combination("3♣")
            .add_card_in_combination("6♣")
            .add_card_in_combination("7♣")            
            .add_card_in_combination("5♣")
            .add_card_in_combination("6♣")
            .add_card_in_combination("2♣")
            .add_card_in_combination("K♣")
            .calculate_combination()
            .is_not_valid_quinte_flush_figure()
    )
    
def test_find_quinte_flush_from_7_started_finished_by_seven_and_two_wrongs_cards_with_no_good_number_and_color():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_combination("3♥")
            .add_card_in_combination("6♥")
            .add_card_in_combination("7♥")            
            .add_card_in_combination("5♥")
            .add_card_in_combination("10♠")
            .add_card_in_combination("2♣")
            .add_card_in_combination("4♥")
            .calculate_combination()
            .is_valid_quinte_flush_figure("7", "♥")
    )

def test_find_quinte_flush_from_7_started_finished_by_seven_and_fails_because_one_quinte_card_have_different_color():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_combination("3♥")
            .add_card_in_combination("6♥")
            .add_card_in_combination("7♥")            
            .add_card_in_combination("5♦")
            .add_card_in_combination("10♠")
            .add_card_in_combination("2♣")
            .add_card_in_combination("4♥")
            .calculate_combination()
            .is_not_valid_quinte_flush_figure()
    )

def test_cannot_find_quinte_flush_from_7_contains_double():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_combination("3♥")
            .add_card_in_combination("Q♥")
            .add_card_in_combination("4♥")            
            .add_card_in_combination("4♥")
            .add_card_in_combination("5♥")
            .add_card_in_combination("6♥")
            .add_card_in_combination("K♥")
            .calculate_combination()
            .is_not_valid_quinte_flush_figure()
    )

def test_find_quinte_flush_from_7_contains_double_in_second_place():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_combination("3♣")
            .add_card_in_combination("Q♣")
            .add_card_in_combination("4♣")            
            .add_card_in_combination("4♥")
            .add_card_in_combination("7♣")
            .add_card_in_combination("6♣")
            .add_card_in_combination("5♣")
            .calculate_combination()
            .is_valid_quinte_flush_figure("7", "♣")
    )

def test_find_quinte_flush_from_7_contains_double_in_middle_place():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_combination("3♠")
            .add_card_in_combination("Q♠")
            .add_card_in_combination("4♠")            
            .add_card_in_combination("5♠")
            .add_card_in_combination("7♠")
            .add_card_in_combination("6♠")
            .add_card_in_combination("5♦")
            .calculate_combination()
            .is_valid_quinte_flush_figure("7", "♠")
    )

def test_find_quinte_flush_from_7_contains_double_in_final_place():
    (
        QuinteFlushDetectorDriver()
            .add_card_in_combination("8♠")
            .add_card_in_combination("Q♦")
            .add_card_in_combination("4♦")            
            .add_card_in_combination("5♦")
            .add_card_in_combination("7♦")
            .add_card_in_combination("6♦")
            .add_card_in_combination("8♦")
            .calculate_combination()
            .is_valid_quinte_flush_figure("8", "♦")
    )
    
def test_find_quinte_flush_random_colors__with_six_value():
    color_value = get_colors_random()
    all_cards_values = get_all_values()
    remove_cards(all_cards_values, [CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE])
    top_quinte_flush = get_random_card(all_cards_values)
    second_card = top_quinte_flush - 1
    third_card = top_quinte_flush - 2
    fourth_card = top_quinte_flush - 3
    fifth_card = top_quinte_flush - 4
    combination = [Card(top_quinte_flush, color_value), Card(second_card, color_value), Card(third_card, color_value), Card(fourth_card, color_value), Card(fifth_card, color_value)]
    get_shuffle_combination(combination)
    assert(__find_quinte_flush(combination) == QuinteFlushFigure(top_quinte_flush, color_value))

def __find_quinte_flush(combination):
    manipulating_cards = ManipulatingCards()
    quinte_detector = QuinteDetector(manipulating_cards)
    quinte_flush_detector = QuinteFlushDetector(manipulating_cards, quinte_detector)
    return quinte_flush_detector.find_quinte_flush(combination)

class QuinteFlushDetectorDriver : 
    def __init__(self):
        self.combination = []
        self.quinte_flush_figure = None

    def add_card_in_combination(self, card_crypted):
        card = Card.parse(card_crypted)
        self.combination.append(card)
        return self
    
    def calculate_combination(self):
        manipulating_cards = ManipulatingCards()
        quinte_detector = QuinteDetector(manipulating_cards)
        quinte_flush_detector = QuinteFlushDetector(manipulating_cards, quinte_detector)
        self.quinte_flush_figure = quinte_flush_detector.find_quinte_flush(self.combination)
        return self

    def is_valid_quinte_flush_figure(self, card_value_crypted, card_color_crypted):
        card_value = Card.parse_value(card_value_crypted)
        card_color = Card.parse_color(card_color_crypted)
        assert(QuinteFlushFigure(card_value, card_color) == self.quinte_flush_figure)

    def is_not_valid_quinte_flush_figure(self): 
        assert(self.quinte_flush_figure == None) 