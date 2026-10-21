from PokerHands.card import Card, CardColor, CardValue
from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.hand.table import Table
from PokerHands.tests.fake_multi_draw_cards import FakeMultiDrawCards

#TODO one test everything random without burn and add cards from board
def test_1():
    (TableDriver(MultiDrawCards() )
            .add_player("Steve")
            .add_player("Natacha")
            .add_player("Tony")
            .add_player("Thor")
            .deal_card("Steve")
            .deal_card("Natacha")
            .deal_card("Tony")
            .deal_card("Thor")
            .deal_card("Steve")
            .deal_card("Natacha")
            .deal_card("Tony")
            .deal_card("Thor")
            .is_valid_player("Steve")
            .is_valid_player("Natacha")
            .is_valid_player("Tony")
            .is_valid_player("Thor")
            .is_this_player_have_his_dealing_cards("Steve")
            .is_this_player_have_his_dealing_cards("Natacha")
            .is_this_player_have_his_dealing_cards("Tony")
            .is_this_player_have_his_dealing_cards("Thor")
            .valid_all_cards_draw_are_unique())

#TODO one test everything determinist without burn and add cards from board
def test_2():
    fake_cards = ["K♣","Q♥","Q♦","J♠", "J♣","10♥","10♦","9♠"]
    (TableDriver(FakeMultiDrawCards(fake_cards) )
            .add_player("Steve")
            .add_player("Natacha")
            .add_player("Tony")
            .add_player("Thor")
            .deal_card("Steve")
            .deal_card("Natacha")
            .deal_card("Tony")
            .deal_card("Thor")
            .deal_card("Steve")
            .deal_card("Natacha")
            .deal_card("Tony")
            .deal_card("Thor")
            .is_valid_player("Steve")
            .is_valid_player("Natacha")
            .is_valid_player("Tony")
            .is_valid_player("Thor")
            .is_this_player_have_his_dealing_cards("Steve")
            .is_this_player_have_his_dealing_cards("Natacha")
            .is_this_player_have_his_dealing_cards("Tony")
            .is_this_player_have_his_dealing_cards("Thor")
            .is_this_player_have_this_cards("Steve", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.JACK, CardColor.CLUBS)])
            .is_this_player_have_this_cards("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.TEN, CardColor.HEARTS)])
            .is_this_player_have_this_cards("Tony", [Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.DIAMONDS)])
            .is_this_player_have_this_cards("Thor", [Card(CardValue.JACK, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES)])
            .valid_all_cards_draw_are_unique())   
    
#TODO one test everything random 
def test_3():
    (TableDriver(MultiDrawCards() )
                .add_player("Steve")
                .add_player("Natacha")
                .add_player("Tony")
                .add_player("Thor")
                .deal_card("Steve")
                .deal_card("Natacha")
                .deal_card("Tony")
                .deal_card("Thor")
                .deal_card("Steve")
                .deal_card("Natacha")
                .deal_card("Tony")
                .deal_card("Thor")
                .burn_one_card()
                .deal_flop()
                .burn_one_card()
                .deal_turn()
                .burn_one_card()
                .deal_river()
                .affect_boards_cards_to_players()
                .is_valid_player("Steve")
                .is_valid_player("Natacha")
                .is_valid_player("Tony")
                .is_valid_player("Thor")
                .is_this_player_have_all_his_dealing_cards("Steve")
                .is_this_player_have_all_his_dealing_cards("Natacha")
                .is_this_player_have_all_his_dealing_cards("Tony")
                .is_this_player_have_all_his_dealing_cards("Thor")
                .is_three_cards_are_burned()
                .is_five_cards_in_the_board()
                .valid_all_cards_draw_are_unique())

