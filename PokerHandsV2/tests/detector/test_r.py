# from PokerHandsV2.card import Card, CardColor, CardValue
# from PokerHandsV2.counting_cards import CountingCards

# def test_1():
#     (QuinteDetectorDriver()
#      .add_card("5♥")
#      .add_card("6♠")
#      .add_card("7♣")
#      .add_card("8♦")
#      .add_card("9♥")
#      .is_quinte_figure()
#      .is_his_high_card("9"))

# def test_2(): 
#     (QuinteDetectorDriver()
#         .add_card("9♥")
#         .add_card("6♠")
#         .add_card("8♦")
#         .add_card("5♥")
#         .add_card("7♣")
#         .is_quinte_figure()
#         .is_his_high_card("9")
#     )

# #TODO tests à faire 
# # - quinte simple DID
# # - quinte mixed
# # - quinte mixed où la highed card n'est pas 9
# # - quinte avec 7 cartes
# # - pas une quinte car pas 5 cartes au minimum 
# # - pas une quinte car ca ne se suit pas 
# # - pas une quinte car à cause des doublons pas cinq cartes qui se suivent
# # - quinte au départ commençant par as
# # - quinte flush aussi

# class QuinteDetectorDriver: 
#     def __init__(self):
#         self.cards = []
#         self.counting_cards = CountingCards()

#     def add_card(self, card_crypted): 
#         card = Card.parse(card_crypted)
#         self.cards.append(card)
#         return self

#     def is_quinte_figure(self):
#         card_sorted =self.counting_cards.Count(self.cards)
#         last_card = Card(CardValue.UNDEFINED, CardColor.UNDEFINED)        
#         card_is_following = True
#         for card_value in card_sorted : 
#             card = card_sorted[card_value]
#             if last_card == Card(CardValue.UNDEFINED, CardColor.UNDEFINED)  :
#                 last_card = card
#                 continue
#             else : 
#                 difference = card.value - last_card.value
#                 if difference != 1 : 
#                     card_is_following = False
#                     break
#                 else : 
#                     last_card = card
#                     continue
#         assert(card_is_following == True)
#         return self

#     def is_his_high_card(self, high_card):
#         is_valid = high_card == "9"
#         assert(is_valid == True)
#         return self