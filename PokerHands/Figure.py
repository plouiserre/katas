from dataclasses import dataclass
from PokerHands.card import CardValue, CardColor
from typing import ClassVar

@dataclass(frozen=True)
class HighCardFigure : 
    value : CardValue
    points : ClassVar[int] = 10

@dataclass(frozen=True)
class PairFigure : 
    value : CardValue
    high_value_rest_of_cards: CardValue
    points : ClassVar[int] = 20

@dataclass(frozen=True)
class TwoPairFigure: 
    first_pair_value : CardValue
    second_pair_value : CardValue
    high_value_rest_of_cards: CardValue
    points : ClassVar[int] = 30

@dataclass(frozen=True)
class ThreeOfKindFigure : 
    value : CardValue
    high_value_rest_of_cards: CardValue
    points : ClassVar[int] = 40

@dataclass(frozen=True)
class StraitFigure:
    value : CardValue
    points : ClassVar[int] = 50

@dataclass(frozen=True)
class FlushFigure : 
    color : CardColor
    high_value : CardValue
    points : ClassVar[int] = 60

@dataclass(frozen=True)
class FullFigure : 
    two_times : CardValue
    three_times : CardValue
    points : ClassVar[int] = 70

@dataclass(frozen=True)
class FourOfKindFigure : 
    value : CardValue
    high_value_rest_of_cards: CardValue
    points : ClassVar[int] = 80

@dataclass(frozen=True)
class QuinteFlush : 
    value : CardValue
    color : CardColor
    points : ClassVar[int] = 90

Figure = HighCardFigure | PairFigure | TwoPairFigure | ThreeOfKindFigure | StraitFigure | FullFigure | FourOfKindFigure    