#TODO one test everything determinist 
def test_4():
    false_cards = ["K♣","Q♥","Q♦","J♠", "J♣","10♥","10♦","9♠", "9♣", "8♥", "8♦", "7♠", "6♣", "6♥", "5♦", "5♠"]
    (TableDriver(FakeMultiDrawCards(false_cards) )
                .add_player("Steve")
                .add_player("Natacha")
                .add_player("Tony")
                .add_player("Thor")
                .deal_card("Steve")
                .deal_card("Natacha")
                .deal_card("Tony")
                .deal_card("Thor")
                .deal_card("Steve")
                .deal_card("Natacha")
                .deal_card("Tony")
                .deal_card("Thor")
                .burn_one_card()
                .deal_flop()
                .burn_one_card()
                .deal_turn()
                .burn_one_card()
                .deal_river()
                .affect_boards_cards_to_players()
                .is_valid_player("Steve")
                .is_valid_player("Natacha")
                .is_valid_player("Tony")
                .is_valid_player("Thor")
                .is_this_player_have_all_his_dealing_cards("Steve")
                .is_this_player_have_all_his_dealing_cards("Natacha")
                .is_this_player_have_all_his_dealing_cards("Tony")
                .is_this_player_have_all_his_dealing_cards("Thor")
                .is_three_cards_are_burned()
                .is_five_cards_in_the_board()                                                                                                                                                                                                     
                .is_this_player_have_this_cards("Steve", [Card(CardValue.KING, CardColor.CLUBS), Card(CardValue.JACK, CardColor.CLUBS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.SPADES), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.SPADES)])                                                                                                                                                                                                                                                                                                                                                                              
                .is_this_player_have_this_cards("Natacha", [Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.SPADES), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.SPADES)]) 
                .is_this_player_have_this_cards("Tony", [Card(CardValue.QUEEN, CardColor.DIAMONDS), Card(CardValue.TEN, CardColor.DIAMONDS), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.SPADES), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.SPADES)])
                .is_this_player_have_this_cards("Thor", [Card(CardValue.JACK, CardColor.SPADES), Card(CardValue.NINE, CardColor.SPADES), Card(CardValue.EIGHT, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.DIAMONDS), Card(CardValue.SEVEN, CardColor.SPADES), Card(CardValue.SIX, CardColor.HEARTS), Card(CardValue.FIVE, CardColor.SPADES)])
                .valid_all_cards_draw_are_unique())

class TableDriver(): 
    def __init__(self, multi_draw_cards):
        self.players = {}
        self.multi_draw_cards = multi_draw_cards
        self.all_cards = []
        self.burn_cards = []     
        self.flop_cards = []
        self.turn_card = None
        self.river_card = None
        self.table = Table(multi_draw_cards)

    def add_player(self, name_player):
        self.table.add_player(name_player)
        return self

    def deal_card(self,name_player): 
        one_card = self.table.deal_card(name_player)
        self.all_cards.append(one_card)
        return self

    def burn_one_card(self):
        card_burned = self.table.burn_one_card()
        self.burn_cards.append(card_burned)
        self.all_cards.append(card_burned)
        return self
        
    def deal_flop(self):
        self.flop_cards = self.table.deal_flop()
        for card in self.flop_cards: 
            self.all_cards.append(card)
        return self

    def deal_turn(self):
        self.turn_card = self.table.deal_turn()
        self.all_cards.append(self.turn_card)
        return self

    def deal_river(self):
        self.river_card = self.table.deal_river()
        self.all_cards.append(self.river_card)
        return self

    def affect_boards_cards_to_players(self):
        all_cards_to_affect = []
        for card in self.flop_cards: 
            all_cards_to_affect.append(card)
        all_cards_to_affect.append(self.turn_card)
        all_cards_to_affect.append(self.river_card)
        self.table.affect_boards_cards_to_players(all_cards_to_affect)
        return self

    def is_valid_player(self, name_player):
        is_player_here = name_player in self.table.players
        assert(is_player_here == True)
        return self

    def is_this_player_have_his_dealing_cards(self, name_player):
        cards = self.table.players[name_player]
        assert(len(cards) == 2)
        return self

    def is_this_player_have_all_his_dealing_cards(self, name_player):
            cards = self.table.players[name_player]
            assert(len(cards) == 7)
            return self

    def is_this_player_have_this_cards(self, name_player, cards_expected): 
        is_still_ok = True
        cards = self.table.players[name_player]
        for idx, card in enumerate(cards_expected): 
            card_expected = cards[idx]
            if card.color != card_expected.color or card.value != card_expected.value :
                is_still_ok = False
                break
        assert(is_still_ok == True)
        return self
    
    def is_three_cards_are_burned(self):
        assert(len(self.burn_cards) == 3)
        return self

    def is_five_cards_in_the_board(self):
        board_cards = []
        for card in self.flop_cards : 
            board_cards.append(card)
        board_cards.append(self.turn_card)
        board_cards.append(self.river_card)
        return self

    def valid_all_cards_draw_are_unique(self):
            cards_draw_unique_element = set(self.all_cards)
            assert (len(self.all_cards) == len(cards_draw_unique_element))
            return self