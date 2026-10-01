from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.multiple_game import MultipleGame

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