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
from PokerHandsV2.hand import Hand
from PokerHandsV2.tests.fake_multi_draw_cards import FakeMultiDrawCards

def test_1():
    best_players = (CompareHandsAfterFlopDriver(MultiDrawCards())
                    .add_player("Steve")
                    .add_player("Natacha")
                    .add_card_before_flop(Card(CardValue.TWO, CardColor.SPADES), "Steve")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.HEARTS), "Natacha")
                    .add_card_before_flop(Card(CardValue.SIX, CardColor.SPADES), "Steve")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.CLUBS), "Natacha")
                    .draw_flop()
                    .determinate_players_winners())                    
    assert("Steve" in best_players or "Natacha" in best_players)

def test_2(): 
    fake_cards = [Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.QUEEN, CardColor.SPADES), Card(CardValue.EIGHT, CardColor.SPADES)]
    best_players = (CompareHandsAfterFlopDriver(FakeMultiDrawCards(fake_cards))
                    .add_player("Steve")
                    .add_player("Natacha")
                    .add_card_before_flop(Card(CardValue.TWO, CardColor.SPADES), "Steve")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.HEARTS), "Natacha")
                    .add_card_before_flop(Card(CardValue.SIX, CardColor.SPADES), "Steve")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.CLUBS), "Natacha")
                    .draw_flop()
                    .determinate_players_winners()
                    )  
    assert(["Steve"] == best_players)

def test_3(): 
    fake_cards = [Card(CardValue.ACE, CardColor.SPADES), Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.CLUBS)]
    best_players = (CompareHandsAfterFlopDriver(FakeMultiDrawCards(fake_cards))
                    .add_player("Steve")
                    .add_player("Natacha")
                    .add_card_before_flop(Card(CardValue.TWO, CardColor.SPADES), "Steve")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.HEARTS), "Natacha")
                    .add_card_before_flop(Card(CardValue.SIX, CardColor.SPADES), "Steve")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.CLUBS), "Natacha")
                    .draw_flop()
                    .determinate_players_winners()
                    )  
    assert(["Natacha"] == best_players)

def test_4(): 
    fake_cards = [Card(CardValue.KING, CardColor.SPADES), Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.CLUBS)]
    best_players = (CompareHandsAfterFlopDriver(FakeMultiDrawCards(fake_cards))
                    .add_player("Steve")
                    .add_player("Natacha")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.SPADES), "Steve")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.HEARTS), "Natacha")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.DIAMONDS), "Steve")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.CLUBS), "Natacha")
                    .draw_flop()
                    .determinate_players_winners()
                    )  
    assert(["Steve", "Natacha"] == best_players)

def test_5(): 
    fake_cards = [Card(CardValue.KING, CardColor.SPADES), Card(CardValue.QUEEN, CardColor.HEARTS), Card(CardValue.EIGHT, CardColor.CLUBS)]
    best_players = (CompareHandsAfterFlopDriver(FakeMultiDrawCards(fake_cards))
                    .add_player("Steve")
                    .add_player("Natacha")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.SPADES), "Steve")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.HEARTS), "Natacha")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.DIAMONDS), "Steve")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.CLUBS), "Natacha")
                    .draw_flop()
                    .determinate_players_winners()
                    )  
    assert(["Steve", "Natacha"] == best_players)

def test_6():
    best_players = (CompareHandsAfterFlopDriver(MultiDrawCards())
                    .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.SPADES), "Steve")
                    .add_card_before_flop(Card(CardValue.KING, CardColor.CLUBS), "Natacha")
                    .add_card_before_flop(Card(CardValue.QUEEN, CardColor.HEARTS), "Tony")
                    .add_card_before_flop(Card(CardValue.JACK, CardColor.DIAMONDS), "Thor")
                    .add_card_before_flop(Card(CardValue.TEN, CardColor.CLUBS), "Bruce")
                    .add_card_before_flop(Card(CardValue.NINE, CardColor.DIAMONDS), "Clint")
                    .add_card_before_flop(Card(CardValue.EIGHT, CardColor.HEARTS), "Carol")
                    .add_card_before_flop(Card(CardValue.SEVEN, CardColor.SPADES), "T'Challa")
                    .add_card_before_flop(Card(CardValue.SIX, CardColor.CLUBS), "Steven")
                    .add_card_before_flop(Card(CardValue.FIVE, CardColor.DIAMONDS), "Wanda")
                    .add_card_before_flop(Card(CardValue.FOUR, CardColor.HEARTS), "Steve")
                    .add_card_before_flop(Card(CardValue.THREE, CardColor.SPADES), "Natacha")
                    .add_card_before_flop(Card(CardValue.TWO, CardColor.CLUBS), "Tony")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.DIAMONDS), "Thor")
                    .add_card_before_flop(Card(CardValue.KING, CardColor.HEARTS), "Bruce")
                    .add_card_before_flop(Card(CardValue.QUEEN, CardColor.SPADES), "Clint")
                    .add_card_before_flop(Card(CardValue.JACK, CardColor.CLUBS), "Carol")
                    .add_card_before_flop(Card(CardValue.TEN, CardColor.DIAMONDS), "T'Challa")
                    .add_card_before_flop(Card(CardValue.NINE, CardColor.HEARTS), "Steven")
                    .add_card_before_flop(Card(CardValue.EIGHT, CardColor.SPADES), "Wanda")
                    .draw_flop()
                    .determinate_players_winners())
    assert("Steve" in  best_players or "Natacha" in  best_players or "Tony" in  best_players 
               or "Thor" in  best_players  or "Bruce" in  best_players  or "Clint" in  best_players 
               or "Carol" in best_players or "T'Challa" in best_players or "Steven" in best_players
               or "Peter" in best_players or "Wanda" in best_players)

