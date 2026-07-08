import copy
import random 

def test_1() : 
    all_colors = ["♠", "♥", "♦", "♣"]
    all_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    all_combinaisons = __calculate_all_combinaisons(all_colors, all_values)

    assert(drawn_randomly_card(all_values, all_colors, []) in all_combinaisons)

def test_2() : 
    final_card = "Q♥"
    all_colors = ["♠", "♥", "♦", "♣"]
    all_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    all_combinaisons = __calculate_all_combinaisons(all_colors, all_values)
    all_last_pickus_cards = copy.deepcopy(all_combinaisons)
    all_last_pickus_cards.remove(final_card)

    assert(final_card == drawn_randomly_card(all_values, all_colors, all_last_pickus_cards))


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