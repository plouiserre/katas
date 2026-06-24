from dataclasses import dataclass
from PokerHands.card import CardValue
from typing import ClassVar

@dataclass(frozen=True)
class FullFigure : 
    two_times : CardValue
    three_times : CardValue
    points : ClassVar[int] = 70