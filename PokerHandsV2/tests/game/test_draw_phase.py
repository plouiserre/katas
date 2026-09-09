import pytest

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
from PokerHandsV2.exception.TooManyPlayerException import TooManyPlayerException
from PokerHandsV2.hand import Hand
from PokerHandsV2.game.draw_phase import DrawPhase
from PokerHandsV2.game.hands_manager import HandsManager
from PokerHandsV2.tests.fake_multi_draw_cards import FakeMultiDrawCards

def test_launch_draw_phase_with_two_players_randomly(): 
    (DrawAndComparePlayersHandDriver(MultiDrawCards())
        .add_players(["Steve","Natacha"])    
        .launch_draw_phase_and_compare_players_hand()
        .is_this_players_can_be_a_winner(["Steve", "Natacha", "Steve_Natacha"]))
    
def test_launch_draw_phase_with_two_players_and_steve_wins(): 
    fake_cards = ["K♣","Q♥","Q♦","7♠"]
    (DrawAndComparePlayersHandDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha"])    
        .launch_draw_phase_and_compare_players_hand()
        .is_this_players_can_be_a_winner(["Steve"]))

def test_launch_draw_phase_with_two_players_and_natacha_wins(): 
    fake_cards = ["10♣","Q♥","J♦","7♠"]
    (DrawAndComparePlayersHandDriver(FakeMultiDrawCards(fake_cards))
            .add_players(["Steve","Natacha"])                                 
            .launch_draw_phase_and_compare_players_hand()
            .is_this_players_can_be_a_winner(["Natacha"]))
    
def test_launch_draw_phase_with_two_players_and_steve_and_natacha_win(): 
    fake_cards = ["Q♣","Q♥","Q♦","Q♠"]
    (DrawAndComparePlayersHandDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha"])    
        .launch_draw_phase_and_compare_players_hand()
        .is_this_players_can_be_a_winner(["Steve_Natacha"]))

def test_launch_draw_phase_with_six_players_randomly(): 
    (DrawAndComparePlayersHandDriver(MultiDrawCards())
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])                                                                          
        .launch_draw_phase_and_compare_players_hand()
        .is_this_players_can_be_a_winner(["Steve", "Natacha", "Tony", "Thor", "Bruce", "Clint"]))

def test_launch_draw_phase_with_six_players_and_steve_wins():
    fake_cards = ["K♣", "Q♥", "J♣", "10♥",  "9♣", "8♥", "Q♦", "J♠", "10♦", "9♠", "8♦", "7♠"]
    (DrawAndComparePlayersHandDriver(FakeMultiDrawCards(fake_cards))
            .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])                                                                                                                        
            .launch_draw_phase_and_compare_players_hand()
            .is_this_players_can_be_a_winner(["Steve"]))

def test_launch_draw_phase_with_six_players_and_tony_wins():
    fake_cards = ["7♣", "J♣", "Q♥", "10♥", "9♣", "8♥", "6♦", "10♦", "J♠", "9♠", "8♦", "7♠"]
    (DrawAndComparePlayersHandDriver(FakeMultiDrawCards(fake_cards))
            .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])                                                                                                                      
            .launch_draw_phase_and_compare_players_hand()
            .is_this_players_can_be_a_winner(["Tony"]))

def test_launch_draw_phase_with_six_players_and_clint_wins():
    fake_cards = ["7♣", "6♥", "J♣", "10♥", "9♣", "A♥", "6♦", "5♠", "10♦", "9♠", "8♦", "A♠"]
    (DrawAndComparePlayersHandDriver(FakeMultiDrawCards(fake_cards))
            .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])
            .launch_draw_phase_and_compare_players_hand()
            .is_this_players_can_be_a_winner(["Clint"]))

def test_launch_draw_phase_with_six_players_and_natacha_and_bruce_win(): 
    fake_cards = ["7♣", "K♥", "J♣", "10♥", "K♣", "2♥", "6♦", "Q♠", "10♦", "9♠", "Q♦", "4♠"]
    (DrawAndComparePlayersHandDriver(FakeMultiDrawCards(fake_cards))
            .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint"])
            .launch_draw_phase_and_compare_players_hand()
            .is_this_players_can_be_a_winner(["Natacha_Bruce"]))

def test_launch_draw_phase_with_ten_players_randomly(): 
    (DrawAndComparePlayersHandDriver(MultiDrawCards())
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .launch_draw_phase_and_compare_players_hand()
        .is_this_players_can_be_a_winner(["Steve", "Natacha", "Tony", "Thor", "Bruce", "Clint", "Carol", "T'Challa", "Steven", "Peter", "Wanda"]))

def test_launch_draw_phase_with_ten_players_and_carol_wins():
    fake_cards = ["7♣", "K♥", "J♣", "10♥", "K♣", "2♥", "A♥", "A♦", "3♠", "K♠", "6♦", "Q♠", "10♦", "9♠", "Q♦", "4♠","A♠", "Q♠", "4♣", "K♦"] 
    (DrawAndComparePlayersHandDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .launch_draw_phase_and_compare_players_hand()
        .is_this_players_can_be_a_winner(["Carol"]))

def test_launch_draw_phase_with_eleven_players_and_the_game_fails(): 
    with pytest.raises(TooManyPlayerException) :
        (DrawAndComparePlayersHandDriver(MultiDrawCards())
                .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Peter","Wanda"])
                .launch_draw_phase_and_compare_players_hand())

class DrawAndComparePlayersHandDriver():
    def __init__(self, multidrawcards):
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
        self.multi_draw_cards = multidrawcards
        self.hands_manager = HandsManager(hand, self.multi_draw_cards)
        self.winners = []
        
    def add_players(self, name_players):
        for name_player in name_players:
            self.players[name_player] = []
        return self

    def launch_draw_phase_and_compare_players_hand(self):
        self.draw_phase = DrawPhase(self.players, self.hands_manager)
        self.winners =  self.draw_phase.launch_phase_and_get_best_players()
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