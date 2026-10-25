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
from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.hand.flop_phase import FlopPhase
from PokerHands.hand.pre_flop_phase import PreFlopPhase
from PokerHands.hand.showdown_phase import ShowdownPhase
from PokerHands.poker_hand import PokerHand
from PokerHands.table.table import Table
from PokerHands.hand.river_phase import RiverPhase
from PokerHands.hand.turn_phase import TurnPhase

class PhasePoker(Enum) : 
    DRAW = 1
    FLOP = 2
    TURN = 3
    RIVER = 4
    SHOWDOWN = 5

class Hand : 
    def __init__(self, multi_draw_cards):
        self.multi_draw_cards = multi_draw_cards
        self.players = []
        self.pre_flop_data = None
        self.flop_phase_data = None
        self.turn_phase_data = None
        self.river_phase_data = None

    def add_players(self, players_name): 
        for player_name in players_name : 
            self.players.append(player_name)

    def launch_hand(self): 
        self.__init_all_players_and_phases()
        self.pre_flop_data = self.pre_flop_phase.launch_phase_and_get_all_pre_flop_datas()
        self.flop_phase_data = self.flop_phase.launch_phase_and_get_all_flop_datas()
        self.turn_phase_data = self.turn_phase.launch_phase_and_get_all_turn_datas()
        self.river_phase_data  = self.river_phase.launch_phase_and_get_all_river_datas()
        hand_result = self.show_down_phase.analyze_pokers_hand_and_calculate_hand_results()
        return hand_result

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
        poker_hand = PokerHand(high_card_detector, pair_detector, two_pairs_detector, three_cards_detector, quinte_detector, flush_detector, full_detector, four_cards_detector, quinte_flush_detector)
        table = Table(self.multi_draw_cards)
        self.pre_flop_phase = PreFlopPhase(self.players, table)
        self.flop_phase = FlopPhase(table)
        self.turn_phase = TurnPhase(table)
        self.river_phase = RiverPhase(table)  
        poker_hand = PokerHand(high_card_detector, pair_detector, two_pairs_detector, three_cards_detector, quinte_detector, flush_detector, full_detector, four_cards_detector, quinte_flush_detector)
        self.show_down_phase = ShowdownPhase(poker_hand, table)      