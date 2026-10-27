from PokerHands.table.compare_combination import CompareCombination
from PokerHands.table.identify_poker_combination import IdentifyCombination
from PokerHands.round.round_result import RoundResult

class ShowdownPhase :
    def __init__(self, combination, table):
        self.combination = combination
        self.table = table

    def analyze_pokers_hand_and_calculate_hand_results(self):
        identify_combination = IdentifyCombination(self.combination, self.table.players)
        combination_by_player = identify_combination.determinate_combination()
        compare_combination = CompareCombination(self.table.players, combination_by_player)
        compare_results = compare_combination.get_players_with_best_combination()
        round_result = RoundResult(compare_results.winners, compare_results.best_figure, combination_by_player)
        return round_result