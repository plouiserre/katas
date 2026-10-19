from PokerHands.hand.compare_hand import CompareHand
from PokerHands.hand.identify_hand import IdentifyHand
from PokerHands.hand.player_result import PlayerResult

class Hand : 
    def __init__(self, poker_hand, multi_draw_cards):
        self.players = {}
        self.poker_hand = poker_hand
        self.multi_draw_cards = multi_draw_cards           

    def add_player(self, name_player):
        self.players[name_player] = []

    def draw_card_player(self, name_player):
            new_card = self.multi_draw_cards.draw_one_card()
            self.players[name_player].append(new_card)
            return self
    
    def give_specific_poker_hand(self, name_player, cards): 
        self.players[name_player] = cards
        return self

    def get_players_with_best_poker_hands(self):
        identify_poker_hand = IdentifyHand(self.poker_hand, self.players)
        poker_hands_by_player = identify_poker_hand.determinate_poker_hands()
        compare_poker_hand = CompareHand(self.players, poker_hands_by_player)
        compare_results = compare_poker_hand.get_players_with_best_poker_hands()
        players_results = PlayerResult(compare_results.winners, compare_results.best_figure, poker_hands_by_player)
        return players_results

    def add_cards_to_players(self, player_name, card):
        self.players[player_name].append(card)
        self.multi_draw_cards.remove_one_card(card)

    def get_all_players(self): 
        return self.players

    def burn_one_card(self): 
        card_burn = self.multi_draw_cards.draw_one_card()
        return card_burn