from PokerHandsV2.card import Card
from PokerHandsV2.counting_cards import CountingCards
from PokerHandsV2.detector.four_cards_detector import FourCardsDetector
from PokerHandsV2.detector.flush_detector import FlushDetector
from PokerHandsV2.detector.full_detector import FullDetector
from PokerHandsV2.detector.high_card_detector import HighCardDetector
from PokerHandsV2.detector.pair_detector import PairDetector
from PokerHandsV2.detector.quinte_flush_detector import QuinteFlushDetector
from PokerHandsV2.detector.straight_detector import StraightDetector
from PokerHandsV2.detector.three_cards_detector import ThreeCardsDetector
from PokerHandsV2.detector.two_pairs_detector import TwoPairsDetector
from PokerHandsV2.draw.multi_draw_cards import MultiDrawCards
from PokerHandsV2.game.hands_manager import HandsManager
from PokerHandsV2.game.turn_phase import TurnPhase
from PokerHandsV2.hand import Hand
from PokerHandsV2.tests.fake_multi_draw_cards import FakeMultiDrawCards

def test_launch_turn_phase_with_two_players_randomly():
    (TurnPhaseDriver(MultiDrawCards())
                    .add_player("Steve")
                    .add_player("Natacha")
                    .add_card_before_flop_phase("2♠", "Steve")
                    .add_card_before_flop_phase("A♥", "Natacha")
                    .add_card_before_flop_phase("6♠", "Steve")
                    .add_card_before_flop_phase("A♣", "Natacha")
                    .add_card_flop_phase("2♥")
                    .add_card_flop_phase("2♦")
                    .add_card_flop_phase("A♠")
                    .launch_phase_and_get_best_players()
                    .is_this_players_can_be_a_winner(["Steve", "Natacha"]))

def test_launch_turn_phase_with_two_players_and_steve_wins():
    false_cards = ["2♣"]
    (TurnPhaseDriver(FakeMultiDrawCards(false_cards))
        .add_player("Steve")
        .add_player("Natacha")
        .add_card_before_flop_phase("2♠", "Steve")
        .add_card_before_flop_phase("A♥", "Natacha")
        .add_card_before_flop_phase("6♠", "Steve")
        .add_card_before_flop_phase("A♣", "Natacha")
        .add_card_flop_phase("2♥")
        .add_card_flop_phase("2♦")
        .add_card_flop_phase("A♠")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Steve"])
    )

def test_launch_turn_phase_with_two_players_and_natacha_wins():
    false_cards = ["3♣"]
    (TurnPhaseDriver(FakeMultiDrawCards(false_cards))
        .add_player("Steve")
        .add_player("Natacha")
        .add_card_before_flop_phase("2♠", "Steve")
        .add_card_before_flop_phase("A♥", "Natacha")
        .add_card_before_flop_phase("6♠", "Steve")
        .add_card_before_flop_phase("A♣", "Natacha")
        .add_card_flop_phase("2♥")
        .add_card_flop_phase("2♦")
        .add_card_flop_phase("A♠")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Natacha"])
    )

def test_launch_turn_phase_with_two_players_win():
    false_cards = ["3♣"]
    (TurnPhaseDriver(FakeMultiDrawCards(false_cards))
        .add_player("Steve")
        .add_player("Natacha")
        .add_card_before_flop_phase("2♠", "Steve")
        .add_card_before_flop_phase("2♥", "Natacha")
        .add_card_before_flop_phase("A♦", "Steve")
        .add_card_before_flop_phase("A♣", "Natacha")
        .add_card_flop_phase("4♥")
        .add_card_flop_phase("J♦")
        .add_card_flop_phase("6♠")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Steve_Natacha"])
    )

