class StatistiquesFightFigures : 
    def __init__(self, games_results):
        self.games_results = games_results
        self.presences_figures = {}
        self.winning_figures = {}
        self.final_percentages = {}

    def calculate_percentage_winning_fight_for_all_figures_in_showdown(self):
        self.__count_all_presences_for_all_figures()
        self.__count_how_many_times_win_each_figure()
        self.__calculate_percentages_winning_figures()
        return self.final_percentages

    def __count_all_presences_for_all_figures(self):
        all_figures_count = []
        for round in self.games_results : 
            for player_name in round.poker_hands_by_player:
                poker_hand = round.poker_hands_by_player[player_name]
                poker_hand_type = type(poker_hand).__name__
                if (poker_hand_type in all_figures_count) == False:
                    all_figures_count.append(poker_hand_type)
                    if (poker_hand_type in self.presences_figures) == False :
                        self.presences_figures[poker_hand_type] = 0
                    self.presences_figures[poker_hand_type] += 1
            all_figures_count = []

    def __count_how_many_times_win_each_figure(self): 
        for round in self.games_results : 
            figure_name = type(round.best_figure).__name__
            if (figure_name in self.winning_figures) == False : 
                self.winning_figures[figure_name] = 0
            self.winning_figures[figure_name] += 1 

    def __calculate_percentages_winning_figures(self): 
        for figure_name in self.presences_figures : 
            number_victory = 0
            if (figure_name in self.winning_figures):
                number_victory = self.winning_figures[figure_name]
            self.final_percentages[figure_name] = number_victory / self.presences_figures[figure_name]