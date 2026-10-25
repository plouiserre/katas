from PokerHands.hand.phase_result.flop_result import FlopResult

class FlopPhase() : 
    def __init__(self, table):
        self.table = table
        self.card_burn = None
        self.flop_cards = []

    def launch_phase_and_get_all_flop_datas(self): 
        self.__burn_one_card()
        self.__draw_flop()
        flop_result = FlopResult.create(self.table.players, self.flop_cards, self.card_burn)
        return flop_result   

    def __draw_flop(self):
        self.flop_cards = self.table.deal_flop()
        self.table.affect_boards_cards_to_players(self.flop_cards)
        return self

    def __burn_one_card(self): 
        self.card_burn = self.table.burn_one_card()