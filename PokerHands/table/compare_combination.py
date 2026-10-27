from PokerHands.exception.TooManyPlayerException import TooManyPlayerException
from PokerHands.table.comparaison_result import ComparaisonResult
from PokerHands.table.compare_same_type_combination import CompareSameTypeCombination
from PokerHands.winner import Winner

class CompareCombination: 
    def __init__(self, players, combination_by_player):
        self.players = players
        self.combination_by_player = combination_by_player   
        self.compare_same_type_combination = CompareSameTypeCombination()

    def get_players_with_best_combination(self):
        self.__check_not_too_many_players()
        best_players = [] 
        best_combination = self.__determinate_best_combination_from_all_players()
        best_players = self.__get_all_players_with_best_combination(best_combination)
        result = ComparaisonResult.Create(best_players, best_combination)
        return result 
                
    def __check_not_too_many_players(self): 
        if len(self.players) > 10 : 
            raise TooManyPlayerException("You cannot have more than ten players for a game.")

    def __determinate_best_combination_from_all_players(self):
        best_combination = None
        for player_name in self.combination_by_player : 
            combination = self.combination_by_player[player_name]
            if best_combination == None : 
                best_combination = combination
                continue
            combinations_to_compare = [combination, best_combination]
            winner = self.__determinate_winner(combinations_to_compare)
            if winner == Winner.FIRST_COMBINATION :
                best_combination = combination
        return best_combination

    def __determinate_winner(self, combinations ): 
            FIRST_COMBINATION = combinations[0]
            SECOND_COMBINATION = combinations[1]
            if FIRST_COMBINATION.points < SECOND_COMBINATION.points : 
                return Winner.SECOND_COMBINATION
            elif SECOND_COMBINATION.points < FIRST_COMBINATION.points : 
                return Winner.FIRST_COMBINATION
            else : 
                return self.compare_same_type_combination.compare_combinations(FIRST_COMBINATION, SECOND_COMBINATION)    
    
    
    def __get_all_players_with_best_combination(self, best_combination):
        best_players = []
        for player_name in self.combination_by_player : 
            combination = self.combination_by_player[player_name] 
            if best_combination == combination : 
                best_players.append(player_name)
        return best_players