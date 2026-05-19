class Hand :
    def __init__(self, content_hand):
        self.content = content_hand
        self.counting_cards = {}

    def count_all_cards(self) : 
        self.counting_cards = {}
        for card in self.content : 
            if card.value in self.counting_cards : 
                self.counting_cards[card.value] += 1
            else : 
                self.counting_cards[card.value] = 1
        return self.counting_cards