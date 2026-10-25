from PokerHands.card import Card, CardColor, CardValue
from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.game.river_phase import RiverPhase
from PokerHands.table.table import Table
from PokerHands.tests.assert_helper import is_this_two_figure_are_equal
from PokerHands.tests.fake_multi_draw_cards import FakeMultiDrawCards

def test_launch_river_phase_with_two_players_randomly():
    (RiverPhaseDriver(MultiDrawCards())
        .add_player("Steve")
        .add_player("Natacha")
        .add_card_before_flop_phase("2♠", "Steve")
        .add_card_before_flop_phase("A♥", "Natacha")
        .add_card_before_flop_phase("6♠", "Steve")
        .add_card_before_flop_phase("A♣", "Natacha")
        .burn_one_card("K♦")
        .add_card_flop_phase("2♥")
        .add_card_flop_phase("2♦")
        .add_card_flop_phase("A♠")
        .burn_one_card("7♦")
        .add_card_turn_phase("A♠")
        .launch_phase_and_get_river_datas()
        .all_cards_are_differents()
        .is_three_cards_burned()
        .is_this_players_have_seven_cards_dealed("Steve")
        .is_this_players_have_seven_cards_dealed("Natacha"))

def test_launch_turn_phase_with_two_players_and_analyse_turn_datas():
    false_cards = ["8♥","9♣"]
    (RiverPhaseDriver(FakeMultiDrawCards(false_cards))
        .add_player("Steve")
        .add_player("Natacha")
        .add_card_before_flop_phase("2♠", "Steve")
        .add_card_before_flop_phase("A♥", "Natacha")
        .add_card_before_flop_phase("6♠", "Steve")
        .add_card_before_flop_phase("A♣", "Natacha")
        .burn_one_card("K♦")                            
        .add_card_flop_phase("2♥")
        .add_card_flop_phase("2♦")
        .add_card_flop_phase("A♠")
        .burn_one_card("3♠")
        .add_card_turn_phase("2♣")
        .launch_phase_and_get_river_datas()
        .all_cards_are_differents()
        .is_three_cards_burned()
        .is_this_players_have_seven_cards_dealed("Steve")
        .is_this_players_have_seven_cards_dealed("Natacha")
        .is_this_players_have_this_card("Steve", [Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.SIX, CardColor.SPADES),Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.NINE, CardColor.CLUBS)])
        .is_this_players_have_this_card("Natacha", [Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.ACE, CardColor.CLUBS),Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.TWO, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.NINE, CardColor.CLUBS)]))

