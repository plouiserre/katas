from enum import Enum
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
from PokerHands.game.draw_phase import DrawPhase
from PokerHands.game.flop_phase import FlopPhase
from PokerHands.hand import Hand
from PokerHands.player.players_manager import PlayersManager
from PokerHands.game.river_phase import RiverPhase
from PokerHands.game.turn_phase import TurnPhase

class PhasePoker(Enum) : 
    DRAW = 1
    FLOP = 2
    TURN = 3
    RIVER = 4

class Game : 
    def __init__(self, multi_draw_cards):
        self.multi_draw_cards = multi_draw_cards
        self.result = {}
        self.players = []

    def add_players(self, players_name): 
        for player_name in players_name : 
            self.players.append(player_name)

    def launch_game(self): 
        self.__init_all_players_and_phases()
        self.result[PhasePoker.DRAW] = self.draw_phase.launch_phase_and_get_best_players()
        self.result[PhasePoker.FLOP] = self.flop_phase.launch_phase_and_get_best_players()
        self.result[PhasePoker.TURN]  = self.turn_phase.launch_phase_and_get_best_players()
        self.result[PhasePoker.RIVER] = self.river_phase.launch_phase_and_get_best_players()
        return self.result

    def __init_all_players_and_phases(self):
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
        players_manager = PlayersManager(hand, self.multi_draw_cards)
        self.draw_phase = DrawPhase(self.players, players_manager)
        self.flop_phase = FlopPhase(players_manager, self.multi_draw_cards)
        self.turn_phase = TurnPhase(players_manager, self.multi_draw_cards)
        self.river_phase = RiverPhase(players_manager, self.multi_draw_cards)        