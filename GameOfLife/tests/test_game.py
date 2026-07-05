from GameOfLife.game import Game

simple_grid = [".*.", "**.", "..."]
medium_grid = ["*.*", ".*.", "..*"]
complexe_grid = ["...**...", "..*.*...", "...**...", ".*......"]

def test_throw_game_with_simple_grid_three_turns():
    grid_evoluting  = __get_all_turns(simple_grid, 3)
    assert(grid_evoluting[0] == [".*.", "**.", "..."])
    assert(grid_evoluting[1] == ["**.", "**.", "..."])
    assert(grid_evoluting[2] == ["**.", "**.", "..."])

def test_throw_game_with_medium_grid_three_turns(): #il y a un soucis dans cette ligne!!!!!
    grid_evoluting = __get_all_turns(medium_grid, 3)
    assert(grid_evoluting[0] == ["*.*", ".*.", "..*"])
    assert(grid_evoluting[1] == [".*.", ".**", "..."])
    assert(grid_evoluting[2] == [".**", ".**", "..."])

def test_throw_game_with_complexe_grid_three_turns(): 
    grid_evoluting = __get_all_turns(complexe_grid, 3)
    assert(grid_evoluting[0] == ["...**...", "..*.*...", "...**...", ".*......"])
    assert(grid_evoluting[1] == ["...**...", "..*..*..", "..***...","........"])
    assert(grid_evoluting[2] == ["...**...", "..*..*..", "..***...","...*...."])

def __get_all_turns(grid_data, max_turn):
    game = Game(grid_data, max_turn)
    evolutions = game.Throw()
    return evolutions