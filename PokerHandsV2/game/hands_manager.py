from PokerHands.AllFigures.Figure import Figure
from PokerHandsV2.AllFigures.HighCardFigure import HighCardFigure
from PokerHandsV2.AllFigures.PairFigure import PairFigure
from PokerHandsV2.exception.PlayerDoNotHaveCompleteHandException import PlayerDoNotHaveCompleteHandException
from PokerHandsV2.exception.TooManyPlayerException import TooManyPlayerException
from PokerHandsV2.hand import Hand
from PokerHandsV2.winner import Winner

class HandsManager : 
    def __init__(self, hand, multi_draw_cards):
        self.players = {}
        self.hand = hand
        self.multi_draw_cards = multi_draw_cards
        self.hands_by_player = {}                

    def add_player(self, name_player):
        self.players[name_player] = []

    #TODO study if it is necessary
    def draw_card_player(self, name_player):
            new_card = self.multi_draw_cards.draw_one_card()
            self.players[name_player].append(new_card)
            return self
    
    #TODO study if it is necessary
    def give_specific_hand(self, name_player, cards): 
        self.players[name_player] = cards
        return self

    def get_players_with_best_hands(self):
        self.__check_all_players_have_all_their_cards()
        self.__check_not_too_many_players()
        best_players = [] 
        self.__determinate_hand_for_each_player()      
        best_hand = self.__determinate_best_hand_from_all_players()
        best_players = self.__get_all_players_with_best_hand(best_hand)
        return best_players

    def add_cards_to_players(self, player_name, card):
        self.players[player_name].append(card)

    def get_all_players(self): 
        return self.players

    def __check_all_players_have_all_their_cards(self): 
        for player_name in self.players : 
            if len(self.players[player_name]) < 2: 
                raise PlayerDoNotHaveCompleteHandException(player_name+" do not have his/hers 2 cards ")
            
    def __check_not_too_many_players(self): 
        if len(self.players) > 10 : 
            raise TooManyPlayerException("You cannot have more than ten players for a game.")
        
    def __determinate_hand_for_each_player(self):
         for player_name in self.players : 
            player = self.players[player_name]
            hand = self.hand.determinate_high_figure(player) 
            self.hands_by_player[player_name] = hand

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

    def __get_all_players_with_best_hand(self, best_hand):
        best_players = []
        for player_name in self.hands_by_player : 
            hand = self.hands_by_player[player_name] 
            if best_hand == hand : 
                best_players.append(player_name)
        return best_players