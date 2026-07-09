import random

class Deck :
    def __init__(self):
        self.all_colors = ["♠", "♥", "♦", "♣"]
        self.all_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def drawn_five_cards_for_the_two_players(self): 
        first_hand = self.__drawn_five_cards_for_one_player()
        second_hand = self.__drawn_five_cards_for_one_player()
        all_hands = [first_hand, second_hand]
        return all_hands
    
    def __drawn_five_cards_for_one_player(self) : 
        hand = []
        all_cards_pickups = []
        while len(hand) < 5 :
            card_drawned = self.__drawn_randomly_card(all_cards_pickups)
            hand.append(card_drawned)
            all_cards_pickups.append(card_drawned)
        return hand
    
    def __drawn_randomly_card(self, all_last_pickus_cards):
        is_ok_card = False 
        card_value = ""
        while is_ok_card == False :
            card_value_idx = random.randint(0, len(self.all_values) - 1)
            card_color_idx = random.randint(0, len(self.all_colors) - 1)
            card_value = str(self.all_values[card_value_idx] + self.all_colors[card_color_idx])
            is_ok_card = card_value not in all_last_pickus_cards
        return card_value