from dataclasses import dataclass
from PokerHands.card import CardValue, CardColor
from typing import ClassVar

@dataclass(frozen=True)
class TwoPairFigure: 
    first_pair_value : CardValue
    second_pair_value : CardValue
    high_value_rest_of_cards: CardValue
    points : ClassVar[int] = 30