from GameOfLife.game import Game
from GameOfLife.screen import Screen


grid_data = ["...*", "***.", "*.*.", "****"]

game = Game(grid_data, 5)
screen = Screen(game)

displays = screen.draw()

for display in displays : 
    print(display)
    print("\n")