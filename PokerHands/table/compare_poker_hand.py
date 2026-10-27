from PokerHands.exception.TooManyPlayerException import TooManyPlayerException
from PokerHands.table.comparaison_result import ComparaisonResult
from PokerHands.table.compare_same_type_poker_hand import CompareSameTypePokerHand
from PokerHands.winner import Winner

class ComparePokerHand: 
    def __init__(self, players, combination_by_player):
        self.players = players
        self.combination_by_player = combination_by_player   
        self.compare_same_type_poker_hand = CompareSameTypePokerHand()

    def get_players_with_best_combination(self):
        self.__check_not_too_many_players()
        best_players = [] 
        best_poker_hand = self.__determinate_best_combination_from_all_players()
        best_players = self.__get_all_players_with_best_poker_hand(best_poker_hand)
        result = ComparaisonResult.Create(best_players, best_poker_hand)
        return result 
                
    def __check_not_too_many_players(self): 
        if len(self.players) > 10 : 
            raise TooManyPlayerException("You cannot have more than ten players for a game.")

    def __determinate_best_combination_from_all_players(self):
        best_poker_hand = None
        for player_name in self.combination_by_player : 
            combination = self.combination_by_player[player_name]
            if best_poker_hand == None : 
                best_poker_hand = combination
                continue
            poker_hands_to_compare = [combination, best_poker_hand]
            winner = self.__determinate_winner(poker_hands_to_compare)
            if winner == Winner.FIRST_COMBINATION :
                best_poker_hand = combination
        return best_poker_hand

    def __determinate_winner(self, poker_hands ): 
            FIRST_COMBINATION = poker_hands[0]
            SECOND_COMBINATION = poker_hands[1]
            if FIRST_COMBINATION.points < SECOND_COMBINATION.points : 
                return Winner.SECOND_COMBINATION
            elif SECOND_COMBINATION.points < FIRST_COMBINATION.points : 
                return Winner.FIRST_COMBINATION
            else : 
                return self.compare_same_type_poker_hand.compare_poker_hands(FIRST_COMBINATION, SECOND_COMBINATION)    
    
    
    def __get_all_players_with_best_poker_hand(self, best_poker_hand):
        best_players = []
        for player_name in self.combination_by_player : 
            combination = self.combination_by_player[player_name] 
            if best_poker_hand == combination : 
                best_players.append(player_name)
        return best_players