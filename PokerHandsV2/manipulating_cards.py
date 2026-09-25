import copy

from enum import Enum
from PokerHandsV2.card import Card, CardValue, CardColor
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

    def sorted_card(self, hand, limit, sorted_type): 
        hand_sorted_completed = self.__sorted_all_cards(hand, sorted_type)
        if len(hand_sorted_completed) <= limit : 
            return [hand_sorted_completed]
        else : 
            return self.__get_all_combinaisons_carded_sorted(hand_sorted_completed, limit)

    def __sorted_all_cards(self, hand, sorted_type):
        all_cards = copy.deepcopy(hand)
        hand_ordered = []
        last_card = Card(CardValue.UNDEFINED, CardColor.UNDEFINED)
        only_doublons = []
        while(len(all_cards) > 0) :
            min_card = self.__get_min_card_from_selection(all_cards)                            
            if ((sorted_type == SortedType.ONLY_DOUBLONS or sorted_type == SortedType.NO_DOUBLON) and last_card.value == min_card.value ):
                only_doublons.append(last_card)
                only_doublons.append(min_card)
            elif (sorted_type == SortedType.KEEP_ONE_DOUBLON and last_card.value == min_card.value) == False : 
                hand_ordered.append(min_card)
            last_card = min_card
            all_cards.remove(min_card)
        if sorted_type == SortedType.ONLY_DOUBLONS :
            return only_doublons
        elif sorted_type == SortedType.NO_DOUBLON :
            no_doublon_list = self.__delete_all_doublons(hand_ordered, only_doublons)
            return no_doublon_list
        else : 
            return hand_ordered

    def __delete_all_doublons(self, sorted_list, only_doublons):
        final_list = copy.deepcopy(sorted_list)
        for doublon in only_doublons : 
            for element in sorted_list : 
                if (doublon.value == element.value and doublon.color == element.color ):
                    final_list.remove(element)
        return final_list

    def __get_min_card_from_selection(self, all_cards):
        min_card = Card(CardValue.UNDEFINED, CardColor.UNDEFINED)
        for idx, _ in enumerate(all_cards) : 
                card = all_cards[idx]
                if min_card == Card(CardValue.UNDEFINED, CardColor.UNDEFINED) :
                    min_card = card
                    continue
                else : 
                    if min_card.value > card.value : 
                        min_card = card
        return min_card
    
    def __get_all_combinaisons_carded_sorted(self, hand_sorted_completed, limit):
        all_sorted_carded = []
        is_limit_breaked = False 
        i = 0
        while is_limit_breaked == False : 
            new_limit = i + limit
            part_of_carted_sorted = hand_sorted_completed[i :new_limit]
            all_sorted_carded.append(part_of_carted_sorted)
            i += 1
            if new_limit == len(hand_sorted_completed):
                is_limit_breaked = True
        return all_sorted_carded

class SortedType(Enum):
    NORMAL = 0
    NO_DOUBLON = 1
    KEEP_ONE_DOUBLON = 2
    ONLY_DOUBLONS = 3