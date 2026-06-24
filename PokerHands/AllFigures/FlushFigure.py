from dataclasses import dataclass
from PokerHands.card import CardValue, CardColor
from typing import ClassVar

@dataclass(frozen=True)
class FlushFigure : 
    color : CardColor
    high_value : CardValue
    points : ClassVar[int] = 60