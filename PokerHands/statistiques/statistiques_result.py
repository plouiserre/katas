class StatistiquesResult : 
    def __init__(self, percentage_presence_figure_showdown, percentage_winner_players_showdown, percentage_winning_figure_showdown):
        self.percentage_presence_figure_showdown = percentage_presence_figure_showdown
        self.percentage_winner_players_showdown = percentage_winner_players_showdown
        self.percentage_winning_figure_showdown = percentage_winning_figure_showdown    

    @staticmethod
    def create_statistique_result(percentage_presence_figure_showdown, percentage_winner_players_showdown, percentage_winning_figure_showdown):
        return StatistiquesResult(percentage_presence_figure_showdown, percentage_winner_players_showdown, percentage_winning_figure_showdown)