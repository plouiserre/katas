from PokerHands.deck import Deck

def test_check_in_one_time_you_drawn_randownly_five_cards_uniques() : 
    all_cards_drawned = drawn_randomly_five_cards()
    
    assert(len(all_cards_drawned) == 5)
    assert(len(all_cards_drawned) == len(set(all_cards_drawned)))

def test_check_in_one_tousand_time_you_drawn_randownly_five_cards_uniques() : 
    attempt = 0
    while attempt < 5000 :
        all_cards_drawned = drawn_randomly_five_cards()
                
        assert(len(all_cards_drawned) == 5)
        assert(len(all_cards_drawned) == len(set(all_cards_drawned)))
        attempt += 1

def drawn_randomly_five_cards():
    deck = Deck()
    return deck.drawn_five_cards()
