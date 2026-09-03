import pytest

from PokerHands.card import Card, CardColor, CardValue
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
from PokerHandsV2.game.hands_manager import HandsManager

def test_two_players_compare_random_hands_after_drawn(): 
    player_with_better_hand = (HandManagerDriver()
                               .add_players(["Steve","Natacha"])    
                               .players_draw_first_card(["Steve", "Natacha"])
                               .players_draw_second_card(["Steve", "Natacha"])
                               .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Steve"] or player_with_better_hand == ["Natacha"] or player_with_better_hand == ["Steve", "Natacha"])

def test_two_players_compare_specific_hands_after_drawn_and_steve_win(): 
    player_with_better_hand = (HandManagerDriver()
                                   .add_players(["Steve","Natacha"])    
                                   .give_specific_hand("Steve", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)])                                   
                                   .give_specific_hand("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.SEVEN, CardColor.SPADES)])                                   
                                   .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Steve"])

def test_two_players_compare_specific_hands_after_drawn_and_natacha_win(): 
    player_with_better_hand = (HandManagerDriver()
                                   .add_players(["Steve","Natacha"])    
                                   .give_specific_hand("Steve", [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.JACK, CardColor.DIAMONDS)])                                   
                                   .give_specific_hand("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.SEVEN, CardColor.SPADES)])                                   
                                   .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Natacha"])

def test_two_players_compare_specific_hands_after_drawn_and_no_one_win(): 
    player_with_better_hand = (HandManagerDriver()
                                   .add_players(["Steve","Natacha"])    
                                   .give_specific_hand("Steve", [Card(CardValue.QUEEN, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)])                                   
                                   .give_specific_hand("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)])                                   
                                   .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Steve", "Natacha"])

def test_failing_two_players_compare_hands_because_steve_do_not_have_two_cards(): 
     with pytest.raises(PlayerDoNotHaveCompleteHandException) :
            (HandManagerDriver()
                               .add_players(["Steve","Natacha"])                                                                          
                               .players_draw_first_card(["Steve","Natacha"])
                               .players_draw_second_card(["Natacha"])                                                              
                               .determine_player_with_better_hand())

def test_six_players_compare_random_hands_after_drawn(): 
    player_with_better_hand = (HandManagerDriver()
                               .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])                                                                          
                               .players_draw_first_card(["Steve","Natacha","Tony","Thor","Bruce","Clint"])
                               .players_draw_second_card(["Steve","Natacha","Tony","Thor","Bruce","Clint"])
                               .determine_player_with_better_hand())
    assert("Steve" in  player_with_better_hand or "Natacha" in  player_with_better_hand or "Tony" in  player_with_better_hand 
           or "Thor" in  player_with_better_hand  or "Bruce" in  player_with_better_hand  or "Clint" in  player_with_better_hand )

def test_six_players_compare_specific_hands_after_drawn_and_steve_win():
    player_with_better_hand = (HandManagerDriver()
                                       .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])                                                                                                                        
                                       .give_specific_hand("Steve", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES)])                                        
                                       .give_specific_hand("Tony", [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Thor", [Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES)])                                        
                                       .give_specific_hand("Bruce", [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Clint", [Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SEVEN, CardColor.SPADES)])
                                       .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Steve"])

def test_six_players_compare_specific_hands_after_drawn_and_tony_win():
    player_with_better_hand = (HandManagerDriver()
                                       .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])                                                                                                                      
                                       .give_specific_hand("Steve", [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Natacha", [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS)])                                        
                                       .give_specific_hand("Tony", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.JACK, CardColor.SPADES)])                                   
                                       .give_specific_hand("Thor", [Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES)])                                        
                                       .give_specific_hand("Bruce", [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Clint", [Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.SEVEN, CardColor.SPADES)])
                                       .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Tony"])

def test_six_players_compare_specific_hands_after_drawn_and_clint_win():
    player_with_better_hand = (HandManagerDriver()
                                       .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])
                                       .give_specific_hand("Steve", [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Natacha", [Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.SPADES)])                                        
                                       .give_specific_hand("Tony", [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Thor", [Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES)])                                        
                                       .give_specific_hand("Bruce", [Card(CardValue.NINE, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.DIAMONDS)])                                   
                                       .give_specific_hand("Clint", [Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.ACE , CardColor.SPADES)])
                                       .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Clint"])

def test_six_players_compare_specific_hands_after_drawn_and_natacha_and_bruce_win(): 
    player_with_better_hand = (HandManagerDriver()
                                           .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])
                                           .give_specific_hand("Steve", [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)])                                   
                                           .give_specific_hand("Natacha", [Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)])                                        
                                           .give_specific_hand("Tony", [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS)])                                   
                                           .give_specific_hand("Thor", [Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES)])                                        
                                           .give_specific_hand("Bruce", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)])                                   
                                           .give_specific_hand("Clint", [Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.FOUR , CardColor.SPADES)])
                                           .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Natacha", "Bruce"])

