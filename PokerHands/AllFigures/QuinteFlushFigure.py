from dataclasses import dataclass
from PokerHands.card import CardValue, CardColor
from typing import ClassVar

@dataclass(frozen=True)
class QuinteFlushFigure : 
    value : CardValue
    color : CardColor
    points : ClassVar[int] = 90