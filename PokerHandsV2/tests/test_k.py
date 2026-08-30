import pytest

from PokerHands.card import Card, CardColor, CardValue
from PokerHands.AllFigures.Figure import Figure
from PokerHandsV2.AllFigures.HighCardFigure import HighCardFigure
from PokerHandsV2.AllFigures.PairFigure import PairFigure
from PokerHandsV2.counting_cards import CountingCards
from PokerHandsV2.detector.four_cards_detector import FourCardsDetector
from PokerHandsV2.detector.flush_detector import FlushDetector
from PokerHandsV2.detector.full_detector import FullDetector
from PokerHandsV2.detector.high_card_detector import HighCardDetector
from PokerHandsV2.detector.pair_detector import PairDetector
from PokerHandsV2.detector.quinte_flush_detector import QuinteFlushDetector
from PokerHandsV2.detector.straight_detector import StraightDetector
from PokerHandsV2.detector.three_cards_detector import ThreeCardsDetector
from PokerHandsV2.detector.two_pairs_detector import TwoPairsDetector
from PokerHandsV2.draw.multi_draw_cards import MultiDrawCards
from PokerHandsV2.exception.PlayerDoNotHaveCompleteHandException import PlayerDoNotHaveCompleteHandException
from PokerHandsV2.exception.TooManyPlayerException import TooManyPlayerException
from PokerHandsV2.hand import Hand
from PokerHandsV2.winner import Winner

