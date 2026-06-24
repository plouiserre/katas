from dataclasses import dataclass
from PokerHands.card import CardValue
from typing import ClassVar

@dataclass(frozen=True)
class HighCardFigure : 
    value : CardValue
    points : ClassVar[int] = 10