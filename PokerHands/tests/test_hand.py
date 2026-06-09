from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.hand import Hand
from PokerHands.Figure import HighCardFigure, PairFigure, TwoPairFigure, ThreeOfKindFigure, StraitFigure, FlushFigure, FullFigure, FourOfKindFigure, QuinteFlush
from PokerHands.detector.full_detector import FullDetector
from PokerHands.detector.flush_detector import FlushDetector
from PokerHands.detector.four_cards_detector import FourCardsDetector
from PokerHands.detector.high_card_detector import HighCardDetector
from PokerHands.detector.pair_detector import PairDetector
from PokerHands.detector.quinte_flush_detector import QuinteFlushDetector
from PokerHands.detector.straight_detector import StraightDetector
from PokerHands.detector.two_pairs_detector import TwoPairsDetector
from PokerHands.detector.three_cards_detector import ThreeCardsDetector

def test_find_high_card_ace(): 
    hand = [Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.FOUR, CardColor.DIAMONDS)]
    assert(HighCardFigure(CardValue.ACE) == __find_high_figure(hand))

def test_find_one_pair_figure_before_high_card(): 
    hand = [Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.JACK, CardColor.HEARTS), Card(CardValue.SIX, CardColor.SPADES), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)]
    assert(PairFigure(CardValue.QUEEN, CardValue.JACK) == __find_high_figure(hand))

def test_find_two_pair_two_three_before_one_pair(): 
    hand = [Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.FOUR, CardColor.CLUBS), Card(CardValue.THREE, CardColor.DIAMONDS)]
    assert(TwoPairFigure(CardValue.THREE, CardValue.TWO, CardValue.FOUR) == __find_high_figure(hand))

def test_find_one_three_of_kind_figure_before_one_pair(): 
    hand = [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)]
    assert(ThreeOfKindFigure(CardValue.ACE, CardValue.TEN) == __find_high_figure(hand))

def test_find_straight_finish_by_six(): 
    hand = [Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.HEARTS), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
    assert(StraitFigure(CardValue.SIX) == __find_high_figure(hand))

def test_find_straight_begin_by_ace(): 
    hand = [Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.ACE, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
    assert(StraitFigure(CardValue.FIVE) == __find_high_figure(hand))

def test_find_flush_diamonds_by_ace():
    hand = [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.THREE, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.DIAMONDS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FIVE, CardColor.DIAMONDS)]
    assert(FlushFigure(CardColor.DIAMONDS, CardValue.ACE) == __find_high_figure(hand))    

def test_find_full_ace_two_times_queen_three_times_before_find_one_pair_or_three_kind_of_card():
    hand = [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.DIAMONDS)]
    assert(FullFigure(CardValue.ACE, CardValue.QUEEN) == __find_high_figure(hand))   

def test_find_four_of_kind_queen_with_ace_high_cards_before_two_pairs():
    hand = [Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.DIAMONDS)]
    assert(FourOfKindFigure(CardValue.QUEEN, CardValue.ACE) == __find_high_figure(hand))

def test_find_quinte_flush_spades_finished_by_ace_value():
    hand = [Card(CardValue.JACK, CardColor.SPADES), Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.KING, CardColor.SPADES), Card(CardValue.TEN, CardColor.SPADES)]
    assert(QuinteFlush(CardValue.ACE, CardColor.SPADES) == __find_high_figure(hand))

def test_find_quinte_flush_spades_started_by_ace_value():
    hand = [Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.THREE, CardColor.SPADES)]
    assert(QuinteFlush(CardValue.FIVE, CardColor.SPADES) == __find_high_figure(hand))

def __find_high_figure(content) : 
    counting_cards = CountingCards()
    high_card_detector = HighCardDetector()
    pair_detector = PairDetector(counting_cards)
    two_pairs_detector = TwoPairsDetector(counting_cards)
    three_cards_detector = ThreeCardsDetector(counting_cards)
    straight_detector = StraightDetector(counting_cards)
    flush_detector = FlushDetector()
    full_detector = FullDetector(counting_cards)
    four_cards_detector = FourCardsDetector(counting_cards)
    quinte_flush_detector = QuinteFlushDetector()
    hand = Hand(high_card_detector, pair_detector, two_pairs_detector, three_cards_detector, straight_detector, flush_detector, full_detector, four_cards_detector, quinte_flush_detector)
    figure =  hand.determinate_high_figure(content) 
    return figure 