from PokerHands.card import CardColor, CardValue
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure

class QuinteFlushDetector : 
    def __init__(self):
        self.is_quinte_flush = True 
        self.last_card_color = CardColor.UNDEFINED
        self.last_card_value = CardValue.UNDEFINED
        self.is_ace_present = False
        self.card_value_hand = []        

    def find_quinte_flush(self, hand):        
        hand_sorted = sorted(hand, key=lambda o : o.value)
        self.__determine_if_hand_contains_quinte_flush(hand_sorted)
        if self.is_quinte_flush : 
            return self.__construct_quinte_flush()
        else : 
            return None    
        
    def __construct_quinte_flush(self): 
        if self.is_ace_present == False : 
            return QuinteFlushFigure(self.last_card_value, self.last_card_color)
        elif self.is_ace_present and CardValue.TWO in self.card_value_hand : 
            return QuinteFlushFigure(CardValue.FIVE, self.last_card_color)
        elif self.is_ace_present and CardValue.KING in self.card_value_hand : 
            return QuinteFlushFigure(CardValue.ACE, self.last_card_color)
        
    def __determine_if_hand_contains_quinte_flush(self, hand_sorted):
        for card in hand_sorted : 
            if card.value == CardValue.ACE : 
                self.is_ace_present = True
            if self.last_card_color == CardColor.UNDEFINED  and self.last_card_value == CardValue.UNDEFINED:
                self.last_card_color = card.color
                self.last_card_value = card.value
                self.card_value_hand.append(card.value)
                continue
            elif self.last_card_color != card.color : 
                self.is_quinte_flush = False
                break
            elif self.is_ace_present and (CardValue.KING not in self.card_value_hand and CardValue.TWO not in self.card_value_hand): 
                self.is_quinte_flush = False
                break
            elif card.value != CardValue.ACE and (card.value - self.last_card_value > 1 or card.value in self.card_value_hand): 
                self.is_quinte_flush = False
                break
            else : 
                self.last_card_value = card.value
            self.card_value_hand.append(card.value)