import pytest

from PokerHands.card import Card
from PokerHandsV2.manipulating_cards import ManipulatingCards
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
    (HandManagerDriver()
        .add_players(["Steve","Natacha"])    
        .players_draw_first_card(["Steve", "Natacha"])
        .players_draw_second_card(["Steve", "Natacha"])
        .determine_player_with_better_hand()
        .is_this_players_can_be_a_winner(["Steve" , "Natacha", "Steve_Natacha"]))

def test_two_players_compare_specific_hands_after_drawn_and_steve_win(): 
    (HandManagerDriver()
        .add_players(["Steve","Natacha"])    
        .give_specific_hand("Steve", ["K♣","Q♦"])                                   
        .give_specific_hand("Natacha", ["Q♥", "7♠"])                                   
        .determine_player_with_better_hand()                                   
        .is_this_players_can_be_a_winner(["Steve"]))

def test_two_players_compare_specific_hands_after_drawn_and_natacha_win(): 
    (HandManagerDriver()
            .add_players(["Steve","Natacha"])    
            .give_specific_hand("Steve", ["10♣", "J♦"])                                   
            .give_specific_hand("Natacha", ["Q♥","7♠"])                                   
            .determine_player_with_better_hand()
            .is_this_players_can_be_a_winner(["Natacha"]))

def test_two_players_compare_specific_hands_after_drawn_and_no_one_win(): 
    (HandManagerDriver()
        .add_players(["Steve","Natacha"])    
        .give_specific_hand("Steve", ["Q♣","Q♦"])                                   
        .give_specific_hand("Natacha", ["Q♥","Q♠"])                                   
        .determine_player_with_better_hand()
        .is_this_players_can_be_a_winner(["Steve_Natacha"]))

def test_failing_two_players_compare_hands_because_steve_do_not_have_two_cards(): 
     with pytest.raises(PlayerDoNotHaveCompleteHandException) :
            (HandManagerDriver()
                               .add_players(["Steve","Natacha"])                                                                          
                               .players_draw_first_card(["Steve","Natacha"])
                               .players_draw_second_card(["Natacha"])                                                              
                               .determine_player_with_better_hand())

def test_six_players_compare_random_hands_after_drawn(): 
    (HandManagerDriver()
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])                                                                          
        .players_draw_first_card(["Steve","Natacha","Tony","Thor","Bruce","Clint"])
        .players_draw_second_card(["Steve","Natacha","Tony","Thor","Bruce","Clint"])
        .determine_player_with_better_hand()
        .is_this_players_can_be_a_winner(["Steve" , "Natacha", "Tony", "Thor", "Bruce", "Clint"]))

def test_six_players_compare_specific_hands_after_drawn_and_steve_win():
    (HandManagerDriver()
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])                                                                                                                        
        .give_specific_hand("Steve", ["K♣",  "Q♦"])                                   
        .give_specific_hand("Natacha", ["Q♥","J♠"])                                        
        .give_specific_hand("Tony", ["J♣","10♦"])                                   
        .give_specific_hand("Thor", ["10♥","9♠"])                                        
        .give_specific_hand("Bruce", ["9♣","8♦"])                                   
        .give_specific_hand("Clint", ["8♥","7♠"])
        .determine_player_with_better_hand()
        .is_this_players_can_be_a_winner(["Steve"]))

def test_six_players_compare_specific_hands_after_drawn_and_tony_win():
    (HandManagerDriver()
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])                                                                                                                      
        .give_specific_hand("Steve", ["7♣","6♦"])                                   
        .give_specific_hand("Natacha", ["J♣","10♦"])                                        
        .give_specific_hand("Tony", ["Q♥","J♠"])                                   
        .give_specific_hand("Thor", ["10♥","9♠"])                                        
        .give_specific_hand("Bruce", ["9♣","8♦"])                                   
        .give_specific_hand("Clint", ["8♥","7♠"])
        .determine_player_with_better_hand()
        .is_this_players_can_be_a_winner(["Tony"]))

def test_six_players_compare_specific_hands_after_drawn_and_clint_win():
    (HandManagerDriver()
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])
        .give_specific_hand("Steve", ["7♣","6♦"])                                   
        .give_specific_hand("Natacha", ["6♥","5♠"])                                        
        .give_specific_hand("Tony", ["J♣","10♦"])                                   
        .give_specific_hand("Thor", ["10♥","9♠"])                                        
        .give_specific_hand("Bruce", ["9♣","8♦"])                                   
        .give_specific_hand("Clint", ["A♥","A♠"])
        .determine_player_with_better_hand()
        .is_this_players_can_be_a_winner(["Clint"]))

def test_six_players_compare_specific_hands_after_drawn_and_natacha_and_bruce_win(): 
    (HandManagerDriver()
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])
        .give_specific_hand("Steve", ["7♣","6♦"])                                   
        .give_specific_hand("Natacha", ["K♥","Q♠"])                                        
        .give_specific_hand("Tony", ["J♣","10♦"])                                   
        .give_specific_hand("Thor", ["10♥","9♠"])                                        
        .give_specific_hand("Bruce", ["K♣","Q♦"])                                   
        .give_specific_hand("Clint", ["2♥","4♠"])
        .determine_player_with_better_hand()
        .is_this_players_can_be_a_winner(["Natacha", "Bruce"]))

