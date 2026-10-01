from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure
from PokerHands.AllFigures.FullFigure import FullFigure
from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.card import Card, CardValue
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
from PokerHands.player.players_manager import PlayersManager
from PokerHands.game.turn_phase import TurnPhase
from PokerHands.hand import Hand
from PokerHands.manipulating_cards import ManipulatingCards
from PokerHands.tests.assert_helper import is_this_two_figure_are_equal
from PokerHands.tests.fake_multi_draw_cards import FakeMultiDrawCards

def test_launch_turn_phase_with_two_players_randomly():
    (TurnPhaseDriver(MultiDrawCards())
                    .add_player("Steve")
                    .add_player("Natacha")
                    .add_card_before_flop_phase("2♠", "Steve")
                    .add_card_before_flop_phase("A♥", "Natacha")
                    .add_card_before_flop_phase("6♠", "Steve")
                    .add_card_before_flop_phase("A♣", "Natacha")
                    .add_card_flop_phase("2♥")
                    .add_card_flop_phase("2♦")
                    .add_card_flop_phase("A♠")
                    .launch_phase_and_get_best_players()
                    .is_this_players_can_be_a_winner(["Steve", "Natacha"]))

def test_launch_turn_phase_with_two_players_and_steve_wins():
    false_cards = ["2♣"]
    (TurnPhaseDriver(FakeMultiDrawCards(false_cards))
        .add_player("Steve")
        .add_player("Natacha")
        .add_card_before_flop_phase("2♠", "Steve")
        .add_card_before_flop_phase("A♥", "Natacha")
        .add_card_before_flop_phase("6♠", "Steve")
        .add_card_before_flop_phase("A♣", "Natacha")
        .add_card_flop_phase("2♥")
        .add_card_flop_phase("2♦")
        .add_card_flop_phase("A♠")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Steve"])
        .is_this_best_figure(FourOfKindFigure(CardValue.TWO, CardValue.ACE))
        .is_this_hand("Steve", FourOfKindFigure(CardValue.TWO, CardValue.ACE))
        .is_this_hand("Natacha", FullFigure(CardValue.TWO, CardValue.ACE)))
    

def test_launch_turn_phase_with_two_players_and_natacha_wins():
    false_cards = ["3♣"]
    (TurnPhaseDriver(FakeMultiDrawCards(false_cards))
        .add_player("Steve")
        .add_player("Natacha")
        .add_card_before_flop_phase("2♠", "Steve")
        .add_card_before_flop_phase("A♥", "Natacha")
        .add_card_before_flop_phase("6♠", "Steve")
        .add_card_before_flop_phase("A♣", "Natacha")
        .add_card_flop_phase("2♥")
        .add_card_flop_phase("2♦")
        .add_card_flop_phase("A♠")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Natacha"])
        .is_this_best_figure(FullFigure(CardValue.TWO, CardValue.ACE))
        .is_this_hand("Steve", ThreeOfKindFigure(CardValue.TWO, CardValue.ACE))
        .is_this_hand("Natacha", FullFigure(CardValue.TWO, CardValue.ACE))
    )

def test_launch_turn_phase_with_two_players_win():
    false_cards = ["3♣"]
    (TurnPhaseDriver(FakeMultiDrawCards(false_cards))
        .add_player("Steve")
        .add_player("Natacha")
        .add_card_before_flop_phase("2♠", "Steve")
        .add_card_before_flop_phase("2♥", "Natacha")
        .add_card_before_flop_phase("A♦", "Steve")
        .add_card_before_flop_phase("A♣", "Natacha")
        .add_card_flop_phase("4♥")
        .add_card_flop_phase("J♦")
        .add_card_flop_phase("6♠")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Steve_Natacha"])
        .is_this_best_figure(HighCardFigure(CardValue.ACE))
        .is_this_hand("Steve", HighCardFigure(CardValue.ACE))
        .is_this_hand("Natacha", HighCardFigure(CardValue.ACE))
    )