def test_launch_turn_phase_with_ten_players_and_analyse_turn_datas():
    fake_cards = ["10♥","J♠"]
    (RiverPhaseDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .add_card_before_flop_phase("A♠", "Steve")
        .add_card_before_flop_phase("K♣", "Natacha")
        .add_card_before_flop_phase("Q♥", "Tony")
        .add_card_before_flop_phase("J♦","Thor")
        .add_card_before_flop_phase("10♣", "Bruce")
        .add_card_before_flop_phase("9♦", "Clint")
        .add_card_before_flop_phase("8♥", "Carol")
        .add_card_before_flop_phase("7♠", "T'Challa")
        .add_card_before_flop_phase("6♣", "Steven")
        .add_card_before_flop_phase("5♦", "Wanda")
        .add_card_before_flop_phase("4♥", "Steve")
        .add_card_before_flop_phase("3♠", "Natacha")
        .add_card_before_flop_phase("2♣","Tony")
        .add_card_before_flop_phase("A♦", "Thor")
        .add_card_before_flop_phase("7♥", "Bruce")
        .add_card_before_flop_phase("Q♠", "Clint")
        .add_card_before_flop_phase("J♣", "Carol")
        .add_card_before_flop_phase("10♦", "T'Challa")
        .add_card_before_flop_phase("9♥", "Steven")
        .add_card_before_flop_phase("8♠", "Wanda")               
        .add_card_flop_phase("5♥")
        .add_card_flop_phase("8♦")
        .add_card_flop_phase("4♠")
        .burn_one_card("3♥")
        .add_card_turn_phase("5♠")
        .launch_phase_and_get_river_datas()
        .all_cards_are_differents()
        .is_three_cards_burned()
        .is_this_players_have_seven_cards_dealed("Steve")
        .is_this_players_have_seven_cards_dealed("Natacha")
        .is_this_players_have_seven_cards_dealed("Tony")
        .is_this_players_have_seven_cards_dealed("Thor")
        .is_this_players_have_seven_cards_dealed("Bruce")
        .is_this_players_have_seven_cards_dealed("Clint")
        .is_this_players_have_seven_cards_dealed("Carol")
        .is_this_players_have_seven_cards_dealed("T'Challa")
        .is_this_players_have_seven_cards_dealed("Steven")                                                                    
        .is_this_players_have_this_card("Steve", [Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.FOUR, CardColor.HEARTS),Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)])
        .is_this_players_have_this_card("Natacha", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.THREE, CardColor.SPADES),Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)])
        .is_this_players_have_this_card("Tony", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.TWO, CardColor.CLUBS), Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)])
        .is_this_players_have_this_card("Thor", [Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS),Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)])
        .is_this_players_have_this_card("Bruce", [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.SEVEN, CardColor.HEARTS),Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)])
        .is_this_players_have_this_card("Clint", [Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.SPADES),Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)])
        .is_this_players_have_this_card("Carol", [Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.JACK, CardColor.CLUBS),Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)])
        .is_this_players_have_this_card("T'Challa", [Card(CardValue.SEVEN, CardColor.SPADES), Card(CardValue.TEN, CardColor.DIAMONDS),Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)])
        .is_this_players_have_this_card("Steven", [Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.NINE, CardColor.HEARTS),Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)])
        .is_this_players_have_this_card("Wanda", [Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.SPADES),Card(CardValue.FIVE, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES), Card(CardValue.FIVE, CardColor.SPADES), Card(CardValue.JACK, CardColor.SPADES)]))

    
class RiverPhaseDriver():
    def __init__(self, multi_draw_cards):
        self.table = Table(multi_draw_cards)
        self.river_phase = None
        self.burn_cards = []

    def add_player(self, player_name):
        self.table.add_player(player_name)
        return self
    
    def add_players(self, players_name): 
        for player_name in players_name:
            self.table.add_player(player_name)
        return self 
    
    def burn_one_card(self, card_crypted):
        card = Card.parse(card_crypted)
        self.burn_cards.append(card)
        return self

    def add_card_before_flop_phase(self, card_crypted, player_name):
        card = Card.parse(card_crypted)
        self.table.affect_card_to_player(player_name, card)
        return self

    def add_card_flop_phase(self, card_crypted):
        card = Card.parse(card_crypted)
        for player_name in self.table.players : 
            self.table.affect_card_to_player(player_name, card)
        return self

    def add_card_turn_phase(self, card_encrypted):
        card = Card.parse(card_encrypted)
        for player_name in self.table.players:
            self.table.affect_card_to_player(player_name, card)
        return self

    def launch_phase_and_get_river_datas(self):
        self.river_phase = RiverPhase(self.table)
        self.river_datas = self.river_phase.launch_phase_and_get_all_river_datas()
        return self

    def is_three_cards_burned(self): 
        self.burn_cards.append(self.river_phase.card_burn)
        for burn_card in self.burn_cards : 
            assert(burn_card != Card(CardValue.UNDEFINED, CardColor.UNDEFINED))
        return self

    def is_this_players_have_seven_cards_dealed(self, player_name): 
        assert (len(self.river_datas.players[player_name]) == 7)
        return self

    def all_cards_are_differents(self): 
        all_cards = []
        all_cards.append(self.river_datas.river_card)
        all_cards.append(self.river_datas.burn_card)
        all_cards_drawn_unique = set(all_cards)
        assert(len(all_cards) == len(all_cards_drawn_unique))
        return self

    def is_this_players_have_this_card(self, player_name, cards_expected): 
        is_ok = True
        for idx, card_expected in enumerate(cards_expected):
            card = self.river_datas.players[player_name][idx]
            if card.value != card_expected.value or card.color != card_expected.color : 
                is_ok = False
                break
        assert(is_ok == True)
        return self    