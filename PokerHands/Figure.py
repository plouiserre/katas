from dataclasses import dataclass
from PokerHands.card import CardValue, CardColor

@dataclass(frozen=True)
class HighCardFigure : 
    value : CardValue

@dataclass(frozen=True)
class PairFigure : 
    value : CardValue
    high_value_rest_of_cards: CardValue

@dataclass(frozen=True)
class TwoPairFigure: 
    value : CardValue
    second_pair_value : CardValue
    high_value_rest_of_cards: CardValue

@dataclass(frozen=True)
class ThreeOfKindFigure : 
    value : CardValue
    high_value_rest_of_cards: CardValue

@dataclass(frozen=True)
class StraitFigure:
    value : CardValue

@dataclass(frozen=True)
class FlushFigure : 
    color : CardColor
    high_value : CardValue

@dataclass(frozen=True)
class FullFigure : 
    two_times : CardValue
    three_times : CardValue

@dataclass(frozen=True)
class FourOfKindFigure : 
    value : CardValue
    high_value_rest_of_cards: CardValue

@dataclass(frozen=True)
class QuinteFlush : 
    value : CardValue
    color : CardColor

Figure = HighCardFigure | PairFigure | TwoPairFigure | ThreeOfKindFigure | StraitFigure | FullFigure | FourOfKindFigure    