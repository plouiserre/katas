from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.game.party import Party

multi_draw_cards = MultiDrawCards()
party = Party(multi_draw_cards)


players = []

print("Who are the players?")
while True : 
    raw = input("> ")
    if raw == "stop" :
        break
    else : 
        players.append(raw)

party.add_players(players)

results = party.launch_party()

for phase in results : 
    delimeter = " " 
    winner_str = delimeter.join(results[phase].winners)
    print("the winner for this phase "+phase.name+" is "+winner_str)