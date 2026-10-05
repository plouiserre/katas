from PokerHands.display.display_launch_game import display_winner_each_parties, insert_players, launch_multiple_parties
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

insert_players(multiple_game)

results_multiple_game = launch_multiple_parties(multiple_game)

display_winner_each_parties(results_multiple_game)

statistiques_presence_figures =  StatistiquesPresenceFigures(results_multiple_game)
statistiques_winners_players = StatistiquesWinnerPlayers(results_multiple_game)
statistiques_win_figures = StatistiquesWinFigures(results_multiple_game)
stats = PokerStatistiques(statistiques_presence_figures, statistiques_winners_players, statistiques_win_figures)
stats_results = stats.calculate_all_statistiques()
print("loooool")