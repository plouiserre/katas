from PokerHands.counting_cards import CountingCards
from PokerHands.deck import Deck
from PokerHands.detector.four_cards_detector import FourCardsDetector
from PokerHands.detector.flush_detector import FlushDetector
from PokerHands.detector.full_detector import FullDetector
from PokerHands.detector.high_card_detector import HighCardDetector
from PokerHands.detector.pair_detector import PairDetector
from PokerHands.detector.quinte_flush_detector import QuinteFlushDetector
from PokerHands.detector.straight_detector import StraightDetector
from PokerHands.detector.three_cards_detector import ThreeCardsDetector
from PokerHands.detector.two_pairs_detector import TwoPairsDetector
from PokerHands.hand import Hand  
from PokerHands.player import Player
from PokerHands.score import Score
from PokerHands.winner import Winner
from unittest.mock import Mock

#  self.all_colors = ["♠", "♥", "♦", "♣"]
#     self.all_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
def test_1(): 
    deck = Deck()
    result_poker_game = __launched_poker_game(deck)
    assert( result_poker_game == Winner.FIRST_HAND or result_poker_game == Winner.SECOND_HAND
           or result_poker_game == Winner.EQUALITY)
    
def test_2(): 
    deck = Mock()
    deck.drawn_five_cards_for_the_two_players.return_value = [["9♠", "10♠", "J♠","Q♠","K♠"], ["3♥", "3♠", "3♦","7♠","8♠"]]

    result_poker_game = __launched_poker_game(deck)
    assert (Winner.FIRST_HAND, result_poker_game)


def test_3(): 
    deck = Mock()
    deck.drawn_five_cards_for_the_two_players.return_value = [["3♥", "3♠", "3♦","7♠","8♠"],["9♠", "10♠", "J♠","Q♠","K♠"]]

    result_poker_game = __launched_poker_game(deck)
    assert (Winner.SECOND_HAND, result_poker_game)

def test_4(): 
    deck = Mock()
    deck.drawn_five_cards_for_the_two_players.return_value = [["3♥", "3♠", "6♦","7♠","8♠"],["9♠", "10♠", "3♣","3♠","K♠"]]

    result_poker_game = __launched_poker_game(deck)
    assert (Winner.EQUALITY, result_poker_game)

def __launched_poker_game(deck):
    first_hand = __initiate_hand()
    second_hand = __initiate_hand()
    player_one = Player(first_hand)
    player_two = Player(second_hand)

    all_hands_cards = deck.drawn_five_cards_for_the_two_players()
    high_figure_first_hand = player_one.calculate_hand(all_hands_cards[0])
    high_figure_second_hand = player_two.calculate_hand(all_hands_cards[1])
    score = Score(high_figure_first_hand, high_figure_second_hand)
    return score.determinate_winner()

def __initiate_hand():
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
    return hand
