from dataclasses import dataclass
from PokerHands.card import CardValue

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

Figure = HighCardFigure | PairFigure | TwoPairFigure | ThreeOfKindFigure | StraitFigure

    