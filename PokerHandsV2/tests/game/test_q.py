# from enum import Enum

# from PokerHandsV2.counting_cards import CountingCards
# from PokerHandsV2.detector.four_cards_detector import FourCardsDetector
# from PokerHandsV2.detector.flush_detector import FlushDetector
# from PokerHandsV2.detector.full_detector import FullDetector
# from PokerHandsV2.detector.high_card_detector import HighCardDetector
# from PokerHandsV2.detector.pair_detector import PairDetector
# from PokerHandsV2.detector.quinte_flush_detector import QuinteFlushDetector
# from PokerHandsV2.detector.straight_detector import StraightDetector
# from PokerHandsV2.detector.three_cards_detector import ThreeCardsDetector
# from PokerHandsV2.detector.two_pairs_detector import TwoPairsDetector
# from PokerHandsV2.draw.multi_draw_cards import MultiDrawCards
# from PokerHandsV2.game.draw_phase import DrawPhase
# from PokerHandsV2.game.flop_phase import FlopPhase
# from PokerHandsV2.game.hands_manager import HandsManager
# from PokerHandsV2.game.river_phase import RiverPhase
# from PokerHandsV2.game.turn_phase import TurnPhase
# from PokerHandsV2.hand import Hand
# from PokerHandsV2.tests.fake_multi_draw_cards import FakeMultiDrawCards



# class PhasePoker(Enum) : 
#     DRAW = 1
#     FLOP = 2
#     TURN = 3
#     RIVER = 4

# def test_1():
#     (PartyDriver(MultiDrawCards())
#             .add_players(["Steve", "Natacha"])
#             .launch_party()
#             .is_this_players_can_be_a_winner(["Steve", "Natacha"], PhasePoker.DRAW)
#             .is_this_players_can_be_a_winner(["Steve", "Natacha"], PhasePoker.FLOP)
#             .is_this_players_can_be_a_winner(["Steve", "Natacha"], PhasePoker.TURN)
#             .is_this_players_can_be_a_winner(["Steve", "Natacha"], PhasePoker.RIVER)
#     )

# #♣♠♥♦
# def test_2(): 
#     fake_cards = ["K♣", "Q♠", "Q♥", "J♦", "A♣", "10♠", "9♥", "8♦", "J♣"]
#     (PartyDriver(FakeMultiDrawCards(fake_cards))
#                 .add_players(["Steve", "Natacha"])
#                 .launch_party()
#                 .is_this_players_can_be_a_winner(["Steve"], PhasePoker.DRAW)
#                 .is_this_players_can_be_a_winner(["Steve_Natacha"], PhasePoker.FLOP)
#                 .is_this_players_can_be_a_winner(["Natacha"], PhasePoker.TURN)
#                 .is_this_players_can_be_a_winner(["Steve"], PhasePoker.RIVER)
#         )

# class PartyDriver: 
#     def __init__(self, multi_draw_cards):
#         counting_cards = CountingCards()
#         high_card_detector = HighCardDetector()
#         pair_detector = PairDetector(counting_cards)
#         two_pairs_detector = TwoPairsDetector(counting_cards)
#         three_cards_detector = ThreeCardsDetector(counting_cards)
#         straight_detector = StraightDetector(counting_cards)
#         flush_detector = FlushDetector()
#         full_detector = FullDetector(counting_cards)
#         four_cards_detector = FourCardsDetector(counting_cards)
#         quinte_flush_detector = QuinteFlushDetector()
#         hand = Hand(high_card_detector, pair_detector, two_pairs_detector, three_cards_detector, straight_detector, flush_detector, full_detector, four_cards_detector, quinte_flush_detector)
#         self.multi_draw_cards = multi_draw_cards
#         self.hand_manager = HandsManager(hand, self.multi_draw_cards)
#         self.players = []
#         self.winners = {}

#     def add_players(self, players_name):
#         for player_name in players_name : 
#             self.players.append(player_name)
#         return self

#     def launch_party(self):
#         draw_phase = DrawPhase(self.players, self.hand_manager)
#         self.winners[PhasePoker.DRAW] = draw_phase.launch_phase_and_get_best_players()
#         flop_phase = FlopPhase(self.hand_manager, self.multi_draw_cards)
#         self.winners[PhasePoker.FLOP] = flop_phase.launch_phase_and_get_best_players()
#         turn_phase = TurnPhase(self.hand_manager, self.multi_draw_cards)
#         self.winners[PhasePoker.TURN]  = turn_phase.launch_phase_and_get_best_players()
#         river_phase = RiverPhase(self.hand_manager, self.multi_draw_cards)
#         self.winners[PhasePoker.RIVER] = river_phase.launch_phase_and_get_best_players()
#         return self

#     def is_this_players_can_be_a_winner(self, players_name, phase):
#         winners_phase = self.winners[phase]
#         is_winner = False
#         for player_name in players_name : 
#             if "_" in player_name : 
#                 all_players = player_name.split("_")
#                 is_winner = all_players == winners_phase
#             else : 
#                 is_winner = player_name in winners_phase
#             if is_winner == True: 
#                 break
#         assert (is_winner == True)
#         return self 