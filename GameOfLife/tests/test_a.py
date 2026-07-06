from GameOfLife.game import Game
from GameOfLife.screen import Screen

def test_1():
    simple_grid = [".*.", "**.", "..."]
    assert(draw_grid(simple_grid, 3)==[".*.\n**.\n...", "**.\n**.\n...","**.\n**.\n..."])

def test_2():
    medium_grid = ["*.*", ".*.", "..*"]
    assert(draw_grid(medium_grid, 3)==["*.*\n.*.\n..*",".*.\n.**\n...",".**\n.**\n..."]) 
    
def test_3():
    complexe_grid = ["...**...", "..*.*...", "...**...", ".*......"]
    assert(draw_grid(complexe_grid, 3)==["...**...\n..*.*...\n...**...\n.*......", "...**...\n..*..*..\n..***...\n........", "...**...\n..*..*..\n..***...\n...*...."])
    
def draw_grid(grid_departure, max_turn):
    game = Game(grid_departure, max_turn)
    screen = Screen(game)
    return screen.draw()