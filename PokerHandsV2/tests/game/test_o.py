from PokerHandsV2.card import Card, CardColor, CardValue
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

def test_1():
    best_players = (TurnPhaseDriver(MultiDrawCards())
                    .add_player("Steve")
                    .add_player("Natacha")
                    .add_card_before_flop_phase(Card(CardValue.TWO, CardColor.SPADES), "Steve")
                    .add_card_before_flop_phase(Card(CardValue.ACE, CardColor.HEARTS), "Natacha")
                    .add_card_before_flop_phase(Card(CardValue.SIX, CardColor.SPADES), "Steve")
                    .add_card_before_flop_phase(Card(CardValue.ACE, CardColor.CLUBS), "Natacha")
                    .add_card_flop_phase(Card(CardValue.TWO, CardColor.HEARTS))
                    .add_card_flop_phase(Card(CardValue.TWO, CardColor.DIAMONDS))
                    .add_card_flop_phase(Card(CardValue.ACE, CardColor.SPADES))
                    .launch_phase_and_get_best_players()
    )
    assert("Steve" in best_players or "Natacha" in best_players)

def test_2():
    false_cards = [Card(CardValue.TWO, CardColor.CLUBS)]
    best_players = (TurnPhaseDriver(FakeMultiDrawCards(false_cards))
                    .add_player("Steve")
                    .add_player("Natacha")
                    .add_card_before_flop_phase(Card(CardValue.TWO, CardColor.SPADES), "Steve")
                    .add_card_before_flop_phase(Card(CardValue.ACE, CardColor.HEARTS), "Natacha")
                    .add_card_before_flop_phase(Card(CardValue.SIX, CardColor.SPADES), "Steve")
                    .add_card_before_flop_phase(Card(CardValue.ACE, CardColor.CLUBS), "Natacha")
                    .add_card_flop_phase(Card(CardValue.TWO, CardColor.HEARTS))
                    .add_card_flop_phase(Card(CardValue.TWO, CardColor.DIAMONDS))
                    .add_card_flop_phase(Card(CardValue.ACE, CardColor.SPADES))
                    .launch_phase_and_get_best_players()
    )
    assert(["Steve"] == best_players)

def test_3():
    false_cards = [Card(CardValue.THREE, CardColor.CLUBS)]
    best_players = (TurnPhaseDriver(FakeMultiDrawCards(false_cards))
                    .add_player("Steve")
                    .add_player("Natacha")
                    .add_card_before_flop_phase(Card(CardValue.TWO, CardColor.SPADES), "Steve")
                    .add_card_before_flop_phase(Card(CardValue.ACE, CardColor.HEARTS), "Natacha")
                    .add_card_before_flop_phase(Card(CardValue.SIX, CardColor.SPADES), "Steve")
                    .add_card_before_flop_phase(Card(CardValue.ACE, CardColor.CLUBS), "Natacha")
                    .add_card_flop_phase(Card(CardValue.TWO, CardColor.HEARTS))
                    .add_card_flop_phase(Card(CardValue.TWO, CardColor.DIAMONDS))
                    .add_card_flop_phase(Card(CardValue.ACE, CardColor.SPADES))
                    .launch_phase_and_get_best_players()
    )
    assert(["Natacha"] == best_players)

def test_4():
    false_cards = [Card(CardValue.THREE, CardColor.CLUBS)]
    best_players = (TurnPhaseDriver(FakeMultiDrawCards(false_cards))
                    .add_player("Steve")
                    .add_player("Natacha")
                    .add_card_before_flop_phase(Card(CardValue.TWO, CardColor.SPADES), "Steve")
                    .add_card_before_flop_phase(Card(CardValue.TWO, CardColor.HEARTS), "Natacha")
                    .add_card_before_flop_phase(Card(CardValue.ACE, CardColor.DIAMONDS), "Steve")
                    .add_card_before_flop_phase(Card(CardValue.ACE, CardColor.CLUBS), "Natacha")
                    .add_card_flop_phase(Card(CardValue.FOUR, CardColor.HEARTS))
                    .add_card_flop_phase(Card(CardValue.JACK, CardColor.DIAMONDS))
                    .add_card_flop_phase(Card(CardValue.SIX, CardColor.SPADES))
                    .launch_phase_and_get_best_players()
    )
    assert(["Steve", "Natacha"] == best_players)

