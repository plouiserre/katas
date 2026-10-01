from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure
from PokerHands.AllFigures.FullFigure import FullFigure
from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.card import Card, CardValue
from PokerHands.manipulating_cards import ManipulatingCards
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
from PokerHands.game.river_phase import RiverPhase
from PokerHands.hand import Hand
from PokerHands.tests.assert_helper import is_this_two_figure_are_equal
from PokerHands.tests.fake_multi_draw_cards import FakeMultiDrawCards

def test_launch_river_phase_with_two_players_randomly():
    (RiverPhaseDriver(MultiDrawCards())
            .add_player("Steve")
            .add_player("Natacha")
            .add_card_draw("2♠", "Steve")
            .add_card_draw("A♥", "Natacha")
            .add_card_draw("6♠", "Steve")
            .add_card_draw("A♣", "Natacha")
            .add_card_flop_phase("2♥")
            .add_card_flop_phase("2♦")
            .add_card_flop_phase("A♠")
            .add_card_turn_phase("K♥")
            .launch_river_phase_and_gest_best_players()
            .is_this_players_can_be_a_winner(["Steve", "Natacha"]))
    
def test_launch_river_phase_with_two_players_and_steve_wins():
    false_cards = ["2♣"]
    (RiverPhaseDriver(FakeMultiDrawCards(false_cards))
        .add_player("Steve")
        .add_player("Natacha")
        .add_card_draw("2♠", "Steve")
        .add_card_draw("A♥", "Natacha")
        .add_card_draw("6♠", "Steve")
        .add_card_draw("A♣", "Natacha")
        .add_card_flop_phase("2♥")
        .add_card_flop_phase("2♦")
        .add_card_flop_phase("A♠")
        .add_card_turn_phase("K♥")
        .launch_river_phase_and_gest_best_players()
        .is_this_players_can_be_a_winner(["Steve"])
        .is_this_best_figure(FourOfKindFigure(CardValue.TWO, CardValue.ACE))
        .is_this_hand("Steve", FourOfKindFigure(CardValue.TWO, CardValue.ACE))
        .is_this_hand("Natacha", ThreeOfKindFigure(CardValue.TWO, CardValue.KING)))

def test_launch_river_phase_with_two_players_and_natacha_wins():
  false_cards = ["5♥"]
  (RiverPhaseDriver(FakeMultiDrawCards(false_cards))
           .add_player("Steve")
           .add_player("Natacha")
           .add_card_draw("2♠", "Steve")
           .add_card_draw("A♥", "Natacha")
           .add_card_draw("6♠", "Steve")
           .add_card_draw("A♣", "Natacha")
           .add_card_flop_phase("2♥")
           .add_card_flop_phase("2♦")
           .add_card_flop_phase("A♠")
           .add_card_turn_phase("Q♦")
           .launch_river_phase_and_gest_best_players()
           .is_this_players_can_be_a_winner(["Natacha"])
           .is_this_best_figure(FullFigure(CardValue.TWO, CardValue.ACE))
           .is_this_hand("Steve", ThreeOfKindFigure(CardValue.TWO, CardValue.ACE))
           .is_this_hand("Natacha", FullFigure(CardValue.TWO, CardValue.ACE)))

def test_launch_river_phase_with_two_players_win():
    false_cards = ["J♠"]
    (RiverPhaseDriver(FakeMultiDrawCards(false_cards))
        .add_player("Steve")
        .add_player("Natacha")
        .add_card_draw("2♠", "Steve")
        .add_card_draw("2♥", "Natacha")
        .add_card_draw("A♦", "Steve")
        .add_card_draw("A♣", "Natacha")
        .add_card_flop_phase("4♥")
        .add_card_flop_phase("J♦")
        .add_card_flop_phase("6♠")
        .add_card_turn_phase("5♥")
        .launch_river_phase_and_gest_best_players()
        .is_this_players_can_be_a_winner(["Steve_Natacha"])
        .is_this_best_figure(PairFigure(CardValue.JACK, CardValue.ACE))
        .is_this_hand("Steve", PairFigure(CardValue.JACK, CardValue.ACE))
        .is_this_hand("Natacha", PairFigure(CardValue.JACK, CardValue.ACE))
    )