def test_launch_turn_phase_with_ten_players_randomly():
    (TurnPhaseDriver(MultiDrawCards())
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .add_card_before_flop_phase("A♠", "Steve")
        .add_card_before_flop_phase("K♣", "Natacha")
        .add_card_before_flop_phase("A♠", "Steve")
        .add_card_before_flop_phase("K♣", "Natacha")
        .add_card_before_flop_phase("Q♥", "Tony")
        .add_card_before_flop_phase("J♦","Thor")
        .add_card_before_flop_phase("10♣", "Bruce")
        .add_card_before_flop_phase("9♦", "Clint")
        .add_card_before_flop_phase("8♥", "Carol")
        .add_card_before_flop_phase("7♠", "T'Challa")
        .add_card_before_flop_phase("6♣", "Steven")
        .add_card_before_flop_phase("5♦", "Wanda")
        .add_card_before_flop_phase("4♥", "Steve")
        .add_card_before_flop_phase("3♠", "Natacha")
        .add_card_before_flop_phase("2♣","Tony")
        .add_card_before_flop_phase("A♦", "Thor")
        .add_card_before_flop_phase("K♥", "Bruce")
        .add_card_before_flop_phase("Q♠", "Clint")
        .add_card_before_flop_phase("J♣", "Carol")
        .add_card_before_flop_phase("10♦", "T'Challa")
        .add_card_before_flop_phase("9♥", "Steven")
        .add_card_before_flop_phase("8♠", "Wanda")
        .add_card_flop_phase("4♥")
        .add_card_flop_phase("J♦")
        .add_card_flop_phase("6♠")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Steve", "Natacha", "Tony", "Thor", "Bruce", "Clint", "Carol", "T'Challa", "Steven", "Peter", "Wanda" ]))

def test_launch_turn_phase_with_ten_players_and_wanda_win():
    fake_cards = ["5♠"]
    (TurnPhaseDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .add_card_before_flop_phase("A♠", "Steve")
        .add_card_before_flop_phase("K♣", "Natacha")
        .add_card_before_flop_phase("A♠", "Steve")
        .add_card_before_flop_phase("K♣", "Natacha")
        .add_card_before_flop_phase("Q♥", "Tony")
        .add_card_before_flop_phase("J♦","Thor")
        .add_card_before_flop_phase("10♣", "Bruce")
        .add_card_before_flop_phase("9♦", "Clint")
        .add_card_before_flop_phase("8♥", "Carol")
        .add_card_before_flop_phase("7♠", "T'Challa")
        .add_card_before_flop_phase("6♣", "Steven")
        .add_card_before_flop_phase("5♦", "Wanda")
        .add_card_before_flop_phase("4♥", "Steve")
        .add_card_before_flop_phase("3♠", "Natacha")
        .add_card_before_flop_phase("2♣","Tony")
        .add_card_before_flop_phase("A♦", "Thor")
        .add_card_before_flop_phase("7♥", "Bruce")
        .add_card_before_flop_phase("Q♠", "Clint")
        .add_card_before_flop_phase("J♣", "Carol")
        .add_card_before_flop_phase("10♦", "T'Challa")
        .add_card_before_flop_phase("9♥", "Steven")
        .add_card_before_flop_phase("8♠", "Wanda")               
        .add_card_flop_phase("5♥")
        .add_card_flop_phase("8♦")
        .add_card_flop_phase("4♠")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Wanda"]))

def test_launch_turn_phase_with_ten_players_and_tony_and_clint_win():
    fake_cards = ["Q♦"]
    (TurnPhaseDriver(FakeMultiDrawCards(fake_cards))
        .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
        .add_card_before_flop_phase("A♠", "Steve")
        .add_card_before_flop_phase("K♣", "Natacha")
        .add_card_before_flop_phase("Q♥", "Tony")
        .add_card_before_flop_phase("J♦","Thor")
        .add_card_before_flop_phase("10♣", "Bruce")
        .add_card_before_flop_phase("9♦", "Clint")
        .add_card_before_flop_phase("8♥", "Carol")
        .add_card_before_flop_phase("7♠", "T'Challa")
        .add_card_before_flop_phase("6♣", "Steven")
        .add_card_before_flop_phase("5♦", "Wanda")
        .add_card_before_flop_phase("4♥", "Steve")
        .add_card_before_flop_phase("3♠", "Natacha")
        .add_card_before_flop_phase("2♣","Tony")
        .add_card_before_flop_phase("A♦", "Thor")
        .add_card_before_flop_phase("7♥", "Bruce")
        .add_card_before_flop_phase("Q♠", "Clint")
        .add_card_before_flop_phase("J♣", "Carol")
        .add_card_before_flop_phase("10♦", "T'Challa")
        .add_card_before_flop_phase("9♥", "Steven")
        .add_card_before_flop_phase("8♠", "Wanda")                   
        .add_card_flop_phase("10♥")
        .add_card_flop_phase("6♦")
        .add_card_flop_phase("4♠")
        .launch_phase_and_get_best_players()
        .is_this_players_can_be_a_winner(["Tony_Clint"]))

class TurnPhaseDriver():
    def __init__(self, multi_draw_cards):
        self.players = {}
        counting_cards = CountingCards()
        high_card_detector = HighCardDetector()
        pair_detector = PairDetector(counting_cards)
        two_pairs_detector = TwoPairsDetector(counting_cards)
        three_cards_detector = ThreeCardsDetector(counting_cards)
        straight_detector = StraightDetector(counting_cards)
        flush_detector = FlushDetector()
        full_detector = FullDetector(counting_cards)
        four_cards_detector = FourCardsDetector(counting_cards)
        quinte_flush_detector = QuinteFlushDetector()
        hand = Hand(high_card_detector, pair_detector, two_pairs_detector, three_cards_detector, straight_detector, flush_detector, full_detector, four_cards_detector, quinte_flush_detector)
        self.multi_draw_cards = multi_draw_cards
        self.hand_manager = HandsManager(hand, self.multi_draw_cards)
        self.winners = []

    def add_player(self, player_name):
        self.hand_manager.add_player(player_name)
        return self 

    def add_players(self, players_name): 
            for player_name in players_name:
                self.hand_manager.add_player(player_name)
            return self

    def add_card_before_flop_phase(self, card_crypted, player_name):
        card = Card.parse(card_crypted)
        self.hand_manager.add_cards_to_players(player_name, card)
        return self

    def add_card_flop_phase(self, card_crypted):
        card = Card.parse(card_crypted)
        for player_name in self.hand_manager.get_all_players() : 
            self.hand_manager.add_cards_to_players(player_name, card)
        return self

    def launch_phase_and_get_best_players(self):        
        turn_phase = TurnPhase(self.hand_manager, self.multi_draw_cards)
        self.winners = turn_phase.launch_phase_and_get_best_players()
        return self

    def is_this_players_can_be_a_winner(self, players_name):
        is_winner = False
        for player_name in players_name : 
            if "_" in player_name : 
                all_players = player_name.split("_")
                is_winner = all_players == self.winners
            else : 
                is_winner = player_name in self.winners
            if is_winner == True: 
                break
        assert (is_winner == True)
        return self 