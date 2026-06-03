from enum import Enum
from PokerHands.card import CardValue, CardColor
from PokerHands.Figure import StraitFigure, FlushFigure, FullFigure, FourOfKindFigure, QuinteFlush

class Hand :
    def __init__(self, high_cards_detector, pair_detector, two_pairs_detector, three_cards_detector, straight_detector):
        self.counting_cards = {}
        self.high_cards_detector = high_cards_detector
        self.pair_detector = pair_detector
        self.two_pairs_detector = two_pairs_detector
        self.three_cards_detector = three_cards_detector
        self.straight_detector = straight_detector
    
    def determinate_high_figure(self, hand):
        cards_sorted = self.__count_all_cards(hand)
        quinte_flush = self.__detect_quinte_flush(hand)
        four_a_kind = self.__detect_four_a_kind(cards_sorted)
        full_figure = self.__detect_full(cards_sorted)
        flush_figure = self.__detect_flush(hand)
        strait_figure = self.__detect_straight(hand)
        three_of_kind = self.__detect_three_of_kind(hand)
        two_pairs = self.__detect_two_pairs(hand)
        pair = self.__detect_one_pair(hand)
        high_card_figure = self.__detect_high_card_figure(hand)
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
    
    def __detect_straight(self, hand) : 
        return self.straight_detector.find_straight(hand)
        
    def __detect_three_of_kind(self, hand): 
        return self.three_cards_detector.find_three_of_kind(hand)
        
    def __detect_two_pairs(self, hand): 
        return self.two_pairs_detector.find_two_pairs(hand)
        
    def __detect_one_pair(self, hand):
        return self.pair_detector.find_pair(hand)
        
    def __detect_high_card_figure(self, hand): 
        return self.high_cards_detector.find_high_card(hand)