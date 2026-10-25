from PokerHands.card import Card, CardColor, CardValue
from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.hand.flop_phase import FlopPhase
from PokerHands.table.table import Table
from PokerHands.tests.fake_multi_draw_cards import FakeMultiDrawCards

def test_launch_flop_phase_with_two_players_randomly():
    (CompareHandsAfterFlopDriver(MultiDrawCards())
        .add_player("Steve")
        .add_player("Natacha")
        .add_card_before_flop("2♠", "Steve")
        .add_card_before_flop("A♥", "Natacha")
        .add_card_before_flop("6♠", "Steve")
        .add_card_before_flop("A♣", "Natacha")
        .launch_phase_and_get_flop_datas()
        .are_all_cards_dealed_unique()
        .is_one_card_burned()
        .is_three_cards_flopped()
        .is_this_players_have_five_cards_dealed("Steve")
        .is_this_players_have_five_cards_dealed("Natacha"))     

def test_launch_flop_phase_with_two_players_and_evaluate_flop_datas(): 
    fake_cards = ["K♥","A♠", "Q♠", "8♠"]
    (CompareHandsAfterFlopDriver(FakeMultiDrawCards(fake_cards))
        .add_player("Steve")
        .add_player("Natacha")
        .add_card_before_flop("2♠", "Steve")
        .add_card_before_flop("A♥", "Natacha")
        .add_card_before_flop("6♠", "Steve")
        .add_card_before_flop("A♣", "Natacha")
        .launch_phase_and_get_flop_datas()        
        .are_all_cards_dealed_unique()
        .is_one_card_burned()
        .is_three_cards_flopped()
        .is_this_players_have_five_cards_dealed("Steve")
        .is_this_players_have_five_cards_dealed("Natacha")
        .is_this_players_have_this_card("Steve", [Card(CardValue.TWO, CardColor.SPADES), Card(CardValue.SIX, CardColor.SPADES),Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.EIGHT, CardColor.SPADES)])        
        .is_this_players_have_this_card("Natacha", [Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.ACE, CardColor.CLUBS),Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.EIGHT, CardColor.SPADES)])
        .is_three_cards_flopped())  


def test_launch_flop_phase_with_ten_players_and_steve_wins():
    fake_cards = ["3♥","A♥", "6♦", "4♠"]
    (CompareHandsAfterFlopDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .add_card_before_flop("A♠", "Steve")
        .add_card_before_flop("K♣", "Natacha")
        .add_card_before_flop("Q♥", "Tony")
        .add_card_before_flop("J♦","Thor")
        .add_card_before_flop("10♣", "Bruce")
        .add_card_before_flop("9♦", "Clint")
        .add_card_before_flop("8♥", "Carol")
        .add_card_before_flop("7♠", "T'Challa")
        .add_card_before_flop("6♣", "Steven")
        .add_card_before_flop("5♦", "Wanda")
        .add_card_before_flop("4♥", "Steve")
        .add_card_before_flop("3♠", "Natacha")
        .add_card_before_flop("2♣","Tony")
        .add_card_before_flop("A♦", "Thor")
        .add_card_before_flop("K♥", "Bruce")
        .add_card_before_flop("Q♠", "Clint")
        .add_card_before_flop("J♣", "Carol")
        .add_card_before_flop("10♦", "T'Challa")
        .add_card_before_flop("9♥", "Steven")
        .add_card_before_flop("8♠", "Wanda")
        .launch_phase_and_get_flop_datas()        
        .are_all_cards_dealed_unique()
        .is_one_card_burned()
        .is_three_cards_flopped()
        .is_this_players_have_five_cards_dealed("Steve")
        .is_this_players_have_five_cards_dealed("Natacha")
        .is_this_players_have_five_cards_dealed("Tony")
        .is_this_players_have_five_cards_dealed("Thor")
        .is_this_players_have_five_cards_dealed("Bruce")
        .is_this_players_have_five_cards_dealed("Clint")
        .is_this_players_have_five_cards_dealed("Carol")
        .is_this_players_have_five_cards_dealed("T'Challa")
        .is_this_players_have_five_cards_dealed("Steven") 
        .is_this_players_have_this_card("Steve", [Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.FOUR, CardColor.HEARTS),Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES)])
        .is_this_players_have_this_card("Natacha", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.THREE, CardColor.SPADES),Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES)])
        .is_this_players_have_this_card("Tony", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.TWO, CardColor.CLUBS),Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES)])
        .is_this_players_have_this_card("Thor", [Card(CardValue.JACK, CardColor.DIAMONDS), Card(CardValue.ACE, CardColor.DIAMONDS),Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES)])
        .is_this_players_have_this_card("Bruce", [Card(CardValue.TEN, CardColor.CLUBS), Card(CardValue.KING, CardColor.HEARTS),Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES)])
        .is_this_players_have_this_card("Clint", [Card(CardValue.NINE, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.SPADES),Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES)])
        .is_this_players_have_this_card("Carol", [Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.JACK, CardColor.CLUBS),Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES)])
        .is_this_players_have_this_card("T'Challa", [Card(CardValue.SEVEN, CardColor.SPADES), Card(CardValue.TEN, CardColor.DIAMONDS),Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES)])
        .is_this_players_have_this_card("Steven", [Card(CardValue.SIX, CardColor.CLUBS), Card(CardValue.NINE, CardColor.HEARTS),Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES)])
        .is_this_players_have_this_card("Wanda", [Card(CardValue.FIVE, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.SPADES),Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES)]))


