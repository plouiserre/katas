from PokerHands.display_stats import display_stats_presences_figures_in_river, display_stats_presences_figures_in_each_phase, display_winner_in_river_phase, display_winner_in_every_phase, display_percentage_best_figure_in_river_phase, display_percentage_best_figure_in_every_phase
from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.multiple_game import MultipleGame
from PokerHands.statistiques.poker_statistiques import PokerStatistiques
from PokerHands.statistiques.statistiques_presence_figures import StatistiquesPresenceFigures
from PokerHands.statistiques.statistiques_win_figures import StatistiquesWinFigures
from PokerHands.statistiques.statistiques_winners_players import StatistiquesWinnerPlayers

multi_draw_cards = MultiDrawCards()
multiple_game = MultipleGame()

players = []
number = 0

print("Who are the players?")
while True : 
    raw = input("> ")
    if raw == "stop" :
        break
    else :         
        multiple_game.add_player(raw)

print("How many games will be launch?")
raw = input("> ")
number = int(raw)

multiple_game.define_how_many_game_will_be_launching(number)

results_multiple_game = multiple_game.launch_multiple_game()
    

statistiques_presence_figures =  StatistiquesPresenceFigures(results_multiple_game)
statistiques_winners_players = StatistiquesWinnerPlayers(results_multiple_game)
statistiques_win_figures = StatistiquesWinFigures(results_multiple_game)
stats = PokerStatistiques(statistiques_presence_figures, statistiques_winners_players, statistiques_win_figures)
stats_results = stats.calculate_all_statistiques()
display_stats_presences_figures_in_river(stats_results)
display_stats_presences_figures_in_each_phase(stats_results)
display_winner_in_river_phase(stats_results)
display_winner_in_every_phase(stats_results)
display_percentage_best_figure_in_river_phase(stats_results)
display_percentage_best_figure_in_every_phase(stats_results)