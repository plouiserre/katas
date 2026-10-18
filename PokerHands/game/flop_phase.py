from PokerHands.game.phase import Phase

class FlopPhase(Phase) : 
    def __init__(self, player_manager, multi_draw_cards):
        super().__init__(player_manager, multi_draw_cards)
        self.card_burn = None
        self.cards_returned = []

    def launch_phase_and_get_best_players(self): 
        self.card_burn = super().burn_one_card()
        self.__draw_flop()
        result = self.player_manager.get_players_with_best_hands()
        return result   

    def __draw_flop(self):
        flop = []
        i = 0
        while i < 3 :
            new_card = self.multi_draw_cards.draw_one_card()
            self.cards_returned.append(new_card)
            flop.append(new_card)
            i += 1
        for player_name in self.player_manager.get_all_players() : 
            for card in flop :                 
                self.player_manager.add_cards_to_players(player_name, card)
        return self