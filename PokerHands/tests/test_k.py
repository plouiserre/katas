import pytest

from PokerHands.card import Card, CardColor, CardValue
from PokerHands.counting_cards import CountingCards
from PokerHands.detector.four_cards_detector import FourCardsDetector
from PokerHands.detector.flush_detector import FlushDetector
from PokerHands.detector.full_detector import FullDetector
from PokerHands.detector.high_card_detector import HighCardDetector
from PokerHands.detector.pair_detector import PairDetector
from PokerHands.detector.quinte_flush_detector import QuinteFlushDetector
from PokerHands.detector.straight_detector import StraightDetector
from PokerHands.detector.three_cards_detector import ThreeCardsDetector
from PokerHands.detector.two_pairs_detector import TwoPairsDetector
from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.exception.PlayerDoNotHaveCompleteHandException import PlayerDoNotHaveCompleteHandException
from PokerHands.hand import Hand
from PokerHands.score import Score
from PokerHands.winner import Winner

def test_1(): 
    player_with_better_hand = (DrawAndComparePlayersHandDriver()
                               .add_player("Steve")
                               .add_player("Natacha")
                               .draw_card_player("Steve")
                               .draw_card_player("Natacha")
                               .draw_card_player("Steve")
                               .draw_card_player("Natacha")
                               .determine_player_with_better_hand())
    assert(player_with_better_hand == Winner.FIRST_HAND or player_with_better_hand == Winner.SECOND_HAND or player_with_better_hand == Winner.EQUALITY)

def test_2(): 
    player_with_better_hand = (DrawAndComparePlayersHandDriver()
                                   .add_player("Steve")
                                   .add_player("Natacha")
                                   .give_specific_hand("Steve", [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)])                                   
                                   .give_specific_hand("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)])                                   
                                   .determine_player_with_better_hand())
    assert(player_with_better_hand == Winner.EQUALITY)

#TODO faire un test où les joueurs n'ont pas le bon nombre de carte en main
def test_3(): 
     with pytest.raises(PlayerDoNotHaveCompleteHandException) :
            (DrawAndComparePlayersHandDriver()
                               .add_player("Steve")
                               .add_player("Natacha")
                               .draw_card_player("Steve")
                               .draw_card_player("Natacha")
                               .draw_card_player("Natacha")
                               .determine_player_with_better_hand())

#TODO il faut que ce test pête un moment
def test_4(): 
    player_with_better_hand = (DrawAndComparePlayersHandDriver()
                               .add_player("Steve")
                               .add_player("Natacha")
                               .add_player("Tony")
                               .add_player("Thor")
                               .add_player("Bruce")
                               .add_player("Clint")
                               .draw_card_player("Steve")
                               .draw_card_player("Natacha")
                               .draw_card_player("Tony")
                               .draw_card_player("Thor")
                               .draw_card_player("Bruce")
                               .draw_card_player("Clint")
                               .draw_card_player("Steve")
                               .draw_card_player("Natacha")
                               .draw_card_player("Tony")
                               .draw_card_player("Thor")
                               .draw_card_player("Bruce")
                               .draw_card_player("Clint")
                               .determine_player_with_better_hand())
    assert(player_with_better_hand == Winner.FIRST_HAND or player_with_better_hand == Winner.SECOND_HAND or player_with_better_hand == Winner.THIRD_HAND 
           or player_with_better_hand == Winner.FOURTH_HAND or player_with_better_hand == Winner.FIFTH_HAND or player_with_better_hand == Winner.SIXTH_HAND)

def test_5():
    player_with_better_hand = (DrawAndComparePlayersHandDriver()
                                       .add_player("Steve")
                                       .add_player("Natacha")
                                       .add_player("Tony")
                                        .add_player("Thor")
                                        .add_player("Bruce")
                                        .add_player("Clint")                                        
                                       .give_specific_hand("Steve", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES)])                                        
                                       .give_specific_hand("Tony", [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Thor", [Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES)])                                        
                                       .give_specific_hand("Bruce", [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Clint", [Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SEVEN, CardColor.SPADES)])
                                       .determine_player_with_better_hand())
    assert(player_with_better_hand == Winner.FIRST_HAND)

def test_6():
    player_with_better_hand = (DrawAndComparePlayersHandDriver()
                                       .add_player("Steve")
                                       .add_player("Natacha")
                                       .add_player("Tony")
                                        .add_player("Thor")
                                        .add_player("Bruce")
                                        .add_player("Clint")                                        
                                       .give_specific_hand("Steve", [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES)])                                        
                                       .give_specific_hand("Tony", [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Thor", [Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES)])                                        
                                       .give_specific_hand("Bruce", [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Clint", [Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SEVEN, CardColor.SPADES)])
                                       .determine_player_with_better_hand())
    assert(player_with_better_hand == Winner.SECOND_HAND)

# def test_7():
#     player_with_better_hand = (DrawAndComparePlayersHandDriver()
#                                        .add_player("Steve")
#                                        .add_player("Natacha")
#                                        .add_player("Tony")
#                                        .add_player("Thor")
#                                        .add_player("Bruce")
#                                        .add_player("Clint")                                        
#                                        .give_specific_hand("Steve", [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)])                                   
#                                        .give_specific_hand("Natacha", [Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.SPADES)])                                        
#                                        .give_specific_hand("Tony", [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS)])                                   
#                                        .give_specific_hand("Thor", [Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES)])                                        
#                                        .give_specific_hand("Bruce", [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS)])                                   
#                                        .give_specific_hand("Clint", [Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SEVEN, CardColor.SPADES)])
#                                        .determine_player_with_better_hand())
#     assert(player_with_better_hand == Winner.THIRD_HAND)

class DrawAndComparePlayersHandDriver():
    def __init__(self):
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
        self.hand = Hand(high_card_detector, pair_detector, two_pairs_detector, three_cards_detector, straight_detector, flush_detector, full_detector, four_cards_detector, quinte_flush_detector)
        self.multi_draw_cards = MultiDrawCards()
        self.players = {}
        
    def add_player(self, name_player):
        self.players[name_player] = []
        return self

    def draw_card_player(self, name_player):
        new_card = self.multi_draw_cards.draw_one_card()
        self.players[name_player].append(new_card)
        return self

    def give_specific_hand(self, name_player, cards): 
        self.players[name_player] = cards
        return self

    def determine_player_with_better_hand(self):
        self.__check_all_players_have_all_their_cards()
        hands = []
        for player_name in self.players : 
            player = self.players[player_name]
            hand = self.hand.determinate_high_figure(player) 
            hands.append(hand)
        score = Score(hands)
        result = score.determinate_winner()
        return result

    def __check_all_players_have_all_their_cards(self): 
        for player_name in self.players : 
            if len(self.players[player_name]) < 2: 
                raise PlayerDoNotHaveCompleteHandException(player_name+" do not have his/hers 2 cards ")
