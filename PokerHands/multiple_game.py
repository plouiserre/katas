from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.hand.hand import Hand

class MultipleGame : 
    def __init__(self):
        self.players = []
        self.number = 0
        self.hand_results = []

    def add_player(self, player_name): 
        self.players.append(player_name)
        return self

    def define_how_many_hand_will_be_launching(self, number):
        self.number = number
        return self

    def launch_multiple_hand(self): 
        for _ in range(self.number):
            multi_draw_cards = MultiDrawCards()
            hand = Hand(multi_draw_cards)
            hand.add_players(self.players)
            hand_result = hand.launch_hand()
            self.hand_results.append(hand_result)
        return self.hand_results