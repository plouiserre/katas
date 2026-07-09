from PokerHands.score import Score

class Game : 
    def __init__(self, deck, player_one, player_two):
        self.deck = deck
        self.player_one = player_one
        self.player_two = player_two

    def launch(self): 
        all_hands_cards = self.deck.drawn_five_cards_for_the_two_players()
        high_figure_first_hand = self.player_one.calculate_hand(all_hands_cards[0])
        high_figure_second_hand = self.player_two.calculate_hand(all_hands_cards[1])
        score = Score(high_figure_first_hand, high_figure_second_hand)
        return score.determinate_winner()