def test_launch_turn_phase_with_ten_players_randomly():
    (TurnPhaseDriver(MultiDrawCards())
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .add_card_before_flop_phase("A♠", "Steve")
        .add_card_before_flop_phase("K♣", "Natacha")
        .add_card_before_flop_phase("A♠", "Steve")
        .add_card_before_flop_phase("K♣", "Natacha")
        .add_card_before_flop_phase("Q♥", "Tony")
        .add_card_before_flop_phase("J♦","Thor")
        .add_card_before_flop_phase("10♣", "Bruce")
        .add_card_before_flop_phase("9♦", "Clint")
        .add_card_before_flop_phase("8♥", "Carol")
        .add_card_before_flop_phase("7♠", "T'Challa")
        .add_card_before_flop_phase("6♣", "Steven")
        .add_card_before_flop_phase("5♦", "Wanda")
        .add_card_before_flop_phase("4♥", "Steve")
        .add_card_before_flop_phase("3♠", "Natacha")
        .add_card_before_flop_phase("2♣","Tony")
        .add_card_before_flop_phase("A♦", "Thor")
        .add_card_before_flop_phase("K♥", "Bruce")
        .add_card_before_flop_phase("Q♠", "Clint")
        .add_card_before_flop_phase("J♣", "Carol")
        .add_card_before_flop_phase("10♦", "T'Challa")
        .add_card_before_flop_phase("9♥", "Steven")
        .add_card_before_flop_phase("8♠", "Wanda")
        .add_card_flop_phase("4♥")
        .add_card_flop_phase("J♦")
        .add_card_flop_phase("6♠")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Steve", "Natacha", "Tony", "Thor", "Bruce", "Clint", "Carol", "T'Challa", "Steven", "Peter", "Wanda" ]))

def test_launch_turn_phase_with_ten_players_and_wanda_win():
    fake_cards = ["5♠"]
    (TurnPhaseDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .add_card_before_flop_phase("A♠", "Steve")
        .add_card_before_flop_phase("K♣", "Natacha")
        .add_card_before_flop_phase("Q♥", "Tony")
        .add_card_before_flop_phase("J♦","Thor")
        .add_card_before_flop_phase("10♣", "Bruce")
        .add_card_before_flop_phase("9♦", "Clint")
        .add_card_before_flop_phase("8♥", "Carol")
        .add_card_before_flop_phase("7♠", "T'Challa")
        .add_card_before_flop_phase("6♣", "Steven")
        .add_card_before_flop_phase("5♦", "Wanda")
        .add_card_before_flop_phase("4♥", "Steve")
        .add_card_before_flop_phase("3♠", "Natacha")
        .add_card_before_flop_phase("2♣","Tony")
        .add_card_before_flop_phase("A♦", "Thor")
        .add_card_before_flop_phase("7♥", "Bruce")
        .add_card_before_flop_phase("Q♠", "Clint")
        .add_card_before_flop_phase("J♣", "Carol")
        .add_card_before_flop_phase("10♦", "T'Challa")
        .add_card_before_flop_phase("9♥", "Steven")
        .add_card_before_flop_phase("8♠", "Wanda")               
        .add_card_flop_phase("5♥")
        .add_card_flop_phase("8♦")
        .add_card_flop_phase("4♠")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Wanda"])
        .is_this_best_figure(FullFigure(CardValue.EIGHT, CardValue.FIVE))
        .is_this_hand("Steve", TwoPairFigure(CardValue.FIVE, CardValue.FOUR, CardValue.ACE))
        .is_this_hand("Natacha", PairFigure(CardValue.FIVE, CardValue.KING))
        .is_this_hand("Tony", PairFigure(CardValue.FIVE, CardValue.QUEEN))
        .is_this_hand("Thor", PairFigure(CardValue.FIVE,CardValue.ACE))
        .is_this_hand("Bruce", PairFigure(CardValue.FIVE,CardValue.TEN))
        .is_this_hand("Clint", PairFigure(CardValue.FIVE,CardValue.QUEEN))
        .is_this_hand("Carol", TwoPairFigure(CardValue.EIGHT, CardValue.FIVE, CardValue.JACK))
        .is_this_hand("T'Challa", PairFigure(CardValue.FIVE, CardValue.TEN))
        .is_this_hand("Steven", PairFigure(CardValue.FIVE, CardValue.NINE))
        .is_this_hand("Wanda", FullFigure(CardValue.EIGHT, CardValue.FIVE))
    )

def test_launch_turn_phase_with_ten_players_and_tony_and_clint_win():
    fake_cards = ["Q♦"]
    (TurnPhaseDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .add_card_before_flop_phase("A♠", "Steve")
        .add_card_before_flop_phase("K♣", "Natacha")
        .add_card_before_flop_phase("Q♥", "Tony")
        .add_card_before_flop_phase("J♦","Thor")
        .add_card_before_flop_phase("10♣", "Bruce")
        .add_card_before_flop_phase("9♦", "Clint")
        .add_card_before_flop_phase("8♥", "Carol")
        .add_card_before_flop_phase("7♠", "T'Challa")
        .add_card_before_flop_phase("6♣", "Steven")
        .add_card_before_flop_phase("5♦", "Wanda")
        .add_card_before_flop_phase("4♥", "Steve")
        .add_card_before_flop_phase("3♠", "Natacha")
        .add_card_before_flop_phase("2♣","Tony")
        .add_card_before_flop_phase("A♦", "Thor")
        .add_card_before_flop_phase("7♥", "Bruce")
        .add_card_before_flop_phase("Q♠", "Clint")
        .add_card_before_flop_phase("J♣", "Carol")
        .add_card_before_flop_phase("10♦", "T'Challa")
        .add_card_before_flop_phase("9♥", "Steven")
        .add_card_before_flop_phase("8♠", "Wanda")                   
        .add_card_flop_phase("10♥")
        .add_card_flop_phase("6♦")
        .add_card_flop_phase("4♠")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Tony_Clint"])
        .is_this_best_figure(PairFigure(CardValue.QUEEN, CardValue.TEN))
        .is_this_hand("Steve", PairFigure(CardValue.FOUR, CardValue.ACE))
        .is_this_hand("Natacha", HighCardFigure(CardValue.KING))
        .is_this_hand("Tony", PairFigure(CardValue.QUEEN, CardValue.TEN))
        .is_this_hand("Thor", HighCardFigure(CardValue.ACE))
        .is_this_hand("Bruce", PairFigure(CardValue.TEN, CardValue.QUEEN))
        .is_this_hand("Clint", PairFigure(CardValue.QUEEN, CardValue.TEN))
        .is_this_hand("Carol", HighCardFigure(CardValue.QUEEN))
        .is_this_hand("T'Challa", PairFigure(CardValue.TEN, CardValue.QUEEN))
        .is_this_hand("Steven", PairFigure(CardValue.SIX, CardValue.QUEEN))
        .is_this_hand("Wanda", HighCardFigure(CardValue.QUEEN)))

class TurnPhaseDriver():
    def __init__(self, multi_draw_cards):
        self.players = {}
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

    def add_card_before_flop_phase(self, card_crypted, player_name):
        card = Card.parse(card_crypted)
        self.players_manager.add_cards_to_players(player_name, card)
        return self

    def add_card_flop_phase(self, card_crypted):
        card = Card.parse(card_crypted)
        for player_name in self.players_manager.get_all_players() : 
            self.players_manager.add_cards_to_players(player_name, card)
        return self

    def launch_phase_and_get_best_players(self):        
        turn_phase = TurnPhase(self.players_manager, self.multi_draw_cards)
        self.result = turn_phase.launch_phase_and_get_best_players()
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

    def is_this_hand(self, player_name, figure_expected): 
        figure_calculated = self.result.hands_by_player[player_name]
        is_right = is_this_two_figure_are_equal(figure_expected, figure_calculated) 
        assert(is_right == True)
        return self