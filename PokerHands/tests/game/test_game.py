from PokerHands.AllFigures.FullFigure import FullFigure
from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.AllFigures.QuinteFigure import QuinteFigure
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.card import CardValue, CardColor
from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.game.game import Game, PhasePoker
from PokerHands.tests.assert_helper import is_this_two_figure_are_equal
from PokerHands.tests.fake_multi_draw_cards import FakeMultiDrawCards

def test_launch_random_game_with_two_players():
    (GameDriver(MultiDrawCards())
            .add_players(["Steve", "Natacha"])
            .launch_game()
            .is_this_players_can_be_a_winner(["Steve", "Natacha"], PhasePoker.DRAW)
            .is_this_players_can_be_a_winner(["Steve", "Natacha"], PhasePoker.FLOP)
            .is_this_players_can_be_a_winner(["Steve", "Natacha"], PhasePoker.TURN)
            .is_this_players_can_be_a_winner(["Steve", "Natacha"], PhasePoker.RIVER)
    )

def test_launch_determine_game_with_two_players(): 
    fake_cards = ["K♣", "Q♠", "Q♥", "J♦", "A♣", "10♠", "9♥", "8♦", "J♣"]
    (GameDriver(FakeMultiDrawCards(fake_cards))
                .add_players(["Steve", "Natacha"])
                .launch_game()
                .is_this_players_can_be_a_winner_with_best_figure(["Steve"], PhasePoker.DRAW, HighCardFigure(CardValue.KING))
                .is_this_players_can_be_a_winner_with_best_figure(["Steve_Natacha"], PhasePoker.FLOP, HighCardFigure(CardValue.ACE))
                .is_this_players_can_be_a_winner_with_best_figure(["Natacha"], PhasePoker.TURN, QuinteFigure(CardValue.QUEEN))
                .is_this_players_can_be_a_winner_with_best_figure(["Steve"], PhasePoker.RIVER, QuinteFigure(CardValue.ACE))
        )

def test_launch_random_game_with_ten_players(): 
    (GameDriver(MultiDrawCards())
                .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                .launch_game()
                .is_this_players_can_be_a_winner(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"], PhasePoker.DRAW)
                .is_this_players_can_be_a_winner(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"], PhasePoker.FLOP)
                .is_this_players_can_be_a_winner(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"], PhasePoker.TURN)
                .is_this_players_can_be_a_winner(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"], PhasePoker.RIVER)
        )

def test_launch_determine_game_with_ten_players(): 
    fake_cards = ["A♣", "K♠", "Q♥", "J♦", "10♣", "9♦", "8♥", "7♦", "6♣", "5♠", "4♥", "3♦", "2♣", "A♠", "K♥", "Q♦", "J♣", "10♠", "9♥", "8♥", "10♦", "10♥", "7♠", "J♦", "8♦"]
    (GameDriver(FakeMultiDrawCards(fake_cards))
                .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                .launch_game()
                .is_this_players_can_be_a_winner_with_best_figure(["Thor"], PhasePoker.DRAW, HighCardFigure(CardValue.ACE))
                .is_this_players_can_be_a_winner_with_best_figure(["T'Challa"], PhasePoker.FLOP, FullFigure(CardValue.SEVEN, CardValue.TEN))
                .is_this_players_can_be_a_winner_with_best_figure(["T'Challa"], PhasePoker.TURN, FullFigure(CardValue.SEVEN, CardValue.TEN))
                .is_this_players_can_be_a_winner_with_best_figure(["Clint"], PhasePoker.RIVER, QuinteFlushFigure(CardValue.QUEEN, CardColor.DIAMONDS))
        )

class GameDriver: 
    def __init__(self, multi_draw_cards):
        self.game = Game(multi_draw_cards)
                
        self.players = []
        self.winners = {}

    def add_players(self, players_name):
        self.game.add_players(players_name)
        return self

    def launch_game(self):
        self.result = self.game.launch_game()
        return self

    def is_this_players_can_be_a_winner_with_best_figure(self, players_name, phase, figure):
        phase = self.result[phase]
        is_winner = self.__is_winner(players_name, phase.winners)
        is_best_figure =  is_this_two_figure_are_equal(figure, phase.best_figure)
        assert (is_winner == True and is_best_figure == True)
        return self 

    def is_this_players_can_be_a_winner(self, players_name, phase):
        phase = self.result[phase]
        is_winner = self.__is_winner(players_name, phase.winners)
        assert (is_winner == True)
        return self 

    def __is_winner(self, players_name, winners):
        is_winner = False
        for player_name in players_name : 
            if "_" in player_name : 
                all_players = player_name.split("_")
                is_winner = all_players == winners
            else : 
                is_winner = player_name in winners
            if is_winner == True: 
                break
        return is_winner    