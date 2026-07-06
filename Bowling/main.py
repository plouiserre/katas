from Bowling.game import Game
from Bowling.score_parser import ScoreParser

score_parser = ScoreParser()
score_writing = "5 2|6 3|4 1|- 6|5 3|4 3|4 4|2 6|1 5|8 / 6"
game = Game(score_writing, score_parser)
score_final = game.Calculate()

print("Score final de la partie "+str(score_final))