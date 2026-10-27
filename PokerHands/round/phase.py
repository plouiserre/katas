from abc import ABC, abstractmethod


class Phase(ABC):
    def __init__(self, player_manager, multi_draw_cards):
        self.player_manager = player_manager
        self.multi_draw_cards = multi_draw_cards        
        self.card_turned = None

    @abstractmethod
    def launch_phase_and_get_best_players(self):
        self.__draw_turn()
        result = self.player_manager.get_players_with_best_combination()
        return result   
    
    def burn_one_card(self):
        card_burn = self.player_manager.burn_one_card()
        return card_burn
    
    def __draw_turn(self):
        self.card_turned = self.multi_draw_cards.draw_one_card()
        for player_name in self.player_manager.get_all_players() : 
            self.player_manager.add_cards_to_players(player_name, self.card_turned)