def test_1(): 
    player_with_better_hand = (DrawAndComparePlayersHandDriver()
                               .add_player("Steve")
                               .add_player("Natacha")
                               .draw_card_player("Steve")
                               .draw_card_player("Natacha")
                               .draw_card_player("Steve")
                               .draw_card_player("Natacha")
                               .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Steve"] or player_with_better_hand == ["Natacha"] or player_with_better_hand == ["Steve", "Natacha"])

def test_2(): 
    player_with_better_hand = (DrawAndComparePlayersHandDriver()
                                   .add_player("Steve")
                                   .add_player("Natacha")
                                   .give_specific_hand("Steve", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)])                                   
                                   .give_specific_hand("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.SEVEN, CardColor.SPADES)])                                   
                                   .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Steve"])

def test_3(): 
    player_with_better_hand = (DrawAndComparePlayersHandDriver()
                                   .add_player("Steve")
                                   .add_player("Natacha")
                                   .give_specific_hand("Steve", [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS)])                                   
                                   .give_specific_hand("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.SEVEN, CardColor.SPADES)])                                   
                                   .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Natacha"])

def test_4(): 
    player_with_better_hand = (DrawAndComparePlayersHandDriver()
                                   .add_player("Steve")
                                   .add_player("Natacha")
                                   .give_specific_hand("Steve", [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)])                                   
                                   .give_specific_hand("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)])                                   
                                   .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Steve", "Natacha"])

def test_5(): 
     with pytest.raises(PlayerDoNotHaveCompleteHandException) :
            (DrawAndComparePlayersHandDriver()
                               .add_player("Steve")
                               .add_player("Natacha")
                               .draw_card_player("Steve")
                               .draw_card_player("Natacha")
                               .draw_card_player("Natacha")
                               .determine_player_with_better_hand())

def test_6(): 
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
    assert("Steve" in  player_with_better_hand or "Natacha" in  player_with_better_hand or "Tony" in  player_with_better_hand 
           or "Thor" in  player_with_better_hand  or "Bruce" in  player_with_better_hand  or "Clint" in  player_with_better_hand )

def test_7():
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
    assert(player_with_better_hand == ["Steve"])

def test_8():
    player_with_better_hand = (DrawAndComparePlayersHandDriver()
                                       .add_player("Steve")
                                       .add_player("Natacha")
                                       .add_player("Tony")
                                        .add_player("Thor")
                                        .add_player("Bruce")
                                        .add_player("Clint")                                        
                                       .give_specific_hand("Steve", [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Natacha", [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS)])                                        
                                       .give_specific_hand("Tony", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES)])                                   
                                       .give_specific_hand("Thor", [Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES)])                                        
                                       .give_specific_hand("Bruce", [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Clint", [Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SEVEN, CardColor.SPADES)])
                                       .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Tony"])

def test_9():
    player_with_better_hand = (DrawAndComparePlayersHandDriver()
                                       .add_player("Steve")
                                       .add_player("Natacha")
                                       .add_player("Tony")
                                       .add_player("Thor")
                                       .add_player("Bruce")
                                       .add_player("Clint")                                        
                                       .give_specific_hand("Steve", [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Natacha", [Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.SPADES)])                                        
                                       .give_specific_hand("Tony", [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Thor", [Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES)])                                        
                                       .give_specific_hand("Bruce", [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Clint", [Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.ACE , CardColor.SPADES)])
                                       .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Clint"])

def test_10(): 
    player_with_better_hand = (DrawAndComparePlayersHandDriver()
                                           .add_player("Steve")
                                           .add_player("Natacha")
                                           .add_player("Tony")
                                           .add_player("Thor")
                                           .add_player("Bruce")
                                           .add_player("Clint")                                        
                                           .give_specific_hand("Steve", [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)])                                   
                                           .give_specific_hand("Natacha", [Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)])                                        
                                           .give_specific_hand("Tony", [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS)])                                   
                                           .give_specific_hand("Thor", [Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES)])                                        
                                           .give_specific_hand("Bruce", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)])                                   
                                           .give_specific_hand("Clint", [Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.FOUR , CardColor.SPADES)])
                                           .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Natacha", "Bruce"])

def test_11(): 
    player_with_better_hand = (DrawAndComparePlayersHandDriver()
                                           .add_player("Steve")
                                           .add_player("Natacha")
                                           .add_player("Tony")
                                           .add_player("Thor")
                                           .add_player("Bruce")
                                           .add_player("Clint")
                                           .add_player("Carol")
                                           .add_player("T'Challa")
                                           .add_player("Steven")
                                           .add_player("Wanda")
                                           .draw_card_player("Steve")
                                           .draw_card_player("Natacha")
                                           .draw_card_player("Tony")
                                           .draw_card_player("Thor")
                                           .draw_card_player("Bruce")
                                           .draw_card_player("Clint")
                                           .draw_card_player("Carol")
                                           .draw_card_player("T'Challa")
                                           .draw_card_player("Steven")
                                           .draw_card_player("Wanda")
                                           .draw_card_player("Steve")
                                           .draw_card_player("Natacha")
                                           .draw_card_player("Tony")
                                           .draw_card_player("Thor")
                                           .draw_card_player("Bruce")
                                           .draw_card_player("Clint")
                                           .draw_card_player("Carol")
                                           .draw_card_player("T'Challa")
                                           .draw_card_player("Steven")
                                           .draw_card_player("Wanda")
                                           .determine_player_with_better_hand())
    assert("Steve" in  player_with_better_hand or "Natacha" in  player_with_better_hand or "Tony" in  player_with_better_hand 
           or "Thor" in  player_with_better_hand  or "Bruce" in  player_with_better_hand  or "Clint" in  player_with_better_hand 
           or "Carol" in player_with_better_hand or "T'Challa" in player_with_better_hand or "Steven" in player_with_better_hand
           or "Peter" in player_with_better_hand or "Wanda" in player_with_better_hand)

def test_12(): 
    player_with_better_hand = (DrawAndComparePlayersHandDriver()
                                           .add_player("Steve")
                                           .add_player("Natacha")
                                           .add_player("Tony")
                                           .add_player("Thor")
                                           .add_player("Bruce")
                                           .add_player("Clint")
                                           .add_player("Carol")
                                           .add_player("T'Challa")
                                           .add_player("Steven")
                                           .add_player("Wanda")
                                           .give_specific_hand("Steve", [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)])                                   
                                           .give_specific_hand("Natacha", [Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)])                                        
                                           .give_specific_hand("Tony", [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS)])                                   
                                           .give_specific_hand("Thor", [Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES)])                                        
                                           .give_specific_hand("Bruce", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)])                                   
                                           .give_specific_hand("Clint", [Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.FOUR , CardColor.SPADES)])                                  
                                           .give_specific_hand("Carol", [Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.ACE , CardColor.SPADES)])                                 
                                           .give_specific_hand("T'Challa", [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.QUEEN , CardColor.SPADES)])                              
                                           .give_specific_hand("Steven", [Card(CardValue.THREE, CardColor.SPADES), Card(CardValue.FOUR , CardColor.CLUBS)])                          
                                           .give_specific_hand("Wanda", [Card(CardValue.KING, CardColor.SPADES), Card(CardValue.KING , CardColor.DIAMONDS)])
                                           .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Carol"])

