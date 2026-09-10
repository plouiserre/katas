import copy

from PokerHands.card import Card, CardValue, CardColor
from typing import Iterator

class ManipulatingCards :
    def __init__(self):
        pass

    def count_cards(self, hand : Iterator[Card]) -> dict[int, CardValue]:
        counting_cards = {}
        for card in hand : 
            if card.value in counting_cards : 
                counting_cards[card.value] += 1
            else : 
                counting_cards[card.value] = 1
        return counting_cards

    def sorted_card(self, hand): 
        all_cards = copy.deepcopy(hand)
        hand_ordered = []
        while(len(hand_ordered) < len(hand)) :
            min_card = Card(CardValue.UNDEFINED, CardColor.UNDEFINED)
            for idx, card_in_hand in enumerate(all_cards) : 
                card = all_cards[idx]
                if min_card == Card(CardValue.UNDEFINED, CardColor.UNDEFINED) :
                    min_card = card
                    continue
                else : 
                    if min_card.value > card.value : 
                        min_card = card
            hand_ordered.append(min_card)
            all_cards.remove(min_card) 
        return hand_ordered