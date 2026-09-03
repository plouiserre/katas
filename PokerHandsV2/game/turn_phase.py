#TODO add abstract class to all phases
class TurnPhase : 
    def __init__(self, hand_manager, multi_draw_cards):
        self.hand_manager = hand_manager
        self.multi_draw_cards = multi_draw_cards

    def launch_phase_and_get_best_players(self):
        self.__draw_turn()
        best_players = self.hand_manager.get_players_with_best_hands()
        return best_players   

    def __draw_turn(self):
        new_card = self.multi_draw_cards.draw_one_card()
        for player_name in self.hand_manager.get_all_players() : 
            self.hand_manager.add_cards_to_players(player_name, new_card)
                