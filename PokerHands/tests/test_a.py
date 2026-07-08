import copy
import random 

def test_1() : 
    all_colors = ["♠", "♥", "♦", "♣"]
    all_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    all_cards_drawned = drawn_randomly_five_cards(all_values, all_colors)
    
    assert(len(all_cards_drawned) == 5)
    assert(len(all_cards_drawned) == len(set(all_cards_drawned)))

def test_2() : 
    all_colors = ["♠", "♥", "♦", "♣"]
    all_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    attempt = 0

    while attempt < 5000 :
        all_cards_drawned = drawn_randomly_five_cards(all_values, all_colors)
        
        assert(len(all_cards_drawned) == 5)
        assert(len(all_cards_drawned) == len(set(all_cards_drawned)))
        attempt += 1

def drawn_randomly_five_cards(all_values, all_colors):
    hand = []
    all_cards_pickups = []
    while len(hand) < 5 :
        card_drawned = drawn_randomly_card(all_values, all_colors, all_cards_pickups)
        hand.append(card_drawned)
        all_cards_pickups.append(card_drawned)
    return hand


def drawn_randomly_card(all_values, all_colors, all_last_pickus_cards):
    is_ok_card = False 
    card_value = ""
    while is_ok_card == False :
        card_value_idx = random.randint(0, len(all_values) - 1)
        card_color_idx = random.randint(0, len(all_colors) - 1)
        card_value = str(all_values[card_value_idx]+all_colors[card_color_idx])
        is_ok_card = card_value not in all_last_pickus_cards
    return card_value


def __calculate_all_combinaisons(all_colors, all_values) : 
    all_combinaisons = []
    for color in all_colors : 
        for value in all_values : 
            card = value+color
            all_combinaisons.append(card)
    return all_combinaisons