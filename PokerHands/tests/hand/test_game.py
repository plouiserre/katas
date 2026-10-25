from PokerHands.AllFigures.FullFigure import FullFigure
from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.AllFigures.QuinteFigure import QuinteFigure
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.card import Card, CardValue, CardColor
from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.hand.hand import Game, PhasePoker
from PokerHands.tests.assert_helper import is_this_two_figure_are_equal
from PokerHands.tests.fake_multi_draw_cards import FakeMultiDrawCards

def test_launch_random_game_with_two_players():
    (GameDriver(MultiDrawCards())
            .add_players(["Steve", "Natacha"])
            .launch_game()
            .all_cards_are_differents()
            .is_three_cards_burned()
            .is_this_players_have_seven_cards_dealed("Steve")
            .is_this_players_have_seven_cards_dealed("Natacha")
            .is_this_players_can_be_a_winner(["Steve", "Natacha"])
    )

def test_launch_determine_game_with_two_players(): 
    fake_cards = ["K♣", "Q♠", "Q♥", "J♦", "3♠","A♣", "10♠", "9♥", "3♥","8♦","K♥", "J♣"]
    (GameDriver(FakeMultiDrawCards(fake_cards))
                .add_players(["Steve", "Natacha"])
                .launch_game()
                .all_cards_are_differents()
                .is_three_cards_burned()
                .is_this_players_have_seven_cards_dealed("Steve")
                .is_this_players_have_seven_cards_dealed("Natacha")
                .is_this_players_can_be_a_winner_with_best_figure(["Steve"], QuinteFigure(CardValue.ACE))
        )

def test_launch_random_game_with_ten_players(): 
    (GameDriver(MultiDrawCards())
                .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                .launch_game()
                .all_cards_are_differents()
                .is_three_cards_burned()
                .is_this_players_have_seven_cards_dealed("Steve")
                .is_this_players_have_seven_cards_dealed("Natacha")
                .is_this_players_can_be_a_winner(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        )

def test_launch_determine_game_with_ten_players(): 
    fake_cards = ["A♣", "K♠", "Q♥", "J♠", "10♣", "9♦", "8♣", "7♦", "6♣", "5♠", "4♥", "3♦", "2♣", "A♠", "K♥", "Q♦", "J♣", "10♠", "9♥", "8♥", "9♠","10♦", "10♥", "7♠", "8♠","J♦", "3♠","8♦"]
    (GameDriver(FakeMultiDrawCards(fake_cards))
                .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                .launch_game()
                .all_cards_are_differents()
                .is_three_cards_burned()
                .is_this_players_have_seven_cards_dealed("Steve")
                .is_this_players_have_seven_cards_dealed("Natacha")
                .is_this_players_can_be_a_winner_with_best_figure(["Clint"], QuinteFlushFigure(CardValue.QUEEN, CardColor.DIAMONDS))
        )

class GameDriver: 
    def __init__(self, multi_draw_cards):
        self.game = Game(multi_draw_cards)                
        self.players = []
        self.burn_cards = []

    def add_players(self, players_name):
        self.game.add_players(players_name)
        return self

    def launch_game(self):
        self.result = self.game.launch_game()
        return self

    def all_cards_are_differents(self): 
            all_cards = []
            for player in self.game.pre_flop_data.players : 
                all_cards_dealed = self.game.pre_flop_data.players[player][0:2]
                for card in all_cards_dealed: 
                    all_cards.append(card)
            all_cards.append(self.game.flop_phase_data.burn_card)
            for card in self.game.flop_phase_data.flop_cards: 
                all_cards.append(card)
            all_cards.append(self.game.turn_phase_data.burn_card)
            all_cards.append(self.game.turn_phase_data.turn_card)
            all_cards.append(self.game.river_phase_data.burn_card)
            all_cards.append(self.game.river_phase_data.river_card)
            all_cards_drawn_unique = set(all_cards)
            assert(len(all_cards) == len(all_cards_drawn_unique))
            return self

    def is_this_players_can_be_a_winner_with_best_figure(self, players_name, figure):
        is_winner = self.__is_winner(players_name)
        is_best_figure =  is_this_two_figure_are_equal(figure, self.result.best_figure)
        assert (is_winner == True and is_best_figure == True)
        return self 

    def is_three_cards_burned(self): 
        self.burn_cards.append(self.game.flop_phase_data.burn_card)        
        self.burn_cards.append(self.game.turn_phase_data.burn_card)
        self.burn_cards.append(self.game.river_phase_data.burn_card)
        for burn_card in self.burn_cards : 
            assert(burn_card != Card(CardValue.UNDEFINED, CardColor.UNDEFINED))
        return self    

    def is_this_players_have_seven_cards_dealed(self, player_name): 
        assert (len(self.game.river_phase_data.players[player_name]) == 7)
        return self

    def is_this_players_can_be_a_winner(self, players_name):
        is_winner = self.__is_winner(players_name)
        assert (is_winner == True)
        return self 

    def __is_winner(self, players_name):
        is_winner = False
        winners = self.result.winners
        for player_name in players_name : 
            if "_" in player_name : 
                all_players = player_name.split("_")
                is_winner = all_players == winners
            else : 
                is_winner = player_name in winners
            if is_winner == True: 
                break
        return is_winner    