from PokerHands.AllFigures.FlushFigure import FlushFigure
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure
from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.AllFigures.QuinteFigure import QuinteFigure
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.card import CardColor, CardValue
from PokerHands.player.compare_hand import CompareHand

def test_1():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", HighCardFigure(CardValue.JACK))
        .add_hand("Natacha", HighCardFigure(CardValue.QUEEN))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_2():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", PairFigure(CardValue.ACE, CardValue.FIVE))
        .add_hand("Natacha", PairFigure(CardValue.QUEEN, CardValue.EIGHT))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_3():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", PairFigure(CardValue.QUEEN, CardValue.FIVE))
        .add_hand("Natacha", PairFigure(CardValue.QUEEN, CardValue.EIGHT))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_4():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", TwoPairFigure(CardValue.KING, CardValue.THREE, CardValue.FOUR))
        .add_hand("Natacha", TwoPairFigure(CardValue.QUEEN, CardValue.FIVE, CardValue.ACE))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_5():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", TwoPairFigure(CardValue.TEN, CardValue.THREE, CardValue.FOUR))
        .add_hand("Natacha", TwoPairFigure(CardValue.QUEEN, CardValue.FIVE, CardValue.ACE))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_6():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", TwoPairFigure(CardValue.QUEEN, CardValue.JACK, CardValue.FOUR))
        .add_hand("Natacha", TwoPairFigure(CardValue.QUEEN, CardValue.FIVE, CardValue.ACE))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_7():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", TwoPairFigure(CardValue.QUEEN, CardValue.THREE, CardValue.FOUR))
        .add_hand("Natacha", TwoPairFigure(CardValue.QUEEN, CardValue.FIVE, CardValue.ACE))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_8():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", TwoPairFigure(CardValue.QUEEN, CardValue.THREE, CardValue.KING))
        .add_hand("Natacha", TwoPairFigure(CardValue.QUEEN, CardValue.THREE, CardValue.FOUR))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_9():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", TwoPairFigure(CardValue.QUEEN, CardValue.THREE, CardValue.KING))
        .add_hand("Natacha", TwoPairFigure(CardValue.QUEEN, CardValue.THREE, CardValue.FOUR))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_10():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", ThreeOfKindFigure(CardValue.QUEEN, CardValue.KING))
        .add_hand("Natacha", ThreeOfKindFigure(CardValue.JACK, CardValue.FOUR))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_11():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", ThreeOfKindFigure(CardValue.SIX, CardValue.THREE))
        .add_hand("Natacha", ThreeOfKindFigure(CardValue.QUEEN, CardValue.FOUR))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_12():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", ThreeOfKindFigure(CardValue.QUEEN, CardValue.KING))
        .add_hand("Natacha", ThreeOfKindFigure(CardValue.QUEEN, CardValue.FOUR))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_13():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", ThreeOfKindFigure(CardValue.QUEEN, CardValue.THREE))
        .add_hand("Natacha", ThreeOfKindFigure(CardValue.QUEEN, CardValue.FOUR))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_14():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", QuinteFigure(CardValue.KING))
        .add_hand("Natacha", QuinteFigure(CardValue.QUEEN))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_15():
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", QuinteFigure(CardValue.SIX))
        .add_hand("Natacha", QuinteFigure(CardValue.QUEEN))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_16(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", FlushFigure(CardColor.CLUBS, CardValue.KING))
        .add_hand("Natacha", FlushFigure(CardColor.DIAMONDS, CardValue.QUEEN))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_17(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", FlushFigure(CardColor.CLUBS, CardValue.KING))
        .add_hand("Natacha", FlushFigure(CardColor.DIAMONDS, CardValue.ACE))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_18(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", FourOfKindFigure(CardValue.KING, CardValue.SIX))
        .add_hand("Natacha", FourOfKindFigure(CardValue.QUEEN, CardValue.SEVEN))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_19(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", FourOfKindFigure(CardValue.JACK, CardValue.SIX))
        .add_hand("Natacha", FourOfKindFigure(CardValue.QUEEN, CardValue.SEVEN))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_20(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", FourOfKindFigure(CardValue.KING, CardValue.QUEEN))
        .add_hand("Natacha", FourOfKindFigure(CardValue.KING, CardValue.SEVEN))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_21(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", FourOfKindFigure(CardValue.QUEEN, CardValue.SIX))
        .add_hand("Natacha", FourOfKindFigure(CardValue.QUEEN, CardValue.SEVEN))
        .determinate_winners()
        .check_winner_name("Natacha"))

def test_22(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", QuinteFlushFigure(CardValue.KING, CardColor.CLUBS))
        .add_hand("Natacha", QuinteFlushFigure(CardValue.QUEEN, CardColor.HEARTS))
        .determinate_winners()
        .check_winner_name("Steve"))

def test_23(): 
    (Driver()
        .add_player("Steve")
        .add_player("Natacha")
        .add_hand("Steve", QuinteFlushFigure(CardValue.EIGHT, CardColor.CLUBS))
        .add_hand("Natacha", QuinteFlushFigure(CardValue.QUEEN, CardColor.HEARTS))
        .determinate_winners()
        .check_winner_name("Natacha"))

class Driver(): 
    def __init__(self):
        self.players = []
        self.hand_players = {}
        self.result = None
        self.winner = ""

    def add_player(self, name_player): 
        self.players.append(name_player)
        return self

    def add_hand(self, name_player, hand): 
        self.hand_players[name_player] = hand
        return self

    def determinate_winners(self):
        compare_hand = CompareHand(self.players, self.hand_players) 
        self.result = compare_hand.get_players_with_best_hands()
        return self

    def check_winner_name(self, winner_name): 
        is_ok = winner_name in self.result.winners
        assert(is_ok == True)