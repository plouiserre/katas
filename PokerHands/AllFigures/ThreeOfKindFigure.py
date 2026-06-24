from dataclasses import dataclass
from PokerHands.card import CardValue, CardColor
from typing import ClassVar

@dataclass(frozen=True)
class ThreeOfKindFigure : 
    value : CardValue
    high_value_rest_of_cards: CardValue
    points : ClassVar[int] = 40