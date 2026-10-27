from PokerHands.round.phase_result.river_result import RiverResult
class RiverPhase(): 
    def __init__(self, table):
        self.table = table
        self.card_burn = None
        self.river_card = None
           
    def launch_phase_and_get_all_river_datas(self):
        self.card_burn = self.table.burn_one_card()
        self.river_card = self.table.deal_turn()
        self.table.affect_boards_cards_to_players([self.river_card])
        river_result = RiverResult.create(self.table.players, self.river_card, self.card_burn)
        return river_result
                