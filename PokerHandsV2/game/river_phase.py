from PokerHandsV2.game.phase import Phase
class RiverPhase(Phase): 
    def __init__(self, hand_manager, multi_draw_cards):
            super().__init__(hand_manager, multi_draw_cards)
    
    def launch_phase_and_get_best_players(self):
        return super().launch_phase_and_get_best_players()
                