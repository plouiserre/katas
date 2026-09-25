from enum import Enum
from PokerHandsV2.manipulating_cards import ManipulatingCards
from PokerHandsV2.detector.four_cards_detector import FourCardsDetector
from PokerHandsV2.detector.flush_detector import FlushDetector
from PokerHandsV2.detector.full_detector import FullDetector
from PokerHandsV2.detector.high_card_detector import HighCardDetector
from PokerHandsV2.detector.pair_detector import PairDetector
from PokerHandsV2.detector.quinte_flush_detector import QuinteFlushDetector
from PokerHandsV2.detector.quinte_detector import QuinteDetector
from PokerHandsV2.detector.three_cards_detector import ThreeCardsDetector
from PokerHandsV2.detector.two_pairs_detector import TwoPairsDetector
from PokerHandsV2.game.draw_phase import DrawPhase
from PokerHandsV2.game.flop_phase import FlopPhase
from PokerHandsV2.hand import Hand
from PokerHandsV2.player.player_manager import HandsManager
from PokerHandsV2.game.river_phase import RiverPhase
from PokerHandsV2.game.turn_phase import TurnPhase

class PhasePoker(Enum) : 
    DRAW = 1
    FLOP = 2
    TURN = 3
    RIVER = 4

class Party : 
    def __init__(self, multi_draw_cards):
        self.multi_draw_cards = multi_draw_cards
        self.winners = {}
        self.players = []

    def add_players(self, players_name): 
        for player_name in players_name : 
            self.players.append(player_name)

    def launch_party(self): 
        self.__init_all_players_and_phases()
        self.winners[PhasePoker.DRAW] = self.draw_phase.launch_phase_and_get_best_players()
        self.winners[PhasePoker.FLOP] = self.flop_phase.launch_phase_and_get_best_players()
        self.winners[PhasePoker.TURN]  = self.turn_phase.launch_phase_and_get_best_players()
        self.winners[PhasePoker.RIVER] = self.river_phase.launch_phase_and_get_best_players()
        return self.winners

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
        hands_manager = HandsManager(hand, self.multi_draw_cards)
        self.draw_phase = DrawPhase(self.players, hands_manager)
        self.flop_phase = FlopPhase(hands_manager, self.multi_draw_cards)
        self.turn_phase = TurnPhase(hands_manager, self.multi_draw_cards)
        self.river_phase = RiverPhase(hands_manager, self.multi_draw_cards)
        