def test_7():
    fake_cards = [Card(CardValue.ACE, CardColor.HEARTS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES)]
    best_players = (CompareHandsAfterFlopDriver(FakeMultiDrawCards(fake_cards))
                    .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.SPADES), "Steve")
                    .add_card_before_flop(Card(CardValue.KING, CardColor.CLUBS), "Natacha")
                    .add_card_before_flop(Card(CardValue.QUEEN, CardColor.HEARTS), "Tony")
                    .add_card_before_flop(Card(CardValue.JACK, CardColor.DIAMONDS), "Thor")
                    .add_card_before_flop(Card(CardValue.TEN, CardColor.CLUBS), "Bruce")
                    .add_card_before_flop(Card(CardValue.NINE, CardColor.DIAMONDS), "Clint")
                    .add_card_before_flop(Card(CardValue.EIGHT, CardColor.HEARTS), "Carol")
                    .add_card_before_flop(Card(CardValue.SEVEN, CardColor.SPADES), "T'Challa")
                    .add_card_before_flop(Card(CardValue.SIX, CardColor.CLUBS), "Steven")
                    .add_card_before_flop(Card(CardValue.FIVE, CardColor.DIAMONDS), "Wanda")
                    .add_card_before_flop(Card(CardValue.FOUR, CardColor.HEARTS), "Steve")
                    .add_card_before_flop(Card(CardValue.THREE, CardColor.SPADES), "Natacha")
                    .add_card_before_flop(Card(CardValue.TWO, CardColor.CLUBS), "Tony")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.DIAMONDS), "Thor")
                    .add_card_before_flop(Card(CardValue.KING, CardColor.HEARTS), "Bruce")
                    .add_card_before_flop(Card(CardValue.QUEEN, CardColor.SPADES), "Clint")
                    .add_card_before_flop(Card(CardValue.JACK, CardColor.CLUBS), "Carol")
                    .add_card_before_flop(Card(CardValue.TEN, CardColor.DIAMONDS), "T'Challa")
                    .add_card_before_flop(Card(CardValue.NINE, CardColor.HEARTS), "Steven")
                    .add_card_before_flop(Card(CardValue.EIGHT, CardColor.SPADES), "Wanda")
                    .draw_flop()
                    .determinate_players_winners())
    assert(["Steve"] ==  best_players)

def test_8():
    fake_cards = [Card(CardValue.TEN, CardColor.HEARTS), Card(CardValue.SIX, CardColor.DIAMONDS), Card(CardValue.FOUR, CardColor.SPADES)]
    best_players = (CompareHandsAfterFlopDriver(FakeMultiDrawCards(fake_cards))
                    .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.SPADES), "Steve")
                    .add_card_before_flop(Card(CardValue.KING, CardColor.CLUBS), "Natacha")
                    .add_card_before_flop(Card(CardValue.QUEEN, CardColor.HEARTS), "Tony")
                    .add_card_before_flop(Card(CardValue.JACK, CardColor.DIAMONDS), "Thor")
                    .add_card_before_flop(Card(CardValue.TEN, CardColor.CLUBS), "Bruce")
                    .add_card_before_flop(Card(CardValue.NINE, CardColor.DIAMONDS), "Clint")
                    .add_card_before_flop(Card(CardValue.EIGHT, CardColor.HEARTS), "Carol")
                    .add_card_before_flop(Card(CardValue.SEVEN, CardColor.SPADES), "T'Challa")
                    .add_card_before_flop(Card(CardValue.SIX, CardColor.CLUBS), "Steven")
                    .add_card_before_flop(Card(CardValue.FIVE, CardColor.DIAMONDS), "Wanda")
                    .add_card_before_flop(Card(CardValue.FOUR, CardColor.HEARTS), "Steve")
                    .add_card_before_flop(Card(CardValue.THREE, CardColor.SPADES), "Natacha")
                    .add_card_before_flop(Card(CardValue.TWO, CardColor.CLUBS), "Tony")
                    .add_card_before_flop(Card(CardValue.ACE, CardColor.DIAMONDS), "Thor")
                    .add_card_before_flop(Card(CardValue.SEVEN, CardColor.HEARTS), "Bruce")
                    .add_card_before_flop(Card(CardValue.QUEEN, CardColor.SPADES), "Clint")
                    .add_card_before_flop(Card(CardValue.JACK, CardColor.CLUBS), "Carol")
                    .add_card_before_flop(Card(CardValue.TEN, CardColor.DIAMONDS), "T'Challa")
                    .add_card_before_flop(Card(CardValue.NINE, CardColor.HEARTS), "Steven")
                    .add_card_before_flop(Card(CardValue.EIGHT, CardColor.SPADES), "Wanda")
                    .draw_flop()
                    .determinate_players_winners())
    assert(["Bruce", "T'Challa"] ==  best_players)

class CompareHandsAfterFlopDriver():
    def __init__(self, multi_draw_cards):
        self.card_players = {}
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

    def add_card_before_flop(self, card, player_name):
        if player_name not in self.card_players : 
            self.card_players[player_name]=[]
        self.card_players[player_name].append(card)
        return self

    def draw_flop(self): 
        flop = []
        i = 0
        while i < 3 :
            new_card = self.multi_draw_cards.draw_one_card()
            flop.append(new_card)
            i += 1
        for player_name in self.card_players : 
            for card in flop : 
                self.card_players[player_name].append(card)
            self.hand_manager.give_specific_hand(player_name, self.card_players[player_name])
        return self

    def determinate_players_winners(self):
        best_players = self.hand_manager.get_players_with_best_hands()
        return best_players