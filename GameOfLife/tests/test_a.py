from GameOfLife.game import Game

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
    evolutions = game.Throw()
    texts = []
    for grid in evolutions : 
        text = ""
        counter = 0
        for counter, line in enumerate(grid) : 
            if counter != len(grid) - 1:
                text += line+"\n"
            else :
                text+= line
        texts.append(text)
    return texts