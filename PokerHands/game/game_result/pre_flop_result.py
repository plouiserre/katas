from dataclasses import dataclass, field
from PokerHands.card import Card

@dataclass(frozen=True)
class PreFlopResult: 
    players : dict[str, list[Card]] = field(default_factory=dict)

    @staticmethod
    def create(players):
        return PreFlopResult(players)
