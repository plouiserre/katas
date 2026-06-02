from enum import Enum
from PokerHands.card import CardValue, CardColor
from PokerHands.Figure import HighCardFigure, PairFigure, TwoPairFigure, ThreeOfKindFigure, StraitFigure, FlushFigure, FullFigure, FourOfKindFigure, QuinteFlush

class Hand :
    def __init__(self):
        self.counting_cards = {}
    
    def determinate_high_figure(self, hand):
        cards_sorted = self.__count_all_cards(hand)
        quinte_flush = self.__detect_quinte_flush(hand)
        four_a_kind = self.__detect_four_a_kind(cards_sorted)
        full_figure = self.__detect_full(cards_sorted)
        flush_figure = self.__detect_flush(hand)
        strait_figure = self.__detect_straight(cards_sorted)
        three_of_kind = self.__detect_three_of_kind(cards_sorted)
        two_pairs = self.__detect_two_pairs(cards_sorted)
        pair = self.__detect_one_pair(cards_sorted)
        high_card_figure = self.__detect_high_card_figure(cards_sorted)
        if quinte_flush != None : 
            return quinte_flush
        elif four_a_kind != None : 
            return four_a_kind
        elif full_figure != None : 
            return full_figure
        elif flush_figure != None : 
            return flush_figure
        elif strait_figure != None : 
            return strait_figure
        elif three_of_kind != None : 
            return three_of_kind
        elif two_pairs != None : 
            return two_pairs
        elif pair != None : 
            return pair
        else : 
            return high_card_figure 

    def __count_all_cards(self, content) : 
        self.counting_cards = {}
        for card in content : 
            if card.value in self.counting_cards : 
                self.counting_cards[card.value] += 1
            else : 
                self.counting_cards[card.value] = 1
        return self.counting_cards
    
    def __detect_quinte_flush(self, hand):
        is_quinte_flush = True 
        last_card_color = CardColor.UNDEFINED
        last_card_value = CardValue.UNDEFINED
        is_ace_present = False
        card_value_hand = []
        hand_sorted = sorted(hand, key=lambda o : o.value)
        for card in hand_sorted : 
            if card.value == CardValue.ACE : 
                is_ace_present = True
            if last_card_color == CardColor.UNDEFINED  and last_card_value == CardValue.UNDEFINED:
                last_card_color = card.color
                last_card_value = card.value
                card_value_hand.append(card.value)
                continue
            elif last_card_color != card.color : 
                is_quinte_flush = False
                break
            elif is_ace_present and (CardValue.KING not in card_value_hand and CardValue.TWO not in card_value_hand): 
                is_quinte_flush = False
                break
            elif card.value != CardValue.ACE and (card.value - last_card_value > 1 or card.value in card_value_hand): 
                is_quinte_flush = False
                break
            else : 
                last_card_value = card.value
            card_value_hand.append(card.value)
        if is_quinte_flush : 
            if is_ace_present == False : 
                return QuinteFlush(last_card_value, last_card_color)
            elif is_ace_present and CardValue.TWO in card_value_hand : 
                return QuinteFlush(CardValue.FIVE, last_card_color)
            elif is_ace_present and CardValue.KING in card_value_hand : 
                return QuinteFlush(CardValue.ACE, last_card_color)
        else : 
            return None            
    
    def __detect_four_a_kind(self, cards_sorted):
        card_four_times = CardValue.UNDEFINED
        high_card_value = CardValue.UNDEFINED
        for card in cards_sorted : 
            number_cards = cards_sorted[card]
            if number_cards == 4 :
                card_four_times = card
            else :
                high_card_value = card
        if card_four_times != CardValue.UNDEFINED :
            return FourOfKindFigure(card_four_times, high_card_value)
        else : 
            return None
    
    def __detect_full(self, cards_sorted):
        card_two_times = CardValue.UNDEFINED
        card_three_times = CardValue.UNDEFINED
        for card in cards_sorted :
            number_cards = cards_sorted[card]
            if number_cards == 3 : 
                card_three_times = card
            elif number_cards == 2 : 
                card_two_times = card
            else : 
                break
        if card_two_times != CardValue.UNDEFINED and card_three_times != CardValue.UNDEFINED : 
            return FullFigure(card_two_times, card_three_times)
        else : 
            return None
    
    def __detect_flush(self, hand): 
        is_flush = True
        last_color = CardColor.UNDEFINED
        high_card_value = CardValue.TWO
        for card in hand : 
            if last_color == CardColor.UNDEFINED : 
                last_color = card.color 
            elif last_color != card.color : 
                is_flush = False
                break
            if high_card_value < card.value : 
                high_card_value = card.value
        if is_flush:
            return FlushFigure(last_color, high_card_value)
        else : 
            return None
    
    def __detect_straight(self, cards_sorted) : 
        cards_ordered = dict(sorted(cards_sorted.items()))
        high_card_value = CardValue.TWO
        is_ace_present = False
        if len(cards_ordered) == 5 :
            last_value = CardValue.UNDEFINED
            for card in cards_ordered :
                if card.value == CardValue.ACE :
                    is_ace_present = True
                    continue 
                high_card_value = card
                if last_value != CardValue.UNDEFINED : 
                    if card.value - last_value > 1 : 
                        return None
                last_value = card.value
            if is_ace_present == False or (is_ace_present and CardValue.TWO in cards_ordered): 
                return StraitFigure(high_card_value)
            elif is_ace_present and CardValue.KING in cards_ordered : 
                return StraitFigure(CardValue.ACE)
            else :
                return None
        else : 
            return None
        
    def __detect_three_of_kind(self, cards_sorted): 
        is_three_cards = False
        three_of_kind_value = CardValue.TWO
        high_value_outside_three_of_kind = CardValue.TWO
        for card in cards_sorted : 
            number_cards = cards_sorted[card]
            if number_cards == 3 : 
                is_three_cards = True
                three_of_kind_value = card
            else : 
                if card > high_value_outside_three_of_kind : 
                    high_value_outside_three_of_kind = card
        if is_three_cards : 
            return ThreeOfKindFigure(three_of_kind_value, high_value_outside_three_of_kind)
        else : 
            return None
        
    def __detect_two_pairs(self, cards_sorted): 
        is_two_pairs = False
        first_value_pair = CardValue.TWO
        second_value_pair = CardValue.TWO
        high_value_outside_two_pair = CardValue.TWO
        number_pair = 0
        for card in cards_sorted : 
            number_cards = cards_sorted[card]
            if number_cards == 2 : 
                number_pair = number_pair + 1 
                if number_pair == 1 :
                    first_value_pair = card
                else : 
                    is_two_pairs = True
                    if card > first_value_pair : 
                        second_value_pair = first_value_pair
                        first_value_pair = card
                    else : 
                        second_value_pair = card
            else : 
                if card > high_value_outside_two_pair : 
                    high_value_outside_two_pair = card
        if is_two_pairs : 
            return TwoPairFigure(first_value_pair, second_value_pair, high_value_outside_two_pair)
        else : 
            return None
        
    def __detect_one_pair(self, cards_sorted):
        is_one_pair = False
        value_pair = CardValue.TWO
        high_value_outside_one_pair = CardValue.TWO
        for card in cards_sorted : 
            number_cards = cards_sorted[card]
            if number_cards == 2 : 
                is_one_pair = True
                value_pair = card                
            else : 
                if card > high_value_outside_one_pair : 
                    high_value_outside_one_pair = card
        if is_one_pair : 
            return PairFigure(value_pair, high_value_outside_one_pair)
        
    def __detect_high_card_figure(self, cards_sorted): 
        high_value = CardValue.TWO
        for card in cards_sorted : 
            if high_value < card : 
                high_value = card
        return HighCardFigure(high_value)