from PokerHands.exception.TooManyPlayerException import TooManyPlayerException
from PokerHands.player.comparaison_result import ComparaisonResult
from PokerHands.player.compare_same_type_hand import CompareSameTypeHand
from PokerHands.winner import Winner

class CompareHand: 
    def __init__(self, players, hands_by_player):
        self.players = players
        self.hands_by_player = hands_by_player   
        self.compare_same_type_hand = CompareSameTypeHand()

    def get_players_with_best_hands(self):
        self.__check_not_too_many_players()
        best_players = [] 
        best_hand = self.__determinate_best_hand_from_all_players()
        best_players = self.__get_all_players_with_best_hand(best_hand)
        result = ComparaisonResult.Create(best_players, best_hand)
        return result 
                
    def __check_not_too_many_players(self): 
        if len(self.players) > 10 : 
            raise TooManyPlayerException("You cannot have more than ten players for a game.")

    def __determinate_best_hand_from_all_players(self):
        best_hand = None
        for player_name in self.hands_by_player : 
            hand = self.hands_by_player[player_name]
            if best_hand == None : 
                best_hand = hand
                continue
            hands_to_compare = [hand, best_hand]
            winner = self.__determinate_winner(hands_to_compare)
            if winner == Winner.FIRST_HAND :
                best_hand = hand
        return best_hand

    def __determinate_winner(self, hands ): 
            first_hand = hands[0]
            second_hand = hands[1]
            if first_hand.points < second_hand.points : 
                return Winner.SECOND_HAND
            elif second_hand.points < first_hand.points : 
                return Winner.FIRST_HAND
            else : 
                return self.compare_same_type_hand.compare_hands(first_hand, second_hand)    
    
    
    def __get_all_players_with_best_hand(self, best_hand):
        best_players = []
        for player_name in self.hands_by_player : 
            hand = self.hands_by_player[player_name] 
            if best_hand == hand : 
                best_players.append(player_name)
        return best_players