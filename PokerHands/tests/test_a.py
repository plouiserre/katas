from PokerHands.AllFigures.FlushFigure import FlushFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.detector.high_card_detector import HighCardDetector
from PokerHands.detector.pair_detector import PairDetector
from PokerHands.detector.two_pairs_detector import TwoPairsDetector
from PokerHands.detector.three_cards_detector import ThreeCardsDetector
from PokerHands.detector.straight_detector import StraightDetector
from PokerHands.detector.flush_detector import FlushDetector
from PokerHands.detector.full_detector import FullDetector
from PokerHands.detector.four_cards_detector import FourCardsDetector
from PokerHands.detector.quinte_flush_detector import QuinteFlushDetector
from PokerHands.hand import Hand
from PokerHands.player import Player

def test_1():
    hand_content = "7♠ K♥ 3♦ K♦ K♠"

    assert(ThreeOfKindFigure(CardValue.KING, CardValue.SEVEN) == read_hand(hand_content))

def test_2():
    hand_content = "K♣ 7♣ 3♣ A♣ 2♣"

    assert(FlushFigure(CardColor.CLUBS, CardValue.ACE) == read_hand(hand_content))

def test_3(): 
    hand_content = "Q♣ 6♦ K♦ 6♠ Q♠"

    assert(TwoPairFigure(CardValue.QUEEN, CardValue.SIX, CardValue.KING) == read_hand(hand_content)
           or TwoPairFigure(CardValue.SIX, CardValue.QUEEN, CardValue.KING) == read_hand(hand_content))


def read_hand(hand_content):
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
    player = Player(hand)
    high_figure = player.calculate_hand(hand_content)
    return high_figure