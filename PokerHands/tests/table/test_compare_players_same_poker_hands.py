from PokerHands.AllFigures.FlushFigure import FlushFigure
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure
from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.AllFigures.QuinteFigure import QuinteFigure
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.card import CardColor, CardValue
from PokerHands.table.compare_combination import CompareCombination

def test_compare_two_combination_with_high_card_figure_and_natacha_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", HighCardFigure(CardValue.JACK))
        .add_combination("Natacha", HighCardFigure(CardValue.QUEEN))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_compare_two_combination_with_pair_figure_and_steve_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", PairFigure(CardValue.ACE, CardValue.FIVE))
        .add_combination("Natacha", PairFigure(CardValue.QUEEN, CardValue.EIGHT))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_compare_two_combination_with_pair_figure_and_natacha_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", PairFigure(CardValue.QUEEN, CardValue.FIVE))
        .add_combination("Natacha", PairFigure(CardValue.QUEEN, CardValue.EIGHT))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_compare_two_combination_with_two_pair_figure_with_differents_pairs_and_steve_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", TwoPairFigure(CardValue.KING, CardValue.THREE, CardValue.FOUR))
        .add_combination("Natacha", TwoPairFigure(CardValue.QUEEN, CardValue.FIVE, CardValue.ACE))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_compare_two_combination_with_two_pair_figure_with_differents_pairs_and_natacha_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", TwoPairFigure(CardValue.TEN, CardValue.THREE, CardValue.FOUR))
        .add_combination("Natacha", TwoPairFigure(CardValue.QUEEN, CardValue.FIVE, CardValue.ACE))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_compare_two_combination_with_two_pair_figure_with_same_first_pair_and_steve_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", TwoPairFigure(CardValue.QUEEN, CardValue.JACK, CardValue.FOUR))
        .add_combination("Natacha", TwoPairFigure(CardValue.QUEEN, CardValue.FIVE, CardValue.ACE))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_compare_two_combination_with_two_pair_figure_with_same_first_pair_and_natacha_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", TwoPairFigure(CardValue.QUEEN, CardValue.THREE, CardValue.FOUR))
        .add_combination("Natacha", TwoPairFigure(CardValue.QUEEN, CardValue.FIVE, CardValue.ACE))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_compare_two_combination_with_two_pair_figure_with_same_pairs_and_steve_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", TwoPairFigure(CardValue.QUEEN, CardValue.THREE, CardValue.KING))
        .add_combination("Natacha", TwoPairFigure(CardValue.QUEEN, CardValue.THREE, CardValue.FOUR))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_compare_two_combination_with_two_pair_figure_with_same_pairs_and_natacha_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", TwoPairFigure(CardValue.QUEEN, CardValue.THREE, CardValue.TWO))
        .add_combination("Natacha", TwoPairFigure(CardValue.QUEEN, CardValue.THREE, CardValue.FOUR))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_compare_two_combination_with_three_of_kinds_figure_and_steve_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", ThreeOfKindFigure(CardValue.QUEEN, CardValue.KING))
        .add_combination("Natacha", ThreeOfKindFigure(CardValue.JACK, CardValue.FOUR))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_compare_two_combination_with_three_of_kinds_figure_and_natacha_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", ThreeOfKindFigure(CardValue.SIX, CardValue.THREE))
        .add_combination("Natacha", ThreeOfKindFigure(CardValue.QUEEN, CardValue.FOUR))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_compare_two_combination_with_three_of_kinds_figure_with_same_three_cards_and_steve_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", ThreeOfKindFigure(CardValue.QUEEN, CardValue.KING))
        .add_combination("Natacha", ThreeOfKindFigure(CardValue.QUEEN, CardValue.FOUR))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_compare_two_combination_with_three_of_kinds_figure_with_same_three_cards_and_natacha_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", ThreeOfKindFigure(CardValue.QUEEN, CardValue.THREE))
        .add_combination("Natacha", ThreeOfKindFigure(CardValue.QUEEN, CardValue.FOUR))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_compare_two_combination_with_quinte_and_steve_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", QuinteFigure(CardValue.KING))
        .add_combination("Natacha", QuinteFigure(CardValue.QUEEN))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_compare_two_combination_with_quinte_and_natacha_wins():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", QuinteFigure(CardValue.SIX))
        .add_combination("Natacha", QuinteFigure(CardValue.QUEEN))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_compare_two_combination_with_flush_and_steve_wins(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", FlushFigure(CardColor.CLUBS, CardValue.KING))
        .add_combination("Natacha", FlushFigure(CardColor.DIAMONDS, CardValue.QUEEN))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_compare_two_combination_with_flush_and_natacha_wins(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", FlushFigure(CardColor.CLUBS, CardValue.KING))
        .add_combination("Natacha", FlushFigure(CardColor.DIAMONDS, CardValue.ACE))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_compare_two_combination_with_four_of_a_kind_and_steve_wins(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", FourOfKindFigure(CardValue.KING, CardValue.SIX))
        .add_combination("Natacha", FourOfKindFigure(CardValue.QUEEN, CardValue.SEVEN))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_compare_two_combination_with_four_of_a_kind_and_natacha_wins(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", FourOfKindFigure(CardValue.JACK, CardValue.SIX))
        .add_combination("Natacha", FourOfKindFigure(CardValue.QUEEN, CardValue.SEVEN))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_compare_two_combination_with_four_of_a_kind_with_same_four_cards_and_steve_wins(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", FourOfKindFigure(CardValue.KING, CardValue.QUEEN))
        .add_combination("Natacha", FourOfKindFigure(CardValue.KING, CardValue.SEVEN))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_compare_two_combination_with_four_of_a_kind_with_same_four_cards_and_natacha_wins(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", FourOfKindFigure(CardValue.QUEEN, CardValue.SIX))
        .add_combination("Natacha", FourOfKindFigure(CardValue.QUEEN, CardValue.SEVEN))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_compare_two_combination_with_quinte_flush_and_steve_wins(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", QuinteFlushFigure(CardValue.KING, CardColor.CLUBS))
        .add_combination("Natacha", QuinteFlushFigure(CardValue.QUEEN, CardColor.HEARTS))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_compare_two_combination_with_quinte_flush_and_natacha_wins(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_combination("Steve", QuinteFlushFigure(CardValue.EIGHT, CardColor.CLUBS))
        .add_combination("Natacha", QuinteFlushFigure(CardValue.QUEEN, CardColor.HEARTS))
        .determinate_winners()
        .check_winner_name("Natacha"))

class Driver(): 
    def __init__(self):
        self.players = []
        self.combination_players = {}
        self.result = None
        self.winner = ""

    def add_player(self, name_player): 
        self.players.append(name_player)
        return self

    def add_combination(self, name_player, round): 
        self.combination_players[name_player] = round
        return self

    def determinate_winners(self):
        compare_hand = CompareCombination(self.players, self.combination_players) 
        self.result = compare_hand.get_players_with_best_combination()
        return self

    def check_winner_name(self, winner_name): 
        is_ok = winner_name in self.result.winners
        assert(is_ok == True)