def test_launch_river_phase_with_ten_players_randomly():
    (RiverPhaseDriver(MultiDrawCards())
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .add_card_draw("A♠", "Steve")
        .add_card_draw("K♣", "Natacha")
        .add_card_draw("Q♥", "Tony")
        .add_card_draw("J♦","Thor")
        .add_card_draw("10♣", "Bruce")
        .add_card_draw("9♦", "Clint")
        .add_card_draw("8♥", "Carol")
        .add_card_draw("7♠", "T'Challa")
        .add_card_draw("6♣", "Steven")
        .add_card_draw("5♦", "Wanda")
        .add_card_draw("4♥", "Steve")
        .add_card_draw("3♠", "Natacha")
        .add_card_draw("2♣","Tony")
        .add_card_draw("A♦", "Thor")
        .add_card_draw("K♥", "Bruce")
        .add_card_draw("Q♠", "Clint")
        .add_card_draw("J♣", "Carol")
        .add_card_draw("10♦", "T'Challa")
        .add_card_draw("9♥", "Steven")
        .add_card_draw("8♠", "Wanda")
        .add_card_flop_phase("4♥")
        .add_card_flop_phase("J♦")
        .add_card_flop_phase("6♠")
        .add_card_turn_phase("7♣")
        .launch_river_phase_and_gest_best_players()
        .is_this_players_can_be_a_winner(["Steve", "Natacha", "Tony", "Thor", "Bruce", "Clint", "Carol", "T'Challa", "Steven", "Peter", "Wanda" ]))        
    
def test_launch_river_phase_with_ten_players_and_wanda_win():
    fake_cards = ["8♦"]
    (RiverPhaseDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .add_card_draw("A♠", "Steve")
        .add_card_draw("K♣", "Natacha")
        .add_card_draw("Q♥", "Tony")
        .add_card_draw("J♦","Thor")
        .add_card_draw("10♣", "Bruce")
        .add_card_draw("9♦", "Clint")
        .add_card_draw("6♥", "Carol")
        .add_card_draw("7♠", "T'Challa")
        .add_card_draw("6♣", "Steven")
        .add_card_draw("5♦", "Wanda")
        .add_card_draw("4♥", "Steve")
        .add_card_draw("3♠", "Natacha")
        .add_card_draw("2♣","Tony")
        .add_card_draw("A♦", "Thor")
        .add_card_draw("7♥", "Bruce")
        .add_card_draw("Q♠", "Clint")
        .add_card_draw("J♣", "Carol")
        .add_card_draw("10♦", "T'Challa")
        .add_card_draw("9♥", "Steven")
        .add_card_draw("8♠", "Wanda")               
        .add_card_flop_phase("5♥")
        .add_card_flop_phase("8♥")
        .add_card_flop_phase("4♠")
        .add_card_flop_phase("8♠")
        .launch_river_phase_and_gest_best_players()
        .is_this_players_can_be_a_winner(["Wanda"])
        .is_this_best_figure(FourOfKindFigure(CardValue.EIGHT, CardValue.FIVE))        
        .is_this_hand("Steve", ThreeOfKindFigure(CardValue.EIGHT, CardValue.ACE))
        .is_this_hand("Natacha", ThreeOfKindFigure(CardValue.EIGHT, CardValue.KING))
        .is_this_hand("Tony", ThreeOfKindFigure(CardValue.EIGHT, CardValue.QUEEN))
        .is_this_hand("Thor", ThreeOfKindFigure(CardValue.EIGHT, CardValue.ACE))
        .is_this_hand("Bruce", ThreeOfKindFigure(CardValue.EIGHT, CardValue.TEN))
        .is_this_hand("Clint", ThreeOfKindFigure(CardValue.EIGHT, CardValue.QUEEN))
        .is_this_hand("Carol", ThreeOfKindFigure(CardValue.EIGHT, CardValue.JACK))
        .is_this_hand("T'Challa", ThreeOfKindFigure(CardValue.EIGHT, CardValue.TEN))
        .is_this_hand("Steven", ThreeOfKindFigure(CardValue.EIGHT, CardValue.NINE))
        .is_this_hand("Wanda", FourOfKindFigure(CardValue.EIGHT, CardValue.FIVE)))

