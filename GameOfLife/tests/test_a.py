from GameOfLife.game import Game

simple_grid = [".*.", "**.", "..."]
medium_grid = ["*.*", ".*.", "..*"]
complexe_grid = ["...**...", "..*.*...", "...**...", ".*......"]

def test_1():
    grid_evoluting  = __get_all_turns(simple_grid, 3)
    assert(grid_evoluting[0] == [".*.", "**.", "..."])
    assert(grid_evoluting[1] == ["**.", "**.", "..."])
    assert(grid_evoluting[2] == ["**.", "**.", "..."])

def test_2(): #il y a un soucis dans cette ligne!!!!!
    grid_evoluting = __get_all_turns(medium_grid, 3)
    assert(grid_evoluting[0] == ["*.*", ".*.", "..*"])
    assert(grid_evoluting[1] == [".*.", ".**", "..."])
    assert(grid_evoluting[2] == [".**", ".**", "..."])

def test_3(): 
    grid_evoluting = __get_all_turns(complexe_grid, 3)
    assert(grid_evoluting[0] == ["...**...", "..*.*...", "...**...", ".*......"])
    assert(grid_evoluting[1] == ["...**...", "..*..*..", "..***...","........"])
    assert(grid_evoluting[2] == ["...**...", "..*..*..", "..***...","...*...."])

def __get_all_turns(grid_data, max_turn):
    game = Game(grid_data, max_turn)
    evolutions = game.Throw()
    return evolutions