from PokerHands.deck import Deck

def test_check_in_one_time_you_drawn_randownly_five_cards_uniques() : 
    all_cards_drawned_for_all_players = drawn_randomly_five_cards()
    
    _assert_all_cards_drawned_for_one_player_are_ok(all_cards_drawned_for_all_players)

def test_check_in_one_tousand_time_you_drawn_randownly_five_cards_uniques() : 
    attempt = 0
    while attempt < 5000 :
        all_cards_drawned_for_all_players = drawn_randomly_five_cards()
                
        _assert_all_cards_drawned_for_one_player_are_ok(all_cards_drawned_for_all_players)
        attempt += 1

def drawn_randomly_five_cards():
    deck = Deck()
    return deck.drawn_five_cards()

def _assert_all_cards_drawned_for_one_player_are_ok(all_cards_drawned_all_players) : 
    all_cards_drawned_first_player = all_cards_drawned_all_players[0]
    all_cards_drawned_second_player = all_cards_drawned_all_players[1]
    __assert_all_cards_drawned(all_cards_drawned_first_player)
    __assert_all_cards_drawned(all_cards_drawned_second_player)

def __assert_all_cards_drawned(all_cards_drawned) : 
    assert(len(all_cards_drawned) == 5)
    assert(len(all_cards_drawned) == len(set(all_cards_drawned)))