class CompareHandsAfterFlopDriver():
    def __init__(self, multi_draw_cards):
        self.multi_draw_cards = multi_draw_cards
        self.table = Table(self.multi_draw_cards)
        self.flop_datas = None

    def add_player(self, player_name):
        self.table.add_player(player_name)
        return self

    def add_players(self, players_name): 
        for player_name in players_name:
            self.table.add_player(player_name)
        return self

    def add_card_before_flop(self, card_crypted, player_name):
        card = Card.parse(card_crypted)
        self.table.affect_card_to_player(player_name, card)
        return self

    def launch_phase_and_get_flop_datas(self):
        self.flop_phase = FlopPhase(self.table)
        self.flop_datas = self.flop_phase.launch_phase_and_get_all_flop_datas()
        return self  

    def is_three_cards_flopped(self): 
        assert(len(self.flop_datas.flop_cards) == 3)
        return self

    def is_one_card_burned(self): 
        assert(self.flop_datas.burn_card != Card(CardValue.UNDEFINED, CardColor.UNDEFINED))
        return self

    def all_cards_are_differents(self): 
        all_cards = []
        for card_player in self.cards_given_players : 
            all_cards.append(card_player)
        for flop_card in self.flop_phase.cards_returned : 
            all_cards.append(flop_card)
        all_cards.append(self.flop_phase.card_burn)
        all_cards_drawn_unique = set(all_cards)
        assert(len(all_cards) == len(all_cards_drawn_unique))

    def is_this_players_have_five_cards_dealed(self, player_name): 
        assert (len(self.flop_datas.players[player_name]) == 5)
        return self    

    def is_this_players_have_this_card(self, player_name, cards_expected): 
        is_ok = True
        for idx, card_expected in enumerate(cards_expected):
            card = self.flop_datas.players[player_name][idx]
            if card.value != card_expected.value or card.color != card_expected.color : 
                is_ok = False
                break
        assert(is_ok == True)
        return self

    def are_all_cards_dealed_unique(self):
        all_cards = []
        for card in self.flop_datas.flop_cards : 
                all_cards.append(card)
        all_cards.append(self.flop_datas.burn_card)
        cards_draw_unique_element = set(all_cards)
        assert (len(all_cards) == len(cards_draw_unique_element))
        return self