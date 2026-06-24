from dataclasses import dataclass
from PokerHands.card import CardValue, CardColor
from typing import ClassVar

@dataclass(frozen=True)
class StraitFigure:
    value : CardValue
    points : ClassVar[int] = 50