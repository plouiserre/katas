from PokerHandsV2.card import Card
from PokerHandsV2.draw.draw_cards_texas_holdem import DrawCardsTexasHoldem
from dataclasses import dataclass

def test_draw_all_cards_need_for_two_players_in_poker_texas_holdem(): 
    (DrawCardsTexasHoldemDriver()
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
        .is_player_have_all_cards("Bruce")
        .is_player_have_all_cards("Diana")
        .is_cards_on_table_are_completed()
        .is_cards_burned_are_completed()
        .is_cards_drawned_are_uniqued())
    
def test_draw_all_cards_need_for_six_players_in_poker_texas_holdem(): 
    (DrawCardsTexasHoldemDriver()
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
        .is_player_have_all_cards("Bruce")
        .is_player_have_all_cards("Diana")
        .is_player_have_all_cards("Clark")
        .is_player_have_all_cards("Selina")
        .is_player_have_all_cards("Barry")
        .is_player_have_all_cards("Zatana")        
        .is_cards_on_table_are_completed()
        .is_cards_burned_are_completed()
        .is_cards_drawned_are_uniqued())    

class DrawCardsTexasHoldemDriver : 
    def __init__(self):
        self.draw_cards_texas_holdem = DrawCardsTexasHoldem()
        self.cards = None

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
        self.cards = Cards(all_players, all_cards_on_table, burns_cards)
        return self

    def is_player_have_all_cards(self, player_name_search):
        cards_search = []
        for player_name in self.cards.players : 
            if player_name == player_name_search:
                cards_search = self.cards.players[player_name]
        assert(len(cards_search) == 2)
        return self

    def is_cards_on_table_are_completed(self):
        assert(len(self.cards.cards_on_table) == 5)
        return self

    def is_cards_burned_are_completed(self):
        assert(len(self.cards.burn_cards) == 3)
        return self

    def is_cards_burned_are_uniqued(self):
        is_burn_card_ok = True
        for card in self.cards.burn_cards :
            is_burn_card_ok = card not in self.cards.players["Bruce"] and card not in self.cards.players["Diana"] and card not in self.cards.cards_on_table
            if is_burn_card_ok == False : 
                break
        assert(is_burn_card_ok)

    def is_cards_drawned_are_uniqued(self):
        all_cards_drawn = []
        for player_name in self.cards.players : 
            for card in self.cards.players[player_name]:
                all_cards_drawn.append(card)
        for card in self.cards.cards_on_table : 
            all_cards_drawn.append(card)
        all_cards_drawn_unique = set(all_cards_drawn)
        assert (len(all_cards_drawn) == len(all_cards_drawn_unique))

@dataclass(frozen=True)
class Cards :
    players : dict[str, list[Card]]
    cards_on_table : list[Card]
    burn_cards  : list[Card]