def test_13(): 
    with pytest.raises(TooManyPlayerException) :
        (DrawAndComparePlayersHandDriver()
                .add_player("Steve")
                .add_player("Natacha")
                .add_player("Tony")
                .add_player("Thor")
                .add_player("Bruce")
                .add_player("Clint")
                .add_player("Carol")
                .add_player("T'Challa")
                .add_player("Steven")
                .add_player("Peter")
                .add_player("Wanda")
                .give_specific_hand("Steve", [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)])                                   
                .give_specific_hand("Natacha", [Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)])                                        
                .give_specific_hand("Tony", [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS)])                                   
                .give_specific_hand("Thor", [Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES)])                                        
                .give_specific_hand("Bruce", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)])                                   
                .give_specific_hand("Clint", [Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.FOUR , CardColor.SPADES)])                                  
                .give_specific_hand("Carol", [Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.ACE , CardColor.SPADES)])                                 
                .give_specific_hand("T'Challa", [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.QUEEN , CardColor.SPADES)])                              
                .give_specific_hand("Steven", [Card(CardValue.THREE, CardColor.SPADES), Card(CardValue.FOUR , CardColor.CLUBS)])                            
                .give_specific_hand("Peter", [Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.SIX , CardColor.CLUBS)])                          
                .give_specific_hand("Wanda", [Card(CardValue.KING, CardColor.SPADES), Card(CardValue.KING , CardColor.DIAMONDS)])    
                .determine_player_with_better_hand())

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
        self.__check_not_too_many_players()
        hands_by_player = {}
        best_hand = None
        best_players = []
        for player_name in self.players : 
            player = self.players[player_name]
            hand = self.hand.determinate_high_figure(player) 
            hands_by_player[player_name] = hand
        for player_name in hands_by_player : 
            hand = hands_by_player[player_name]
            if best_hand == None : 
                best_hand = hand
                continue
            hands_to_compare = [hand, best_hand]
            winner = self.__determinate_winner(hands_to_compare)
            if winner == Winner.FIRST_HAND :
                best_hand = hand
        for player_name in hands_by_player : 
            hand = hands_by_player[player_name] 
            if best_hand == hand : 
                best_players.append(player_name)
        return best_players

    def __determinate_winner(self, hands : list[Figure] ): 
        first_hand = hands[0]
        second_hand = hands[1]
        if first_hand.points < second_hand.points : 
            return Winner.SECOND_HAND
        elif second_hand.points < first_hand.points : 
            return Winner.FIRST_HAND
        elif type(first_hand) is HighCardFigure and type(second_hand) is HighCardFigure:
            return self.__compare_two_hands_with_high_cards(first_hand, second_hand)
        elif type(first_hand) is PairFigure and type(second_hand) is PairFigure: 
            return self.__compare_two_hands_with_pairs(first_hand, second_hand)

    def __compare_two_hands_with_high_cards(self, first_hand : Hand, second_hand : Hand) -> Winner: 
            if first_hand.value < second_hand.value : 
                return Winner.SECOND_HAND
            elif second_hand.value < first_hand.value : 
                return Winner.FIRST_HAND 
            else :
                return Winner.EQUALITY
            
    def __compare_two_hands_with_pairs(self, first_hand : Hand, second_hand : Hand) -> Winner:
        if first_hand.value < second_hand.value : 
            return Winner.SECOND_HAND
        elif second_hand.value < first_hand.value : 
            return Winner.FIRST_HAND
        else : 
            if first_hand.high_value_rest_of_cards < second_hand.high_value_rest_of_cards : 
                return Winner.SECOND_HAND
            elif second_hand.high_value_rest_of_cards < first_hand.high_value_rest_of_cards :
                return Winner.FIRST_HAND
            else : 
                return Winner.EQUALITY

    def __check_all_players_have_all_their_cards(self): 
        for player_name in self.players : 
            if len(self.players[player_name]) < 2: 
                raise PlayerDoNotHaveCompleteHandException(player_name+" do not have his/hers 2 cards ")
            
    def __check_not_too_many_players(self): 
        if len(self.players) > 10 : 
            raise TooManyPlayerException("You cannot have more than ten players for a game.")
