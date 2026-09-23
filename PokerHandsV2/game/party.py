from enum import Enum
from PokerHandsV2.game.draw_phase import DrawPhase
from PokerHandsV2.game.flop_phase import FlopPhase
from PokerHandsV2.game.river_phase import RiverPhase
from PokerHandsV2.game.turn_phase import TurnPhase

class PhasePoker(Enum) : 
    DRAW = 1
    FLOP = 2
    TURN = 3
    RIVER = 4

class Party : 
    def __init__(self, hands_manager, multi_draw_cards):
        self.multi_draw_cards = multi_draw_cards
        self.hands_manager = hands_manager
        self.winners = {}
        self.players = []

    def add_players(self, players_name): 
        for player_name in players_name : 
            self.players.append(player_name)

    def launch_party(self): 
        self.__init_all_phase()
        self.winners[PhasePoker.DRAW] = self.draw_phase.launch_phase_and_get_best_players()
        self.winners[PhasePoker.FLOP] = self.flop_phase.launch_phase_and_get_best_players()
        self.winners[PhasePoker.TURN]  = self.turn_phase.launch_phase_and_get_best_players()
        self.winners[PhasePoker.RIVER] = self.river_phase.launch_phase_and_get_best_players()
        return self.winners

    def __init_all_phase(self):
        self.draw_phase = DrawPhase(self.players, self.hands_manager)
        self.flop_phase = FlopPhase(self.hands_manager, self.multi_draw_cards)
        self.turn_phase = TurnPhase(self.hands_manager, self.multi_draw_cards)
        self.river_phase = RiverPhase(self.hands_manager, self.multi_draw_cards)
        