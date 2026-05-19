class Hand :
    def __init__(self, content_hand):
        # self.hand_name = hand_name
        # self.score_name = score_name
        self.content = content_hand
        self.counting_cards = {}

    def count_hand(self) : 
        self.counting_cards = {}
        for card in self.content : 
            if card.value in self.counting_cards : 
                self.counting_cards[card.value] += 1
            else : 
                self.counting_cards[card.value] = 1
        return self.counting_cards
        
    # def __eq__(self, other):
    #     return other.hand_name == self.hand_name and self.score_name == other.score_name 