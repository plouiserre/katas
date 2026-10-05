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

number = 1
for result_game in results_multiple_game : 
    print("Game "+str(number))
    for phase in result_game : 
        delimeter = " " 
        winner_str = delimeter.join(result_game[phase].winners)
        print("the winner for this phase "+phase.name+" is "+winner_str)
    number += 1


statistiques_presence_figures =  StatistiquesPresenceFigures(results_multiple_game)
statistiques_winners_players = StatistiquesWinnerPlayers(results_multiple_game)
statistiques_win_figures = StatistiquesWinFigures(results_multiple_game)
stats = PokerStatistiques(statistiques_presence_figures, statistiques_winners_players, statistiques_win_figures)
stats_results = stats.calculate_all_statistiques()
print("loooool")