def test_5():
    best_players = (TurnPhaseDriver(MultiDrawCards())
                    .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                    .add_card_before_flop_phase(Card(CardValue.ACE, CardColor.SPADES), "Steve")
                    .add_card_before_flop_phase(Card(CardValue.KING, CardColor.CLUBS), "Natacha")
                    .add_card_before_flop_phase(Card(CardValue.QUEEN, CardColor.HEARTS), "Tony")
                    .add_card_before_flop_phase(Card(CardValue.JACK, CardColor.DIAMONDS), "Thor")
                    .add_card_before_flop_phase(Card(CardValue.TEN, CardColor.CLUBS), "Bruce")
                    .add_card_before_flop_phase(Card(CardValue.NINE, CardColor.DIAMONDS), "Clint")
                    .add_card_before_flop_phase(Card(CardValue.EIGHT, CardColor.HEARTS), "Carol")
                    .add_card_before_flop_phase(Card(CardValue.SEVEN, CardColor.SPADES), "T'Challa")
                    .add_card_before_flop_phase(Card(CardValue.SIX, CardColor.CLUBS), "Steven")
                    .add_card_before_flop_phase(Card(CardValue.FIVE, CardColor.DIAMONDS), "Wanda")
                    .add_card_before_flop_phase(Card(CardValue.FOUR, CardColor.HEARTS), "Steve")
                    .add_card_before_flop_phase(Card(CardValue.THREE, CardColor.SPADES), "Natacha")
                    .add_card_before_flop_phase(Card(CardValue.TWO, CardColor.CLUBS), "Tony")
                    .add_card_before_flop_phase(Card(CardValue.ACE, CardColor.DIAMONDS), "Thor")
                    .add_card_before_flop_phase(Card(CardValue.KING, CardColor.HEARTS), "Bruce")
                    .add_card_before_flop_phase(Card(CardValue.QUEEN, CardColor.SPADES), "Clint")
                    .add_card_before_flop_phase(Card(CardValue.JACK, CardColor.CLUBS), "Carol")
                    .add_card_before_flop_phase(Card(CardValue.TEN, CardColor.DIAMONDS), "T'Challa")
                    .add_card_before_flop_phase(Card(CardValue.NINE, CardColor.HEARTS), "Steven")
                    .add_card_before_flop_phase(Card(CardValue.EIGHT, CardColor.SPADES), "Wanda")                    
                    .add_card_flop_phase(Card(CardValue.FOUR, CardColor.CLUBS))
                    .add_card_flop_phase(Card(CardValue.JACK, CardColor.HEARTS))
                    .add_card_flop_phase(Card(CardValue.SIX, CardColor.SPADES))
                    .launch_phase_and_get_best_players())
    assert("Steve" in  best_players or "Natacha" in  best_players or "Tony" in  best_players 
               or "Thor" in  best_players  or "Bruce" in  best_players  or "Clint" in  best_players 
               or "Carol" in best_players or "T'Challa" in best_players or "Steven" in best_players
               or "Peter" in best_players or "Wanda" in best_players)

def test_6():
    fake_cards = [Card(CardValue.QUEEN, CardColor.DIAMONDS)]
    best_players = (TurnPhaseDriver(FakeMultiDrawCards(fake_cards))
                    .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                    .add_card_before_flop_phase(Card(CardValue.ACE, CardColor.SPADES), "Steve")
                    .add_card_before_flop_phase(Card(CardValue.KING, CardColor.CLUBS), "Natacha")
                    .add_card_before_flop_phase(Card(CardValue.QUEEN, CardColor.HEARTS), "Tony")
                    .add_card_before_flop_phase(Card(CardValue.JACK, CardColor.DIAMONDS), "Thor")
                    .add_card_before_flop_phase(Card(CardValue.TEN, CardColor.CLUBS), "Bruce")
                    .add_card_before_flop_phase(Card(CardValue.NINE, CardColor.DIAMONDS), "Clint")
                    .add_card_before_flop_phase(Card(CardValue.EIGHT, CardColor.HEARTS), "Carol")
                    .add_card_before_flop_phase(Card(CardValue.SEVEN, CardColor.SPADES), "T'Challa")
                    .add_card_before_flop_phase(Card(CardValue.SIX, CardColor.CLUBS), "Steven")
                    .add_card_before_flop_phase(Card(CardValue.FIVE, CardColor.DIAMONDS), "Wanda")
                    .add_card_before_flop_phase(Card(CardValue.FOUR, CardColor.HEARTS), "Steve")
                    .add_card_before_flop_phase(Card(CardValue.THREE, CardColor.SPADES), "Natacha")
                    .add_card_before_flop_phase(Card(CardValue.TWO, CardColor.CLUBS), "Tony")
                    .add_card_before_flop_phase(Card(CardValue.ACE, CardColor.DIAMONDS), "Thor")
                    .add_card_before_flop_phase(Card(CardValue.SEVEN, CardColor.HEARTS), "Bruce")
                    .add_card_before_flop_phase(Card(CardValue.QUEEN, CardColor.SPADES), "Clint")
                    .add_card_before_flop_phase(Card(CardValue.JACK, CardColor.CLUBS), "Carol")
                    .add_card_before_flop_phase(Card(CardValue.TEN, CardColor.DIAMONDS), "T'Challa")
                    .add_card_before_flop_phase(Card(CardValue.NINE, CardColor.HEARTS), "Steven")
                    .add_card_before_flop_phase(Card(CardValue.EIGHT, CardColor.SPADES), "Wanda")                 
                    .add_card_flop_phase(Card(CardValue.TEN, CardColor.HEARTS))
                    .add_card_flop_phase(Card(CardValue.SIX, CardColor.DIAMONDS))
                    .add_card_flop_phase(Card(CardValue.FOUR, CardColor.SPADES))
                    .launch_phase_and_get_best_players())
    assert(["Tony", "Clint"] ==  best_players)

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

    def add_player(self, player_name):
        self.hand_manager.add_player(player_name)
        return self 

    def add_players(self, players_name): 
            for player_name in players_name:
                self.hand_manager.add_player(player_name)
            return self

    def add_card_before_flop_phase(self, card, player_name):
        self.hand_manager.add_cards_to_players(player_name, card)
        return self

    def add_card_flop_phase(self, card):
        for player_name in self.hand_manager.get_all_players() : 
            self.hand_manager.add_cards_to_players(player_name, card)
        return self

    def launch_phase_and_get_best_players(self):        
        turn_phase = TurnPhase(self.hand_manager, self.multi_draw_cards)
        best_players = turn_phase.launch_phase_and_get_best_players()
        return best_players