def test_launch_river_phase_with_ten_players_and_tony_and_clint_win():
    fake_cards = ["Q♣"]
    (RiverPhaseDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .add_card_draw("A♠", "Steve")
        .add_card_draw("K♣", "Natacha")
        .add_card_draw("Q♥", "Tony")
        .add_card_draw("J♦","Thor")
        .add_card_draw("10♣", "Bruce")
        .add_card_draw("9♦", "Clint")
        .add_card_draw("8♥", "Carol")
        .add_card_draw("7♠", "T'Challa")
        .add_card_draw("6♣", "Steven")
        .add_card_draw("5♦", "Wanda")
        .add_card_draw("4♥", "Steve")
        .add_card_draw("3♠", "Natacha")
        .add_card_draw("2♣","Tony")
        .add_card_draw("A♦", "Thor")
        .add_card_draw("7♥", "Bruce")
        .add_card_draw("Q♠", "Clint")
        .add_card_draw("J♣", "Carol")
        .add_card_draw("10♦", "T'Challa")
        .add_card_draw("9♥", "Steven")
        .add_card_draw("8♠", "Wanda")                   
        .add_card_flop_phase("10♥")
        .add_card_flop_phase("6♦")
        .add_card_flop_phase("4♠")
        .add_card_turn_phase("Q♦")
        .launch_river_phase_and_gest_best_players()
        .is_this_players_can_be_a_winner(["Tony_Clint"])
        .is_this_best_figure(ThreeOfKindFigure(CardValue.QUEEN, CardValue.TEN))
        .is_this_hand("Steve", TwoPairFigure(CardValue.QUEEN, CardValue.FOUR, CardValue.ACE))
        .is_this_hand("Natacha", PairFigure(CardValue.QUEEN,CardValue.KING))
        .is_this_hand("Tony", ThreeOfKindFigure(CardValue.QUEEN, CardValue.TEN))
        .is_this_hand("Thor", PairFigure(CardValue.QUEEN,CardValue.ACE))
        .is_this_hand("Bruce", TwoPairFigure(CardValue.QUEEN, CardValue.TEN, CardValue.SEVEN))
        .is_this_hand("Clint", ThreeOfKindFigure(CardValue.QUEEN, CardValue.TEN))
        .is_this_hand("Carol", PairFigure(CardValue.QUEEN, CardValue.JACK))
        .is_this_hand("T'Challa", TwoPairFigure(CardValue.QUEEN, CardValue.TEN, CardValue.SEVEN))
        .is_this_hand("Steven", TwoPairFigure( CardValue.QUEEN, CardValue.SIX, CardValue.TEN))
        .is_this_hand("Wanda", PairFigure(CardValue.QUEEN, CardValue.TEN)))
    
class RiverPhaseDriver():
    def __init__(self, multi_draw_cards):
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
        self.players = {}
        self.winners = []

    def add_player(self, player_name):
        self.players_manager.add_player(player_name)
        return self
    
    def add_players(self, players_name): 
                for player_name in players_name:
                    self.players_manager.add_player(player_name)
                return self 

    def add_card_draw(self, card_encrypted, player_name):
        card = Card.parse(card_encrypted)
        self.players_manager.add_cards_to_players(player_name, card)
        return self

    def add_card_flop_phase(self, card_encrypted):
        card = Card.parse(card_encrypted)
        for player_name in self.players_manager.get_all_players():
            self.players_manager.add_cards_to_players(player_name, card)
        return self

    def add_card_turn_phase(self, card_encrypted):
        card = Card.parse(card_encrypted)
        for player_name in self.players_manager.get_all_players():
            self.players_manager.add_cards_to_players(player_name, card)
        return self

    def launch_river_phase_and_gest_best_players(self):
        river_phase = RiverPhase(self.players_manager, self.multi_draw_cards)
        self.result = river_phase.launch_phase_and_get_best_players()
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