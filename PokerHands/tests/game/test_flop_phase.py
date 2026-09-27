from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.AllFigures.FlushFigure import FlushFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.detector.four_cards_detector import FourCardsDetector
from PokerHands.detector.flush_detector import FlushDetector
from PokerHands.detector.full_detector import FullDetector
from PokerHands.detector.high_card_detector import HighCardDetector
from PokerHands.detector.pair_detector import PairDetector
from PokerHands.detector.quinte_flush_detector import QuinteFlushDetector
from PokerHands.detector.quinte_detector import QuinteDetector
from PokerHands.detector.three_cards_detector import ThreeCardsDetector
from PokerHands.detector.two_pairs_detector import TwoPairsDetector
from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.game.flop_phase import FlopPhase
from PokerHands.player.players_manager import PlayersManager
from PokerHands.hand import Hand
from PokerHands.manipulating_cards import ManipulatingCards
from PokerHands.tests.assert_helper import is_this_two_figure_are_equal
from PokerHands.tests.fake_multi_draw_cards import FakeMultiDrawCards

def test_launch_flop_phase_with_two_players_randomly():
    (CompareHandsAfterFlopDriver(MultiDrawCards())
        .add_player("Steve")
        .add_player("Natacha")
        .add_card_before_flop("2♠", "Steve")
        .add_card_before_flop("A♥", "Natacha")
        .add_card_before_flop("6♠", "Steve")
        .add_card_before_flop("A♣", "Natacha")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Steve", "Natacha"]))     

def test_launch_flop_phase_with_two_players_and_steve_wins(): 
    fake_cards = ["A♠", "Q♠", "8♠"]
    (CompareHandsAfterFlopDriver(FakeMultiDrawCards(fake_cards))
        .add_player("Steve")
        .add_player("Natacha")
        .add_card_before_flop("2♠", "Steve")
        .add_card_before_flop("A♥", "Natacha")
        .add_card_before_flop("6♠", "Steve")
        .add_card_before_flop("A♣", "Natacha")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Steve"])
        .is_this_best_figure(FlushFigure(CardColor.SPADES, CardValue.ACE)))  

def test_launch_flop_phase_with_two_players_and_natacha_wins(): 
    fake_cards = ["A♠", "Q♥", "8♣"]
    (CompareHandsAfterFlopDriver(FakeMultiDrawCards(fake_cards))
                    .add_player("Steve")
                    .add_player("Natacha")
                    .add_card_before_flop("2♠", "Steve")
                    .add_card_before_flop("A♥", "Natacha")
                    .add_card_before_flop("6♠", "Steve")
                    .add_card_before_flop("A♣", "Natacha")
                    .launch_phase_and_get_best_players()
                    .is_this_players_can_be_a_winner(["Natacha"])
                    .is_this_best_figure(ThreeOfKindFigure(CardValue.ACE, CardValue.QUEEN))) 

def test_launch_flop_phase_with_two_players_win(): 
    fake_cards = ["K♠","Q♥", "8♣"]
    (CompareHandsAfterFlopDriver(FakeMultiDrawCards(fake_cards))
                    .add_player("Steve")
                    .add_player("Natacha")
                    .add_card_before_flop("A♠", "Steve")
                    .add_card_before_flop("A♥", "Natacha")
                    .add_card_before_flop("A♦", "Steve")
                    .add_card_before_flop("A♣", "Natacha")
                    .launch_phase_and_get_best_players()
                    .is_this_players_can_be_a_winner(["Steve","Natacha"])
                    .is_this_best_figure(PairFigure(CardValue.ACE, CardValue.KING))) 

def test_launch_flop_phase_with_ten_players_randomly():
    (CompareHandsAfterFlopDriver(MultiDrawCards())
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .add_card_before_flop("A♠", "Steve")
        .add_card_before_flop("K♣", "Natacha")
        .add_card_before_flop("Q♥", "Tony")
        .add_card_before_flop("J♦","Thor")
        .add_card_before_flop("10♣", "Bruce")
        .add_card_before_flop("9♦", "Clint")
        .add_card_before_flop("8♥", "Carol")
        .add_card_before_flop("7♠", "T'Challa")
        .add_card_before_flop("6♣", "Steven")
        .add_card_before_flop("5♦", "Wanda")
        .add_card_before_flop("4♥", "Steve")
        .add_card_before_flop("3♠", "Natacha")
        .add_card_before_flop("2♣","Tony")
        .add_card_before_flop("A♦", "Thor")
        .add_card_before_flop("K♥", "Bruce")
        .add_card_before_flop("Q♠", "Clint")
        .add_card_before_flop("J♣", "Carol")
        .add_card_before_flop("10♦", "T'Challa")
        .add_card_before_flop("9♥", "Steven")
        .add_card_before_flop("8♠", "Wanda")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Steve", "Natacha", "Tony", "Thor", "Bruce", "Clint", "Carol", "T'Challa", "Steven", "Wanda"]))

def test_launch_flop_phase_with_ten_players_and_steve_wins():
    fake_cards = ["A♥", "6♦", "4♠"]
    (CompareHandsAfterFlopDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .add_card_before_flop("A♠", "Steve")
        .add_card_before_flop("K♣", "Natacha")
        .add_card_before_flop("Q♥", "Tony")
        .add_card_before_flop("J♦","Thor")
        .add_card_before_flop("10♣", "Bruce")
        .add_card_before_flop("9♦", "Clint")
        .add_card_before_flop("8♥", "Carol")
        .add_card_before_flop("7♠", "T'Challa")
        .add_card_before_flop("6♣", "Steven")
        .add_card_before_flop("5♦", "Wanda")
        .add_card_before_flop("4♥", "Steve")
        .add_card_before_flop("3♠", "Natacha")
        .add_card_before_flop("2♣","Tony")
        .add_card_before_flop("A♦", "Thor")
        .add_card_before_flop("K♥", "Bruce")
        .add_card_before_flop("Q♠", "Clint")
        .add_card_before_flop("J♣", "Carol")
        .add_card_before_flop("10♦", "T'Challa")
        .add_card_before_flop("9♥", "Steven")
        .add_card_before_flop("8♠", "Wanda")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Steve"])
        .is_this_best_figure(TwoPairFigure(CardValue.ACE, CardValue.FOUR, CardValue.SIX)))

def test_launch_flop_phase_with_ten_players_and_bruce_and_tchalla_win():
    fake_cards = ["10♥", "6♦", "4♠"]
    (CompareHandsAfterFlopDriver(FakeMultiDrawCards(fake_cards))
            .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
            .add_card_before_flop("A♠", "Steve")
            .add_card_before_flop("K♣", "Natacha")
            .add_card_before_flop("Q♥", "Tony")
            .add_card_before_flop("J♦","Thor")
            .add_card_before_flop("10♣", "Bruce")
            .add_card_before_flop("9♦", "Clint")
            .add_card_before_flop("8♥", "Carol")
            .add_card_before_flop("7♠", "T'Challa")
            .add_card_before_flop("6♣", "Steven")
            .add_card_before_flop("5♦", "Wanda")
            .add_card_before_flop("4♥", "Steve")
            .add_card_before_flop("3♠", "Natacha")
            .add_card_before_flop("2♣","Tony")
            .add_card_before_flop("A♦", "Thor")
            .add_card_before_flop("7♥", "Bruce")
            .add_card_before_flop("Q♠", "Clint")
            .add_card_before_flop("J♣", "Carol")
            .add_card_before_flop("10♦", "T'Challa")
            .add_card_before_flop("9♥", "Steven")
            .add_card_before_flop("8♠", "Wanda")
            .launch_phase_and_get_best_players()
            .is_this_players_can_be_a_winner(["Bruce", "T'Challa"])
            .is_this_best_figure(PairFigure(CardValue.TEN, CardValue.SEVEN))) 

class CompareHandsAfterFlopDriver():
    def __init__(self, multi_draw_cards):
        self.card_players = {}
        manipulating_cards = ManipulatingCards()
        high_card_detector = HighCardDetector()
        pair_detector = PairDetector(manipulating_cards)
        two_pairs_detector = TwoPairsDetector(manipulating_cards)
        three_cards_detector = ThreeCardsDetector(manipulating_cards)
        quinte_detector = QuinteDetector(manipulating_cards)
        flush_detector = FlushDetector()
        full_detector = FullDetector(manipulating_cards)
        four_cards_detector = FourCardsDetector(manipulating_cards)
        quinte_flush_detector = QuinteFlushDetector(manipulating_cards, quinte_detector)
        hand = Hand(high_card_detector, pair_detector, two_pairs_detector, three_cards_detector, quinte_detector, flush_detector, full_detector, four_cards_detector, quinte_flush_detector)
        self.multi_draw_cards = multi_draw_cards
        self.players_manager = PlayersManager(hand, self.multi_draw_cards)
        self.winners = []

    def add_player(self, player_name):
        self.players_manager.add_player(player_name)
        return self

    def add_players(self, players_name): 
        for player_name in players_name:
            self.players_manager.add_player(player_name)
        return self

    def add_card_before_flop(self, card_crypted, player_name):
        card = Card.parse(card_crypted)
        self.players_manager.add_cards_to_players(player_name, card)
        return self

    def launch_phase_and_get_best_players(self):
        flop_phase = FlopPhase(self.players_manager, self.multi_draw_cards)
        self.result = flop_phase.launch_phase_and_get_best_players()
        return self

    def is_this_players_can_be_a_winner(self, players_name):
            is_winner = False
            for player_name in players_name : 
                if "_" in player_name : 
                    all_players = player_name.split("_")
                    is_winner = all_players == self.result.winners
                else : 
                    is_winner = player_name in self.result.winners
                if is_winner == True: 
                    break
            assert (is_winner == True)
            return self     

    def is_this_best_figure(self, figure): 
        is_equal =  is_this_two_figure_are_equal(figure, self.result.best_figure)
        assert(is_equal == True)
        return self