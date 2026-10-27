from PokerHands.card import Card
from PokerHands.AllFigures.Figure import Figure
from PokerHands.AllFigures.FlushFigure import FlushFigure
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure
from PokerHands.AllFigures.FullFigure import FullFigure
from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.AllFigures.QuinteFigure import QuinteFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from typing import Iterator

class Combination :
    def __init__(self, high_cards_detector, pair_detector, two_pairs_detector, three_cards_detector, quinte_detector, flush_detector, full_detector, four_cards_detector, quinte_flush_detector):
        self.counting_cards = {}
        self.high_cards_detector = high_cards_detector
        self.pair_detector = pair_detector
        self.two_pairs_detector = two_pairs_detector
        self.three_cards_detector = three_cards_detector
        self.quinte_detector = quinte_detector
        self.flush_detector = flush_detector
        self.full_detector = full_detector
        self.four_cards_detector = four_cards_detector
        self.quinte_flush_detector = quinte_flush_detector
    
    def determinate_high_figure(self, combination : Iterator[Card]) -> Figure:
        quinte_flush = self.__detect_quinte_flush(combination)
        four_a_kind = self.__detect_four_a_kind(combination)
        full_figure = self.__detect_full(combination)
        flush_figure = self.__detect_flush(combination)
        quinte_figure = self.__detect_quinte(combination)
        three_of_kind = self.__detect_three_of_kind(combination)
        two_pairs = self.__detect_two_pairs(combination)
        pair = self.__detect_one_pair(combination)
        high_card_figure = self.__detect_high_card_figure(combination)
        if quinte_flush != None : 
            return quinte_flush
        elif four_a_kind != None : 
            return four_a_kind
        elif full_figure != None : 
            return full_figure
        elif flush_figure != None : 
            return flush_figure
        elif quinte_figure != None : 
            return quinte_figure
        elif three_of_kind != None : 
            return three_of_kind
        elif two_pairs != None : 
            return two_pairs
        elif pair != None : 
            return pair
        else : 
            return high_card_figure 

    def __detect_quinte_flush(self, combination: Iterator[Card]) -> QuinteFlushFigure:
        return self.quinte_flush_detector.find_quinte_flush(combination)
    
    def __detect_four_a_kind(self, combination: Iterator[Card]) -> FourOfKindFigure:
        return self.four_cards_detector.find_four_cards(combination)
    
    def __detect_full(self, combination: Iterator[Card]) -> FullFigure:
        return self.full_detector.find_full(combination)
    
    def __detect_flush(self, combination: Iterator[Card]) -> FlushFigure: 
        return self.flush_detector.find_flush(combination)
    
    def __detect_quinte(self, combination: Iterator[Card]) -> QuinteFigure: 
        return self.quinte_detector.find_quinte(combination)
        
    def __detect_three_of_kind(self, combination: Iterator[Card]) -> ThreeOfKindFigure: 
        return self.three_cards_detector.find_three_of_kind(combination)
        
    def __detect_two_pairs(self, combination: Iterator[Card]) -> TwoPairFigure: 
        return self.two_pairs_detector.find_two_pairs(combination)
        
    def __detect_one_pair(self, combination: Iterator[Card]) -> PairFigure:
        return self.pair_detector.find_pair(combination)
        
    def __detect_high_card_figure(self, combination: Iterator[Card]) -> HighCardFigure: 
        return self.high_cards_detector.find_high_card(combination)