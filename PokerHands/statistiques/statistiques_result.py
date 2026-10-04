class StatistiquesResult : 
    def __init__(self, percentage_presence_figure_river, percentage_presence_figure_everywhere, percentage_winner_players_river, percentage_winner_players_everywhere, percentage_winning_figure_river, percentage_winning_figure_everywhere):
        self.percentage_presence_figure_river = percentage_presence_figure_river
        self.percentage_presence_figure_everywhere = percentage_presence_figure_everywhere
        self.percentage_winner_players_river = percentage_winner_players_river
        self.percentage_winner_players_everywhere = percentage_winner_players_everywhere
        self.percentage_winning_figure_river = percentage_winning_figure_river    
        self.percentage_winning_figure_everywhere = percentage_winning_figure_everywhere

    @staticmethod
    def create_statistique_result(percentage_presence_figure_river, percentage_presence_figure_everywhere, percentage_winner_players_river, percentage_winner_players_everywhere, percentage_winning_figure_river, percentage_winning_figure_everywhere):
        return StatistiquesResult(percentage_presence_figure_river, percentage_presence_figure_everywhere, percentage_winner_players_river, percentage_winner_players_everywhere, percentage_winning_figure_river, percentage_winning_figure_everywhere)