from PokerHands.game.game_result.turn_result import TurnResult

class TurnPhase() : 
    def __init__(self, table):
        self.table = table
        self.card_burn = None
        self.turn_card = None

    def launch_phase_and_get_all_turn_datas(self):
        self.card_burn = self.table.burn_one_card()
        self.turn_card = self.table.deal_turn()
        self.table.affect_boards_cards_to_players([self.turn_card])
        turn_result = TurnResult.create(self.table.players, self.turn_card, self.card_burn)
        return turn_result
                