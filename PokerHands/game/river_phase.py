from PokerHands.game.phase import Phase
class RiverPhase(Phase): 
    def __init__(self, player_manager, multi_draw_cards):
        super().__init__(player_manager, multi_draw_cards)
        self.card_burn = None
           
    def launch_phase_and_get_best_players(self):
        self.card_burn = super().burn_one_card()
        return super().launch_phase_and_get_best_players()
                