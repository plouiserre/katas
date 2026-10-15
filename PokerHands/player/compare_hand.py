from PokerHands.AllFigures.Figure import Figure
from PokerHands.AllFigures.FlushFigure import FlushFigure
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure
from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.AllFigures.QuinteFigure import QuinteFigure
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.exception.TooManyPlayerException import TooManyPlayerException
from PokerHands.hand import Hand
from PokerHands.player.comparaison_result import ComparaisonResult
from PokerHands.winner import Winner

class CompareHand: 
    def __init__(self, players, hands_by_player):
        self.players = players
        self.hands_by_player = hands_by_player   

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

    def __determinate_winner(self, hands : list[Figure] ): 
            first_hand = hands[0]
            second_hand = hands[1]
            if first_hand.points < second_hand.points : 
                return Winner.SECOND_HAND
            elif second_hand.points < first_hand.points : 
                return Winner.FIRST_HAND
            elif type(first_hand) is HighCardFigure and type(second_hand) is HighCardFigure:
                return self.__compare_two_hands_with_high_cards(first_hand, second_hand)
            elif type(first_hand) is PairFigure and type(second_hand) is PairFigure: 
                return self.__compare_two_hands_with_pairs(first_hand, second_hand)
            elif type(first_hand) is TwoPairFigure and type(second_hand) is TwoPairFigure : 
                return self.__compare_two_hands_with_two_pairs(first_hand, second_hand)
            elif type(first_hand) is ThreeOfKindFigure and type(second_hand) is ThreeOfKindFigure : 
                return self.__compare_two_hands_with_three_of_kinds(first_hand, second_hand)
            elif type(first_hand) is QuinteFigure and type(second_hand) is QuinteFigure : 
                return self.__compare_two_hands_with_quinte(first_hand, second_hand)
            elif type(first_hand) is FlushFigure and type(second_hand) is FlushFigure : 
                return self.__compare_two_hands_with_flush(first_hand, second_hand)
            elif type(first_hand) is FourOfKindFigure and type(second_hand) is FourOfKindFigure:
                return self.__compare_two_hands_with_four_a_kind(first_hand, second_hand)
            elif type(first_hand) is QuinteFlushFigure and type(second_hand) is QuinteFlushFigure:
                return self.__compare_two_hands_with_quinte_flush(first_hand, second_hand)
    
    def __compare_two_hands_with_high_cards(self, first_hand : Hand, second_hand : Hand) -> Winner: 
            if first_hand.value < second_hand.value : 
                return Winner.SECOND_HAND
            elif second_hand.value < first_hand.value : 
                return Winner.FIRST_HAND 
            else :
                return Winner.EQUALITY
                
    def __compare_two_hands_with_pairs(self, first_hand : Hand, second_hand : Hand) -> Winner:
        if first_hand.value < second_hand.value : 
            return Winner.SECOND_HAND
        elif second_hand.value < first_hand.value : 
            return Winner.FIRST_HAND
        else : 
            if first_hand.high_value_rest_of_cards < second_hand.high_value_rest_of_cards : 
                return Winner.SECOND_HAND
            elif second_hand.high_value_rest_of_cards < first_hand.high_value_rest_of_cards :
                return Winner.FIRST_HAND
            else : 
                return Winner.EQUALITY

    def __compare_two_hands_with_two_pairs(self, first_hand : TwoPairFigure, second_hand : TwoPairFigure) -> Winner : 
        if first_hand.first_pair_value < second_hand.first_pair_value : 
            return Winner.SECOND_HAND
        elif second_hand.first_pair_value < first_hand.first_pair_value : 
            return Winner.FIRST_HAND
        elif first_hand.first_pair_value == second_hand.first_pair_value : 
            if first_hand.second_pair_value < second_hand.second_pair_value : 
                return Winner.SECOND_HAND
            elif second_hand.second_pair_value < first_hand.second_pair_value : 
                return Winner.FIRST_HAND
            elif first_hand.second_pair_value == second_hand.second_pair_value : 
                if first_hand.high_value_rest_of_cards < second_hand.high_value_rest_of_cards :
                    return Winner.SECOND_HAND
                else :
                    return Winner.FIRST_HAND

    def __compare_two_hands_with_three_of_kinds(self, first_hand : ThreeOfKindFigure, second_hand : ThreeOfKindFigure): 
        if first_hand.value < second_hand.value :
            return Winner.SECOND_HAND
        elif second_hand.value < first_hand.value : 
            return Winner.FIRST_HAND
        elif first_hand.value == second_hand.value : 
            if first_hand.high_value_rest_of_cards < second_hand.high_value_rest_of_cards :
                return Winner.SECOND_HAND
            elif second_hand.high_value_rest_of_cards < first_hand.high_value_rest_of_cards : 
                return Winner.FIRST_HAND

    def __compare_two_hands_with_quinte(self, first_hand : QuinteFigure, second_hand : QuinteFigure):
        if first_hand.value < second_hand.value : 
            return Winner.SECOND_HAND 
        elif second_hand.value < first_hand.value : 
            return Winner.FIRST_HAND

    def __compare_two_hands_with_flush(self, first_hand : FlushFigure, second_hand : FlushFigure):
        if first_hand.high_value < second_hand.high_value : 
            return Winner.SECOND_HAND 
        elif second_hand.high_value < first_hand.high_value : 
            return Winner.FIRST_HAND

    def __compare_two_hands_with_four_a_kind(self, first_hand : FourOfKindFigure, second_hand : FourOfKindFigure):
        if first_hand.value < second_hand.value : 
            return Winner.SECOND_HAND 
        elif second_hand.value < first_hand.value : 
            return Winner.FIRST_HAND
        elif first_hand.value == second_hand.value : 
            if first_hand.high_value_rest_of_cards < second_hand.high_value_rest_of_cards : 
                return Winner.SECOND_HAND 
            elif second_hand.high_value_rest_of_cards < first_hand.high_value_rest_of_cards :
                return Winner.FIRST_HAND

    def __compare_two_hands_with_quinte_flush(self, first_hand : QuinteFlushFigure, second_hand : QuinteFlushFigure):
        if first_hand.value < second_hand.value : 
            return Winner.SECOND_HAND 
        elif second_hand.value < first_hand.value : 
            return Winner.FIRST_HAND
    
    def __get_all_players_with_best_hand(self, best_hand):
        best_players = []
        for player_name in self.hands_by_player : 
            hand = self.hands_by_player[player_name] 
            if best_hand == hand : 
                best_players.append(player_name)
        return best_players