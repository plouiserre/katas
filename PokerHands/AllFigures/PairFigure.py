from dataclasses import dataclass
from PokerHands.card import CardValue
from typing import ClassVar

@dataclass(frozen=True)
class PairFigure : 
    value : CardValue
    high_value_rest_of_cards: CardValue
    points : ClassVar[int] = 20