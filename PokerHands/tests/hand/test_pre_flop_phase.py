import pytest

from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.hand.pre_flop_phase import PreFlopPhase
from PokerHands.table.table import Table
from PokerHands.tests.fake_multi_draw_cards import FakeMultiDrawCards

def test_launch_pre_flop_phase_with_two_players_randomly(): 
    (DrawAndComparePlayersPokerHandDriver(MultiDrawCards())
        .add_players(["Steve","Natacha"])    
        .launch_pre_flop_phase_and_get_preflop_datas()
        .are_all_cards_dealed_unique()
        .is_this_players_have_two_cards_dealed("Steve")
        .is_this_players_have_two_cards_dealed("Natacha"))
    
def test_launch_pre_flop_phase_with_two_players_and_check_preflop_data(): 
    fake_cards = ["K♣","Q♥","Q♦","7♠"]
    (DrawAndComparePlayersPokerHandDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha"])    
        .launch_pre_flop_phase_and_get_preflop_datas()
        .are_all_cards_dealed_unique()
        .is_this_players_have_two_cards_dealed("Steve")
        .is_this_players_have_two_cards_dealed("Natacha")
        .is_this_players_have_this_card("Steve", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)])
        .is_this_players_have_this_card("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.SEVEN, CardColor.SPADES)]))

def test_launch_pre_flop_phase_with_ten_players_and_check_preflop_data():
    fake_cards = ["7♣", "K♥", "J♣", "10♥", "K♣", "2♥", "A♥", "A♦", "3♠", "K♠", "6♦", "Q♠", "10♦", "9♠", "Q♦", "4♠","A♠", "Q♣", "4♣", "K♦"] 
    (DrawAndComparePlayersPokerHandDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .launch_pre_flop_phase_and_get_preflop_datas()
        .are_all_cards_dealed_unique()
        .is_this_players_have_two_cards_dealed("Steve")
        .is_this_players_have_two_cards_dealed("Natacha")
        .is_this_players_have_two_cards_dealed("Tony")
        .is_this_players_have_two_cards_dealed("Thor")
        .is_this_players_have_two_cards_dealed("Bruce")
        .is_this_players_have_two_cards_dealed("Clint")
        .is_this_players_have_two_cards_dealed("Carol")
        .is_this_players_have_two_cards_dealed("T'Challa")
        .is_this_players_have_two_cards_dealed("Steven")
        .is_this_players_have_two_cards_dealed("Wanda")                
        .is_this_players_have_this_card("Steve", [Card(CardValue.SEVEN, CardColor.CLUBS), Card(CardValue.SIX, CardColor.DIAMONDS)])
        .is_this_players_have_this_card("Natacha", [Card(CardValue.KING, CardColor.HEARTS), Card(CardValue.QUEEN, CardColor.SPADES)])
        .is_this_players_have_this_card("Tony", [Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.TEN, CardColor.DIAMONDS)])
        .is_this_players_have_this_card("Thor", [Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.NINE, CardColor.SPADES)])
        .is_this_players_have_this_card("Bruce", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.QUEEN, CardColor.DIAMONDS)])
        .is_this_players_have_this_card("Clint", [Card(CardValue.TWO, CardColor.HEARTS), Card(CardValue.FOUR, CardColor.SPADES)])
        .is_this_players_have_this_card("Carol",[Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.ACE, CardColor.SPADES)])
        .is_this_players_have_this_card("T'Challa", [Card(CardValue.ACE, CardColor.DIAMONDS), Card(CardValue.QUEEN, CardColor.CLUBS)])
        .is_this_players_have_this_card("Steven", [Card(CardValue.THREE, CardColor.SPADES), Card(CardValue.FOUR, CardColor.CLUBS)])
        .is_this_players_have_this_card("Wanda", [Card(CardValue.KING, CardColor.SPADES), Card(CardValue.KING, CardColor.DIAMONDS)]))

class DrawAndComparePlayersPokerHandDriver():
    def __init__(self, multidrawcards):
        self.players = []
        self.multi_draw_cards = multidrawcards
        self.table = Table(self.multi_draw_cards)
        self.preflop_data = None
        
    def add_players(self, name_players):
        for name_player in name_players:
            self.players.append(name_player)
        return self

    def launch_pre_flop_phase_and_get_preflop_datas(self):
        self.pre_flop_phase = PreFlopPhase(self.players, self.table)
        self.preflop_data =  self.pre_flop_phase.launch_phase_and_get_all_pre_flop_datas()
        return self

    def is_this_players_have_this_card(self, player_name, cards_expected): 
        is_ok = True
        for idx, card_expected in enumerate(cards_expected):
            card = self.preflop_data.players[player_name][idx]
            if card.value != card_expected.value or card.color != card_expected.color : 
                is_ok = False
                break
        assert(is_ok == True)
        return self

    def is_this_players_have_two_cards_dealed(self, player_name): 
        assert (len(self.preflop_data.players[player_name]) == 2)
        return self

    def are_all_cards_dealed_unique(self):
            all_cards = []
            for player_name in self.table.players : 
                 for card in self.table.players[player_name]:
                      all_cards.append(card)
            cards_draw_unique_element = set(all_cards)
            assert (len(all_cards) == len(cards_draw_unique_element))
            return self