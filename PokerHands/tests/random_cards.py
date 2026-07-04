import copy
import random

from PokerHands.card import Card, CardColor, CardValue

def add_cards(all_cards_value, values_to_add):
    for value in values_to_add :
        all_cards_value.append(value)

def get_all_colors(): 
    all_colors = [CardColor.CLUBS, CardColor.DIAMONDS, CardColor.HEARTS, CardColor.SPADES]
    return all_colors

def get_all_values():
    all_cards_values = [CardValue.TWO, CardValue.THREE, CardValue.FOUR,CardValue.FIVE,CardValue.SIX,
                        CardValue.SEVEN, CardValue.EIGHT, CardValue.NINE, CardValue.TEN, CardValue.JACK, CardValue.QUEEN, CardValue.KING, CardValue.ACE]
    return all_cards_values

def get_colors_random():
    all_colors = get_all_colors()
    index_card_color = random.randint(0, len(all_colors) - 1)
    card_color = all_colors[index_card_color]
    all_colors.remove(card_color)
    return card_color

def get_colors_random_without_remove():
    all_colors = get_all_colors()
    index_card_color = random.randint(0, len(all_colors) - 1)
    card_color = all_colors[index_card_color]
    return card_color

def get_high_cards(all_cards_values):
    high_card = CardValue.UNDEFINED
    if CardValue.TWO in all_cards_values :
        all_cards_values.remove(CardValue.TWO)
    high_card = get_random_card(all_cards_values)
    if CardValue.TWO not in all_cards_values :
        all_cards_values.append(CardValue.TWO)
    all_cards_values_copy = copy.deepcopy(all_cards_values)
    for value in all_cards_values_copy : 
        if high_card <= value : 
            all_cards_values.remove(value)
    return high_card

def get_high_card_complete(all_cards_values):
    card_value = get_high_cards(all_cards_values)
    card_color = get_colors_random_without_remove()
    return Card(card_value, card_color)

def get_lower_card(all_cards_values, high_card):
    second_card = CardValue.UNDEFINED
    all_cards_values_copy = copy.deepcopy(all_cards_values)
    for card_value in all_cards_values_copy : 
        if high_card <= card_value : 
            all_cards_values.remove(card_value)
    second_card = get_random_card(all_cards_values)
    return second_card

def get_lower_card_complete(all_cards_values, high_card): 
    card_value = get_lower_card(all_cards_values, high_card.value)
    card_color = get_colors_random_without_remove()
    return Card(card_value, card_color)

def get_shuffle_hand(hands):
    return random.shuffle(hands)

def get_random_card(all_cards_values) : 
    index = random.randint(0, len(all_cards_values) - 1)
    random_card = all_cards_values[index]
    all_cards_values.remove(random_card)
    return random_card

def get_random_card_complete(all_cards_values) : 
    card_value = get_random_card(all_cards_values)
    card_color = get_colors_random_without_remove()
    return Card(card_value, card_color)

def remove_cards(all_cards_value, values_to_remove): 
    for value in values_to_remove :
        if value in all_cards_value :
            all_cards_value.remove(value)
