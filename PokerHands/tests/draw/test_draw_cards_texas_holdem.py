from PokerHands.card import Card
from PokerHands.draw.draw_cards_texas_holdem import DrawCardsTexasHoldem
from dataclasses import dataclass

def test_draw_all_cards_need_for_two_players_in_poker_texas_holdem(): 
    cards = (
        DrawCardsTexasHoldemDriver()
            .add_one_player("Bruce")
            .add_one_player("Diana")
            .give_one_card_for_one_player("Bruce")
            .give_one_card_for_one_player("Diana")
            .give_one_card_for_one_player("Bruce")
            .give_one_card_for_one_player("Diana")
            .burn_one_card()
            .draw_flop_cards()
            .burn_one_card()
            .draw_turn_card()
            .burn_one_card()
            .draw_river_card()
            .get_all_cards_choosen()
    )
    is_burn_card_ok = True
    all_cards_drawn = __get_all_cards_drawn(cards)
    all_cards_drawn_unique = set(all_cards_drawn)
    assert(len(cards.players["Bruce"]) == 2)
    assert(len(cards.players["Diana"]) == 2)
    assert(len(cards.cards_on_table) == 5)
    assert (len(cards.burn_cards) == 3)
    for card in cards.burn_cards :
        is_burn_card_ok = card not in cards.players["Bruce"] and card not in cards.players["Diana"] and card not in cards.cards_on_table
        if is_burn_card_ok == False : 
            break
    assert (is_burn_card_ok == True)
    assert (len(all_cards_drawn) == len(all_cards_drawn_unique))


def test_draw_all_cards_need_for_six_players_in_poker_texas_holdem(): 
    cards = (
        DrawCardsTexasHoldemDriver()
            .add_one_player("Bruce")
            .add_one_player("Diana")
            .add_one_player("Clark")
            .add_one_player("Selina")
            .add_one_player("Barry")
            .add_one_player("Zatana")
            .give_one_card_for_one_player("Bruce")
            .give_one_card_for_one_player("Diana")
            .give_one_card_for_one_player("Clark")
            .give_one_card_for_one_player("Selina")
            .give_one_card_for_one_player("Barry")
            .give_one_card_for_one_player("Zatana")
            .give_one_card_for_one_player("Bruce")
            .give_one_card_for_one_player("Diana")
            .give_one_card_for_one_player("Clark")
            .give_one_card_for_one_player("Selina")
            .give_one_card_for_one_player("Barry")
            .give_one_card_for_one_player("Zatana")
            .burn_one_card()
            .draw_flop_cards()
            .burn_one_card()
            .draw_turn_card()
            .burn_one_card()
            .draw_river_card()
            .get_all_cards_choosen()
    )
    is_burn_card_ok = True
    all_cards_drawn = __get_all_cards_drawn(cards)
    all_cards_drawn_unique = set(all_cards_drawn)
    assert(len(cards.players["Bruce"]) == 2)
    assert(len(cards.players["Diana"]) == 2)
    assert(len(cards.players["Clark"]) == 2)
    assert(len(cards.players["Selina"]) == 2)
    assert(len(cards.players["Barry"]) == 2)
    assert(len(cards.players["Zatana"]) == 2)
    assert(len(cards.cards_on_table) == 5)
    assert (len(cards.burn_cards) == 3)
    for card in cards.burn_cards :
        is_burn_card_ok = card not in cards.players["Bruce"] and card not in cards.players["Diana"] and card not in cards.players["Clark"] and card not in cards.players["Selina"] and card not in cards.players["Barry"] and card not in cards.players["Zatana"] and card not in cards.cards_on_table 
        if is_burn_card_ok == False : 
            break
    assert (is_burn_card_ok == True)
    assert (len(all_cards_drawn) == len(all_cards_drawn_unique))
        

def __get_all_cards_drawn(cards):
    all_cards_drawn = []
    for player_name in cards.players : 
        for card in cards.players[player_name]:
            all_cards_drawn.append(card)
    for card in cards.cards_on_table : 
        all_cards_drawn.append(card)
    return all_cards_drawn

class DrawCardsTexasHoldemDriver : 
    def __init__(self):
        self.draw_cards_texas_holdem = DrawCardsTexasHoldem()

    def add_one_player(self, name_player):
        self.draw_cards_texas_holdem.add_players(name_player)
        return self

    def give_one_card_for_one_player(self, name_player):
        self.draw_cards_texas_holdem.draw_one_card_for_one_player(name_player)
        return self

    def burn_one_card(self):
        self.draw_cards_texas_holdem.burn_card()
        return self

    def draw_flop_cards(self):
        self.draw_cards_texas_holdem.draw_flop_cards()
        return self

    def draw_turn_card(self):
        self.draw_cards_texas_holdem.draw_turn_card()
        return self

    def draw_river_card(self):
        self.draw_cards_texas_holdem.draw_river_card()
        return self

    def get_all_cards_choosen(self):
        all_players = self.draw_cards_texas_holdem.get_players()
        all_cards_on_table = self.draw_cards_texas_holdem.get_all_cards_on_table()
        burns_cards = self.draw_cards_texas_holdem.get_all_burns_cards()
        return Cards(all_players, all_cards_on_table, burns_cards)

@dataclass(frozen=True)
class Cards :
    players : dict[str, list[Card]]
    cards_on_table : list[Card]
    burn_cards  : list[Card]