class ComparaisonResult : 
    def __init__(self, winners, best_figure):
        self.winners = winners
        self.best_figure = best_figure

    @staticmethod
    def Create(winners, best_figure): 
        return ComparaisonResult(winners, best_figure)