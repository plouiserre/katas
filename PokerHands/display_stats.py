from PokerHands.AllFigures.FlushFigure import FlushFigure
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure
from PokerHands.AllFigures.FullFigure import FullFigure
from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.AllFigures.QuinteFigure import QuinteFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure

def display_stats_presences_figures_in_showdown(stats_results):
    print("----------------% all figures presences----------------")
    stats = stats_results.percentage_presence_figure_showdown
    print("this is all figures presents")
    __display_all_stats_presences_figures(stats)

def __display_all_stats_presences_figures(stats):
    __get_percentage_figure_and_display(stats, HighCardFigure.__name__)
    __get_percentage_figure_and_display(stats, PairFigure.__name__)
    __get_percentage_figure_and_display(stats, TwoPairFigure.__name__)
    __get_percentage_figure_and_display(stats, ThreeOfKindFigure.__name__)
    __get_percentage_figure_and_display(stats, QuinteFigure.__name__)
    __get_percentage_figure_and_display(stats, FlushFigure.__name__)
    __get_percentage_figure_and_display(stats, FullFigure.__name__)
    __get_percentage_figure_and_display(stats, FourOfKindFigure.__name__)
    __get_percentage_figure_and_display(stats, QuinteFlushFigure.__name__)
    
def __get_percentage_figure_and_display(stats, figure_name):
    figure_percentage = __get_percentage_from_figure_presence(stats, figure_name)
    figure_percentage_round = round(figure_percentage, 2)
    print(figure_name+" is "+str(figure_percentage_round)+"%")    
    
def __get_percentage_from_figure_presence(stats, figure): 
    if figure in stats : 
        percentage = stats[figure]*100
        return percentage
    return 0

def display_winner_in_showdown_phase(stats_results):
    print("----------------winning of each player----------------")
    __display_winners_with_percentage(stats_results.percentage_winner_players_showdown)

def __display_winners_with_percentage(stats_winners):
    for player in stats_winners : 
        percentage = str(round(stats_winners[player]*100, 2))
        print(player+" wins "+percentage+"%")

def display_percentage_best_figure_in_showdown_phase(stats_results):
    print("----------------winning of each figure----------------")
    __display_percentage_figure_winning(stats_results.percentage_winning_figure_showdown)

def __display_percentage_figure_winning(stats_all_figures): 
    for figure in stats_all_figures : 
        percentage = str(round(stats_all_figures[figure]*100, 2))
        print(figure+" wins "+percentage+"%")