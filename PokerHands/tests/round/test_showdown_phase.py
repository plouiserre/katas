from PokerHands.AllFigures.FourOfKindFigure import FourOfKindFigure
from PokerHands.AllFigures.FullFigure import FullFigure
from PokerHands.AllFigures.PairFigure import PairFigure
from PokerHands.AllFigures.ThreeOfKindFigure import ThreeOfKindFigure
from PokerHands.AllFigures.TwoPairFigure import TwoPairFigure
from PokerHands.card import Card, CardColor, CardValue
from PokerHands.round.showdown_phase import ShowdownPhase
from PokerHands.table.table import Table
from PokerHands.manipulating_cards import ManipulatingCards
from PokerHands.detector.four_cards_detector import FourCardsDetector
from PokerHands.detector.flush_detector import FlushDetector
from PokerHands.detector.full_detector import FullDetector
from PokerHands.detector.high_card_detector import HighCardDetector
from PokerHands.detector.pair_detector import PairDetector
from PokerHands.detector.quinte_flush_detector import QuinteFlushDetector
from PokerHands.detector.quinte_detector import QuinteDetector
from PokerHands.detector.three_cards_detector import ThreeCardsDetector
from PokerHands.detector.two_pairs_detector import TwoPairsDetector
from PokerHands.combination import Combination
from PokerHands.tests.assert_helper import is_this_two_figure_are_equal
from PokerHands.tests.fake_multi_draw_cards import FakeMultiDrawCards

    
def test_launch_showdown_phase_with_two_players_and_find_steve_winning():
    false_cards = ["2♠", "A♥", "6♠", "A♣", "Q♦", "2♥", "2♦", "A♠", "K♦","K♥", "3♠", "2♣"]
    (ShowdownPhaseDriver(FakeMultiDrawCards(false_cards))
        .add_player("Steve")
        .add_player("Natacha")
        .deal_card("Steve")
        .deal_card("Natacha")
        .deal_card("Steve")
        .deal_card("Natacha")
        .burn_one_card()
        .deal_flop()
        .burn_one_card()
        .deal_turn()
        .burn_one_card()
        .deal_river()
        .affect_boards_cards_to_players()
        .launch_showdown_phase_and_identify_winner()
        .is_this_players_can_be_a_winner(["Steve"])
        .is_this_best_figure(FourOfKindFigure(CardValue.TWO, CardValue.ACE))
        .is_this_poker_hand("Steve", FourOfKindFigure(CardValue.TWO, CardValue.ACE))
        .is_this_poker_hand("Natacha", FullFigure(CardValue.TWO, CardValue.ACE)))

def test_launch_showdown_phase_with_two_players_and_find_steve_and_natacha_winning():
    false_cards = ["2♠", "2♥", "A♦", "A♣", "A♥", "4♥", "J♦", "6♠", "Q♥", "5♥", "3♠","J♠"]
    (ShowdownPhaseDriver(FakeMultiDrawCards(false_cards))
        .add_player("Steve")
        .add_player("Natacha")
        .deal_card("Steve")
        .deal_card("Natacha")
        .deal_card("Steve")
        .deal_card("Natacha")
        .burn_one_card()
        .deal_flop()
        .burn_one_card()
        .deal_turn()
        .burn_one_card()
        .deal_river()
        .affect_boards_cards_to_players()
        .launch_showdown_phase_and_identify_winner()
        .is_this_players_can_be_a_winner(["Steve_Natacha"])
        .is_this_best_figure(PairFigure(CardValue.JACK, CardValue.ACE))
        .is_this_poker_hand("Steve", PairFigure(CardValue.JACK, CardValue.ACE))
        .is_this_poker_hand("Natacha", PairFigure(CardValue.JACK, CardValue.ACE))        
    )     
    
