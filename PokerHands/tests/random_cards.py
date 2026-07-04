import copy
import random

from PokerHands.card import CardColor, CardValue

def get_all_values():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    return all_cards_values

def add_cards(all_cards_value, values_to_add):
    for value in values_to_add :
        all_cards_value.append(value)

def remove_cards(all_cards_value, values_to_remove): 
    for value in values_to_remove :
        all_cards_value.remove(value)

def get_all_colors(): 
    all_colors = [CardColor.CLUBS, CardColor.DIAMONDS, CardColor.HEARTS, CardColor.SPADES]
    return all_colors

def get_high_cards(all_cards_values):
    high_card = CardValue.UNDEFINED
    if CardValue.TWO in all_cards_values :
        all_cards_values.remove(CardValue.TWO)
    high_card = get_random_card(all_cards_values)
    if CardValue.TWO not in all_cards_values :
        all_cards_values.append(CardValue.TWO)
    return high_card

def get_lower_card(all_cards_values, high_card):
    second_card = CardValue.UNDEFINED
    all_cards_values_copy = copy.deepcopy(all_cards_values)
    for card_value in all_cards_values_copy : 
        if high_card <= card_value : 
            all_cards_values.remove(card_value)
    second_card = get_random_card(all_cards_values)
    return second_card

def get_random_card(all_cards_values) : 
    index = random.randint(0, len(all_cards_values) - 1)
    random_card = all_cards_values[index]
    all_cards_values.remove(random_card)
    return random_card

def get_colors_random():
    all_colors = get_all_colors()
    index_card_color = random.randint(0, len(all_colors) - 1)
    card_color = all_colors[index_card_color]
    all_colors.remove(card_color)
    return card_color
