from PokerHands.table.compare_hand import CompareHand
from PokerHands.table.identify_poker_hand import IdentifyPokerHand
from PokerHands.table.hand_result import HandResult

class ShowdownPhase :
    def __init__(self, poker_hand, table):
        self.poker_hand = poker_hand
        self.table = table

    def analyze_pokers_hand_and_calculate_hand_results(self):
        identify_poker_hand = IdentifyPokerHand(self.poker_hand, self.table.players)
        poker_hands_by_player = identify_poker_hand.determinate_poker_hands()
        compare_poker_hand = CompareHand(self.table.players, poker_hands_by_player)
        compare_results = compare_poker_hand.get_players_with_best_poker_hands()
        hand_result = HandResult(compare_results.winners, compare_results.best_figure, poker_hands_by_player)
        return hand_result