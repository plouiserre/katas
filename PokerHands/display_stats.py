from PokerHands.AllFigures.FlushFigure import FlushFigure
from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure
from PokerHands.AllFigures.FullFigure import FullFigure
from PokerHands.AllFigures.HighCardFigure import HighCardFigure
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.AllFigures.QuinteFlushFigure import QuinteFlushFigure
from PokerHands.AllFigures.QuinteFigure import QuinteFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure

def display_stats_presences_figures_in_river(stats_results):
    print("----------------% all figures presences in river phase----------------")
    stats = stats_results.percentage_presence_figure_river
    print("this is all figures presents in river")
    __display_all_stats_presences_figures(stats, "river phase")

def display_stats_presences_figures_in_each_phase(stats_results):
    print("----------------% all figures presences in every phase----------------")
    stats = stats_results.percentage_presence_figure_everywhere
    print("this is all figures presents in each phase")
    __display_all_stats_presences_figures(stats, "each phase")

def __display_all_stats_presences_figures(stats, end_phase):
    __get_percentage_figure_and_display(stats, HighCardFigure.__name__, end_phase)
    __get_percentage_figure_and_display(stats, PairFigure.__name__, end_phase)
    __get_percentage_figure_and_display(stats, TwoPairFigure.__name__, end_phase)
    __get_percentage_figure_and_display(stats, ThreeOfKindFigure.__name__, end_phase)
    __get_percentage_figure_and_display(stats, QuinteFigure.__name__, end_phase)
    __get_percentage_figure_and_display(stats, FlushFigure.__name__, end_phase)
    __get_percentage_figure_and_display(stats, FullFigure.__name__, end_phase)
    __get_percentage_figure_and_display(stats, FourOfKindFigure.__name__, end_phase)
    __get_percentage_figure_and_display(stats, QuinteFlushFigure.__name__, end_phase)
    
def __get_percentage_figure_and_display(stats, figure_name, end_phase):
    figure_percentage = __get_percentage_from_figure_presence(stats, figure_name)
    figure_percentage_round = round(figure_percentage, 2)
    print(figure_name+" is "+str(figure_percentage_round)+"% present in "+end_phase)    
    
def __get_percentage_from_figure_presence(stats, figure): 
    if figure in stats : 
        percentage = stats[figure]*100
        return percentage
    return 0

def display_winner_in_river_phase(stats_results):
    print("----------------winning of each player in river phase----------------")
    __display_winners_with_percentage(stats_results.percentage_winner_players_river, "river phase")

def display_winner_in_every_phase(stats_results):
    print("----------------winning of each player in every phase----------------")
    __display_winners_with_percentage(stats_results.percentage_winner_players_everywhere, "every phase")

def __display_winners_with_percentage(stats_winners, phase_str):
    for player in stats_winners : 
        percentage = str(round(stats_winners[player]*100, 2))
        print(player+" wins "+percentage+"% in "+phase_str)

def display_percentage_best_figure_in_river_phase(stats_results):
    print("----------------winning of each figure in river phase----------------")
    __display_percentage_figure_winning(stats_results.percentage_winning_figure_river, "river phase")

def display_percentage_best_figure_in_every_phase(stats_results):
    print("----------------winning of each figure in every phase----------------")
    __display_percentage_figure_winning(stats_results.percentage_winning_figure_everywhere, "every phase")    

def __display_percentage_figure_winning(stats_all_figures, phase_str): 
    for figure in stats_all_figures : 
        percentage = str(round(stats_all_figures[figure]*100, 2))
        print(figure+" wins "+percentage+"% in "+phase_str)