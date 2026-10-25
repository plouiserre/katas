from dataclasses import dataclass, field
from PokerHands.card import Card

@dataclass(frozen=True)
class TurnResult: 
    turn_card : Card
    burn_card : Card
    players : dict[str, list[Card]] = field(default_factory=dict)
    
    @staticmethod
    def create(players, turn_card, burn_card):
        return TurnResult(turn_card, burn_card, players)
