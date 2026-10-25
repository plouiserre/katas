from PokerHands.statistiques.poker_statistiques import PokerStatistiques
from PokerHands.statistiques.statistiques_fight_figures import StatistiquesFightFigures
from PokerHands.statistiques.statistiques_presence_figures import StatistiquesPresenceFigures
from PokerHands.statistiques.statistiques_win_figures import StatistiquesWinFigures
from PokerHands.statistiques.statistiques_winners_players import StatistiquesWinnerPlayers
from PokerHands.tests.dsl.dsl_hand_result import convert_hand_result_crypted
from PokerHands.tests.dsl.dsl_figure import get_name_figure_from_initial
from PokerHands.tests.dsl.dsl_player import get_player

def test_calculate_poker_satistiques():
    (StatistiquesDriver()
     .add_players(["Jean-Jacques Goldman", "Mylène Farmer", "Omar Sy", "Sophie Marceau"])
     .add_hand_result("PAAK_J:PAKQ-M:HIK-O:PAAK-S:HIK_W:O")
     .add_hand_result("TKQK_J:PAKA-M:TKQK-O:PAAK-S:HIK_W:M")
     .add_hand_result("PAKA_J:PAKA-M:PAQK-O:HIA-S:HIK_W:J")     
     .add_hand_result("QF7S_J:PAKA-M:TKQK-O:PAAK-S:QF7S_W:S")     
     .add_hand_result("FUKA_J:FUAK-M:PAKA-O:FUKA-S:PAKA_W:O")
     .calculate_percentages()
     .validate_percentage("PRS|PA:0.5_HI:0.25_TK:0.1_QF:0.05_FU:0.1")
     .validate_percentage("WNS|J:0.2_M:0.2_O:0.4_S:0.2")
     .validate_percentage("WFS|PA:0.4_TK:0.2_QF:0.2_FU:0.2")
     .validate_percentage("VFF|HI:0.0_PA:0.4_TK:0.5_FU:1.0_QF:1.0"))


def test_calculate_poker_satistiques_after_10_games():
    (StatistiquesDriver()
     .add_players(["Jean-Jacques Goldman", "Mylène Farmer", "Omar Sy", "Sophie Marceau"])
     .add_hand_result("PAAK_J:PAKQ-M:HIK-O:PAAK-S:HIK_W:O")
     .add_hand_result("TKQK_J:PAKA-M:TKQK-O:PAAK-S:HIK_W:M")
     .add_hand_result("PAKA_J:PAKA-M:PAQK-O:HIA-S:HIK_W:J")     
     .add_hand_result("QF7S_J:PAKA-M:TKQK-O:PAAK-S:QF7S_W:S")     
     .add_hand_result("FUKA_J:FUAK-M:PAKA-O:FUKA-S:PAKA_W:O")
     .add_hand_result("2PQA6_J:PAQ6-M:2PQA6-O:HIQ-S:HI6_W:M")
     .add_hand_result("FOAQ_J:FOAQ-M:TKQA-O:PA9A-S:PAA3_W:J")     
     .add_hand_result("PAQA_J:PA2J-M:HIA-O:HIQ-S:PAQA_W:S")
     .add_hand_result("TK69_J:PA6A-M:PA9K-O:TK69-S:HIK_W:O")
     .add_hand_result("2PQA6_J:PAQ6-M:2PJA3-O:HIQ-S:PAAQ_W:M")          
     .calculate_percentages()
     .validate_percentage("PRS|PA:0.475_HI:0.275_TK:0.1_QF:0.025_FU:0.05_FO:0.025_2P:0.05")
     .validate_percentage("WNS|J:0.2_M:0.3_O:0.3_S:0.2")
     .validate_percentage("WFS|PA:0.3_TK:0.2_2P:0.2_QF:0.1_FU:0.1_FO:0.1")
     .validate_percentage("VFF|HI:0.0_PA:0.3_2P:1.0_TK:0.5_FU:1.0_FO:1.0_QF:1.0"))
     
class StatistiquesDriver : 
    def __init__(self):
        self.players = []
        self.games_results = []
        self.statistiques_result = None

    def add_players(self, players_name): 
        for player_name in players_name : 
            self.players.append(player_name)
        return self 
    
    def add_hand_result(self, hand_result_crypted):
        hand_result = convert_hand_result_crypted(hand_result_crypted, self.players)
        self.games_results.append(hand_result)
        return self

    def calculate_percentages(self):
        statistiques = PokerStatistiques(StatistiquesPresenceFigures(self.games_results), StatistiquesWinnerPlayers(self.games_results), StatistiquesWinFigures(self.games_results), StatistiquesFightFigures(self.games_results))
        self.statistiques_result = statistiques.calculate_all_statistiques()
        return self
    
    def validate_percentage(self, datas_crypted):
        all_datas = datas_crypted.split("|")
        if all_datas[0] == "PRS":
            self.__validate_all_percentages_calculated(all_datas[1], self.statistiques_result.percentage_presence_figure_showdown, "figure name")
        elif all_datas[0] == "WNS":
            self.__validate_all_percentages_calculated(all_datas[1], self.statistiques_result.percentage_winner_players_showdown, "player")
        elif all_datas[0] == "WFS":
            self.__validate_all_percentages_calculated(all_datas[1], self.statistiques_result.percentage_winning_figure_showdown, "figure name")
        elif all_datas[0] == "VFF":
            self.__validate_all_percentages_calculated(all_datas[1], self.statistiques_result.percentage_fight_figure_showdown, "figure name")
        return self

    def __validate_all_percentages_calculated(self, percentages_to_validate_crypted, statistiques_calculated, type_key):
        all_percentages_crypted = percentages_to_validate_crypted.split("_")        
        for percentage_crypted in all_percentages_crypted : 
            data_percentage_crypted = percentage_crypted.split(":")
            key_statistics_calculated = self.__get_key_statistics_calculated(type_key, data_percentage_crypted[0])
            data_percentage_calculated = str(statistiques_calculated[key_statistics_calculated])
            data_percentage_expected = data_percentage_crypted[1]
            assert(data_percentage_calculated == data_percentage_expected)

    def __get_key_statistics_calculated(self, type_key, key_percentage_crypted): 
        if type_key == "figure name":
            return get_name_figure_from_initial(key_percentage_crypted)
        else :
            return get_player(self.players, key_percentage_crypted)