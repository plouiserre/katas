from PokerHands.exception.TooManyPlayerException import TooManyPlayerException
from PokerHands.table.comparaison_result import ComparaisonResult
from PokerHands.table.compare_same_type_poker_hand import CompareSameTypePokerHand
from PokerHands.winner import Winner

class ComparePokerHand: 
    def __init__(self, players, poker_hands_by_player):
        self.players = players
        self.poker_hands_by_player = poker_hands_by_player   
        self.compare_same_type_poker_hand = CompareSameTypePokerHand()

    def get_players_with_best_poker_hands(self):
        self.__check_not_too_many_players()
        best_players = [] 
        best_poker_hand = self.__determinate_best_poker_hand_from_all_players()
        best_players = self.__get_all_players_with_best_poker_hand(best_poker_hand)
        result = ComparaisonResult.Create(best_players, best_poker_hand)
        return result 
                
    def __check_not_too_many_players(self): 
        if len(self.players) > 10 : 
            raise TooManyPlayerException("You cannot have more than ten players for a game.")

    def __determinate_best_poker_hand_from_all_players(self):
        best_poker_hand = None
        for player_name in self.poker_hands_by_player : 
            combination = self.poker_hands_by_player[player_name]
            if best_poker_hand == None : 
                best_poker_hand = combination
                continue
            poker_hands_to_compare = [combination, best_poker_hand]
            winner = self.__determinate_winner(poker_hands_to_compare)
            if winner == Winner.FIRST_POKER_HAND :
                best_poker_hand = combination
        return best_poker_hand

    def __determinate_winner(self, poker_hands ): 
            FIRST_POKER_HAND = poker_hands[0]
            SECOND_POKER_HAND = poker_hands[1]
            if FIRST_POKER_HAND.points < SECOND_POKER_HAND.points : 
                return Winner.SECOND_POKER_HAND
            elif SECOND_POKER_HAND.points < FIRST_POKER_HAND.points : 
                return Winner.FIRST_POKER_HAND
            else : 
                return self.compare_same_type_poker_hand.compare_poker_hands(FIRST_POKER_HAND, SECOND_POKER_HAND)    
    
    
    def __get_all_players_with_best_poker_hand(self, best_poker_hand):
        best_players = []
        for player_name in self.poker_hands_by_player : 
            combination = self.poker_hands_by_player[player_name] 
            if best_poker_hand == combination : 
                best_players.append(player_name)
        return best_players