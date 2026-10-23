from dataclasses import dataclass, field
from PokerHands.card import Card

@dataclass(frozen=True)
class FlopResult: 
    flop_cards : list[Card]
    burn_card : Card
    players : dict[str, list[Card]] = field(default_factory=dict)
    
    @staticmethod
    def create(players, flop_cards, burn_card):
        return FlopResult(flop_cards, burn_card, players)
