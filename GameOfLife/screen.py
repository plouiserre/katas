class Screen : 
    def __init__(self, game):
        self.game = game

    def draw(self):
        evolutions = self.game.Throw()
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