def test_ten_players_compare_random_hands_after_drawn(): 
        (HandManagerDriver()
                .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                .players_draw_first_card(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])                                    
                .players_draw_second_card(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                .determine_player_with_better_hand()
                .is_this_players_can_be_a_winner(["Steve" , "Natacha", "Tony", "Thor", "Bruce", "Clint","Carol","T'Challa","Steven","Wanda"]))


def test_six_players_compare_specific_hands_after_drawn_and_wanda_win(): 
    (HandManagerDriver()
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .give_specific_hand("Steve", ["7♣","6♦"])                                   
        .give_specific_hand("Natacha", ["K♥","Q♠"])                                        
        .give_specific_hand("Tony", ["J♣","10♦"])                                   
        .give_specific_hand("Thor", ["10♥","9♠"])                                        
        .give_specific_hand("Bruce", ["K♣","Q♦"])                                   
        .give_specific_hand("Clint", ["2♥","4♠"])                                  
        .give_specific_hand("Carol", ["A♥","A♠"])                                 
        .give_specific_hand("T'Challa", ["A♦","Q♠"])                              
        .give_specific_hand("Steven", ["3♠","4♣"])                          
        .give_specific_hand("Wanda", ["K♠","K♦"])
        .determine_player_with_better_hand()
        .is_this_players_can_be_a_winner(["Carol"]))

def test_failing_because_more_ten_players(): 
    with pytest.raises(TooManyPlayerException) :
        (HandManagerDriver()
                .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Peter","Wanda"])
                .give_specific_hand("Steve", ["7♣","6♦"])                                   
                .give_specific_hand("Natacha", ["K♥","Q♠"])                                        
                .give_specific_hand("Tony", ["J♣","10♦"])                                   
                .give_specific_hand("Thor", ["10♥","9♠"])                                        
                .give_specific_hand("Bruce", ["K♣","Q♦"])                                   
                .give_specific_hand("Clint", ["2♥","4♠"])                                  
                .give_specific_hand("Carol", ["A♥","A♠"])                                 
                .give_specific_hand("T'Challa", ["A♦","Q♠"])                              
                .give_specific_hand("Steven", ["3♠","4♣"])                          
                .give_specific_hand("Peter", ["5♠","6♣"])                          
                .give_specific_hand("Wanda", ["K♠","K♦"])
                .determine_player_with_better_hand())

def test_if_it_is_not_flush_with_one_player_have_two_cards_the_same_colors_but_not_five():
    (HandManagerDriver()
            .add_players(["Steve","Natacha"])    
            .give_specific_hand("Steve", ["K♣","J♣"])                                   
            .give_specific_hand("Natacha", ["Q♥","Q♠"])                                   
            .determine_player_with_better_hand()
            .is_this_players_can_be_a_winner(["Natacha"]))

def test_if_it_is_not_flush_with_one_player_have_two_cards_the_same_colors_and_they_follow_each_other_but_not_five():
    (HandManagerDriver()
            .add_players(["Steve","Natacha"])    
            .give_specific_hand("Steve", ["K♣","Q♣"])                                   
            .give_specific_hand("Natacha", ["Q♥","Q♠"])                                          
            .determine_player_with_better_hand()
            .is_this_players_can_be_a_winner(["Natacha"]))

class HandManagerDriver():
    def __init__(self):
        manipulating_cards = ManipulatingCards()
        high_card_detector = HighCardDetector()
        pair_detector = PairDetector(manipulating_cards)
        two_pairs_detector = TwoPairsDetector(manipulating_cards)
        three_cards_detector = ThreeCardsDetector(manipulating_cards)
        straight_detector = StraightDetector(manipulating_cards)
        flush_detector = FlushDetector()
        full_detector = FullDetector(manipulating_cards)
        four_cards_detector = FourCardsDetector(manipulating_cards)
        quinte_flush_detector = QuinteFlushDetector(manipulating_cards)
        hand = Hand(high_card_detector, pair_detector, two_pairs_detector, three_cards_detector, straight_detector, flush_detector, full_detector, four_cards_detector, quinte_flush_detector)
        self.players = {}
        multi_draw_cards = MultiDrawCards()
        self.hands_manager = HandsManager(hand, multi_draw_cards)
        self.winner = []
        
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

    def give_specific_hand(self, name_player, cards_encrypted):
        cards = []
        for card_encrypted in cards_encrypted:
            card = Card.parse(card_encrypted)
            cards.append(card)
        self.hands_manager.give_specific_hand(name_player, cards)
        return self

    def determine_player_with_better_hand(self):
        self.winners = self.hands_manager.get_players_with_best_hands()   
        return self

    def is_this_players_can_be_a_winner(self, players_name):
        is_winner = False
        for player_name in players_name : 
            if "_" in player_name : 
                all_players = player_name.split("_")
                is_winner = all_players == self.winners
            else : 
                is_winner = player_name in self.winners
            if is_winner == True: 
                break
        assert (is_winner == True)
        return self