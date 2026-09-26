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

winners = party.launch_party()

for phase in winners : 
    delimeter = " " 
    winner_str = delimeter.join(winners[phase])
    print("the winner for this phase "+phase.name+" is "+winner_str)