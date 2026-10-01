from PokerHands.player.compare_hand import CompareHand
from PokerHands.player.identify_hand import IdentifyHand
from PokerHands.player.player_result import PlayerResult

class PlayersManager : 
    def __init__(self, hand, multi_draw_cards):
        self.players = {}
        self.hand = hand
        self.multi_draw_cards = multi_draw_cards           

    def add_player(self, name_player):
        self.players[name_player] = []

    def draw_card_player(self, name_player):
            new_card = self.multi_draw_cards.draw_one_card()
            self.players[name_player].append(new_card)
            return self
    
    def give_specific_hand(self, name_player, cards): 
        self.players[name_player] = cards
        return self

    def get_players_with_best_hands(self):
        identify_hand = IdentifyHand(self.hand, self.players)
        hands_by_player = identify_hand.determinate_hands()
        compare_hand = CompareHand(self.players, hands_by_player)
        compare_results = compare_hand.get_players_with_best_hands()
        players_results = PlayerResult(compare_results.winners, compare_results.best_figure, hands_by_player)
        return players_results

    def add_cards_to_players(self, player_name, card):
        self.players[player_name].append(card)

    def get_all_players(self): 
        return self.players