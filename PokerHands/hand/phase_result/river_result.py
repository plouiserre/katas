from dataclasses import dataclass, field
from PokerHands.card import Card

@dataclass(frozen=True)
class RiverResult: 
    river_card : Card
    burn_card : Card
    players : dict[str, list[Card]] = field(default_factory=dict)
    
    @staticmethod
    def create(players, river_card, burn_card):
        return RiverResult(river_card, burn_card, players)