def test_launch_showdown_phase_with_two_players_and_find_wanda_winning():
    fake_cards = ["A♠", "K♣", "Q♥", "J♦","10♣", "9♦", "6♥", "7♠", "6♣", "5♦", "4♥", "3♠", "2♣", "A♦", "7♥", "Q♠", "J♣", "10♦", "9♥", "8♠", "2♦", "5♥", "8♥" , "4♠", "4♣", "8♠", "9♥", "8♠"]
    (ShowdownPhaseDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .deals_cards(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .deals_cards(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .burn_one_card()
        .deal_flop()
        .burn_one_card()
        .deal_turn()
        .burn_one_card()
        .deal_river()
        .affect_boards_cards_to_players()
        .launch_showdown_phase_and_identify_winner()
        .is_this_players_can_be_a_winner(["Wanda"])
        .is_this_best_figure(FourOfKindFigure(CardValue.EIGHT, CardValue.FIVE))        
        .is_this_poker_hand("Steve", FullFigure(CardValue.FOUR, CardValue.EIGHT))
        .is_this_poker_hand("Natacha", ThreeOfKindFigure(CardValue.EIGHT, CardValue.KING))
        .is_this_poker_hand("Tony", ThreeOfKindFigure(CardValue.EIGHT, CardValue.QUEEN))
        .is_this_poker_hand("Thor", ThreeOfKindFigure(CardValue.EIGHT, CardValue.ACE))
        .is_this_poker_hand("Bruce", ThreeOfKindFigure(CardValue.EIGHT, CardValue.TEN))
        .is_this_poker_hand("Clint", ThreeOfKindFigure(CardValue.EIGHT, CardValue.QUEEN))
        .is_this_poker_hand("Carol", ThreeOfKindFigure(CardValue.EIGHT, CardValue.JACK))
        .is_this_poker_hand("T'Challa", ThreeOfKindFigure(CardValue.EIGHT, CardValue.TEN))
        .is_this_poker_hand("Steven", ThreeOfKindFigure(CardValue.EIGHT, CardValue.NINE))
        .is_this_poker_hand("Wanda", FourOfKindFigure(CardValue.EIGHT, CardValue.FIVE)))

def test_launch_river_phase_with_ten_players_and_tony_and_clint_win():
    fake_cards = ["A♠", "K♣", "Q♥", "J♦", "10♣", "9♦", "8♥", "7♠", "6♣", "5♦", "4♥", "3♠", "2♣", "A♦", "7♥", "Q♠", "J♣", "10♦", "9♥", "8♠", "5♥", "10♥" ,"6♦", "4♠", "3♦", "Q♦", "3♠","Q♣"]
    (ShowdownPhaseDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .deals_cards(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .deals_cards(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .burn_one_card()
        .deal_flop()
        .burn_one_card()
        .deal_turn()
        .burn_one_card()
        .deal_river()
        .affect_boards_cards_to_players()
        .launch_showdown_phase_and_identify_winner()
        .is_this_players_can_be_a_winner(["Tony_Clint"])
        .is_this_best_figure(ThreeOfKindFigure(CardValue.QUEEN, CardValue.TEN))
        .is_this_poker_hand("Steve", TwoPairFigure(CardValue.QUEEN, CardValue.FOUR, CardValue.ACE))
        .is_this_poker_hand("Natacha", PairFigure(CardValue.QUEEN,CardValue.KING))
        .is_this_poker_hand("Tony", ThreeOfKindFigure(CardValue.QUEEN, CardValue.TEN))
        .is_this_poker_hand("Thor", PairFigure(CardValue.QUEEN,CardValue.ACE))
        .is_this_poker_hand("Bruce", TwoPairFigure(CardValue.QUEEN, CardValue.TEN, CardValue.SEVEN))
        .is_this_poker_hand("Clint", ThreeOfKindFigure(CardValue.QUEEN, CardValue.TEN))
        .is_this_poker_hand("Carol", PairFigure(CardValue.QUEEN, CardValue.JACK))
        .is_this_poker_hand("T'Challa", TwoPairFigure(CardValue.QUEEN, CardValue.TEN, CardValue.SEVEN))
        .is_this_poker_hand("Steven", TwoPairFigure( CardValue.QUEEN, CardValue.SIX, CardValue.TEN))
        .is_this_poker_hand("Wanda", PairFigure(CardValue.QUEEN, CardValue.TEN)))


class ShowdownPhaseDriver:
    def __init__(self, multi_card_draws):
        manipulating_cards = ManipulatingCards()
        high_card_detector = HighCardDetector()
        pair_detector = PairDetector(manipulating_cards)
        two_pairs_detector = TwoPairsDetector(manipulating_cards)
        three_cards_detector = ThreeCardsDetector(manipulating_cards)
        quinte_detector = QuinteDetector(manipulating_cards)
        flush_detector = FlushDetector()
        full_detector = FullDetector(manipulating_cards)
        four_cards_detector = FourCardsDetector(manipulating_cards)
        quinte_flush_detector = QuinteFlushDetector(manipulating_cards, quinte_detector)
        self.combination = Combination(high_card_detector, pair_detector, two_pairs_detector, three_cards_detector, quinte_detector, flush_detector, full_detector, four_cards_detector, quinte_flush_detector)
        self.players = {}
        self.table = Table(multi_card_draws)
        self.all_cards = []
        self.burn_cards = []     
        self.flop_cards = []
        self.turn_card = None
        self.river_card = None

    def add_player(self, player_name):
        self.table.add_player(player_name)
        return self

    def add_players(self, players_name):
        for player_name in players_name : 
              self.add_player(player_name)
        return self

    def deals_cards(self, players_name):
        for player_name in players_name: 
              self.deal_card(player_name)
        return self

    def deal_card(self,name_player): 
            one_card = self.table.deal_card(name_player)
            self.all_cards.append(one_card)
            return self

    def burn_one_card(self):
        card_burned = self.table.burn_one_card()
        self.burn_cards.append(card_burned)
        self.all_cards.append(card_burned)
        return self
            
    def deal_flop(self):
        self.flop_cards = self.table.deal_flop()
        for card in self.flop_cards: 
            self.all_cards.append(card)
        return self

    def deal_turn(self):
            self.turn_card = self.table.deal_turn()
            self.all_cards.append(self.turn_card)
            return self
    
    def deal_river(self):
        self.river_card = self.table.deal_river()
        self.all_cards.append(self.river_card)
        return self

    def affect_boards_cards_to_players(self):
            all_cards_to_affect = []
            for card in self.flop_cards: 
                all_cards_to_affect.append(card)
            all_cards_to_affect.append(self.turn_card)
            all_cards_to_affect.append(self.river_card)
            self.table.affect_boards_cards_to_players(all_cards_to_affect)
            return self

    def launch_showdown_phase_and_identify_winner(self):
        showdown_phase = ShowdownPhase(self.combination, self.table)
        self.hand_results = showdown_phase.analyze_pokers_hand_and_calculate_hand_results()
        return self

    def is_this_players_can_be_a_winner(self, players_name):
            is_winner = False
            for player_name in players_name : 
                if "_" in player_name : 
                    all_players = player_name.split("_")
                    is_winner = all_players == self.hand_results.winners
                else : 
                    is_winner = player_name in self.hand_results.winners
                if is_winner == True: 
                    break
            assert (is_winner == True)
            return self 
    
    def is_this_best_figure(self, figure): 
        is_equal =  is_this_two_figure_are_equal(figure, self.hand_results.best_figure)
        assert(is_equal == True)
        return self

    def is_this_poker_hand(self, player_name, figure_expected): 
        figure_calculated = self.hand_results.combination_by_player[player_name]
        is_right = is_this_two_figure_are_equal(figure_expected, figure_calculated) 
        assert(is_right == True)
        return self

    def is_one_card_burned(self): 
        assert(self.river_phase.card_burn != Card(CardValue.UNDEFINED, CardColor.UNDEFINED))
        return self

    def all_cards_are_differents(self): 
        all_cards = []
        all_cards.append(self.river_phase.card_turned)
        all_cards.append(self.river_phase.card_burn)
        all_cards_drawn_unique = set(all_cards)
        assert(len(all_cards) == len(all_cards_drawn_unique))
        return self
    