def test_ten_players_compare_random_hands_after_drawn(): 
    player_with_better_hand = (HandManagerDriver()
                                    .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                                    .players_draw_first_card(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])                                    
                                    .players_draw_second_card(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                                    .determine_player_with_better_hand())
    assert("Steve" in  player_with_better_hand or "Natacha" in  player_with_better_hand or "Tony" in  player_with_better_hand 
           or "Thor" in  player_with_better_hand  or "Bruce" in  player_with_better_hand  or "Clint" in  player_with_better_hand 
           or "Carol" in player_with_better_hand or "T'Challa" in player_with_better_hand or "Steven" in player_with_better_hand
           or "Peter" in player_with_better_hand or "Wanda" in player_with_better_hand)

def test_six_players_compare_specific_hands_after_drawn_and_wanda_win(): 
    player_with_better_hand = (HandManagerDriver()
                                .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
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

def test_failing_because_more_ten_players(): 
    with pytest.raises(TooManyPlayerException) :
        (HandManagerDriver()
                .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Peter","Wanda"])
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

def test_if_it_is_not_flush_with_one_player_have_two_cards_the_same_colors_but_not_five():
    player_with_better_hand = (HandManagerDriver()
                                    .add_players(["Steve","Natacha"])    
                                    .give_specific_hand("Steve", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.JACK, CardColor.CLUBS)])                                   
                                    .give_specific_hand("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)])                                   
                                    .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Natacha"])

def test_if_it_is_not_flush_with_one_player_have_two_cards_the_same_colors_and_they_follow_each_other_but_not_five():
    player_with_better_hand = (HandManagerDriver()
                                    .add_players(["Steve","Natacha"])    
                                    .give_specific_hand("Steve", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.CLUBS)])                                   
                                    .give_specific_hand("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)])                                   
                                    .determine_player_with_better_hand())
    assert(player_with_better_hand == ["Natacha"])

class HandManagerDriver():
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
        hand = Hand(high_card_detector, pair_detector, two_pairs_detector, three_cards_detector, straight_detector, flush_detector, full_detector, four_cards_detector, quinte_flush_detector)
        self.players = {}
        multi_draw_cards = MultiDrawCards()
        self.hands_manager = HandsManager(hand, multi_draw_cards)
        
    def add_players(self, name_players):
        for name_player in name_players:
            self.hands_manager.add_player(name_player)
        return self

    def draw_card_player(self, name_player):
        self.hands_manager.draw_card_player(name_player)
        return self

    def players_draw_first_card(self, name_players):
        for name_player in name_players : 
            self.hands_manager.draw_card_player(name_player)
        return self

    def players_draw_second_card(self, name_players):
        for name_player in name_players : 
            self.hands_manager.draw_card_player(name_player)
        return self

    def give_specific_hand(self, name_player, cards): 
        self.hands_manager.give_specific_hand(name_player, cards)
        return self

    def determine_player_with_better_hand(self):
        return self.hands_manager.get_players_with_best_hands()   