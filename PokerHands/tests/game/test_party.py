from PokerHands.draw.multi_draw_cards import MultiDrawCards
from PokerHands.game.party import Party, PhasePoker
from PokerHands.tests.fake_multi_draw_cards import FakeMultiDrawCards

def test_launch_random_party_with_two_players():
    (PartyDriver(MultiDrawCards())
            .add_players(["Steve", "Natacha"])
            .launch_party()
            .is_this_players_can_be_a_winner(["Steve", "Natacha"], PhasePoker.DRAW)
            .is_this_players_can_be_a_winner(["Steve", "Natacha"], PhasePoker.FLOP)
            .is_this_players_can_be_a_winner(["Steve", "Natacha"], PhasePoker.TURN)
            .is_this_players_can_be_a_winner(["Steve", "Natacha"], PhasePoker.RIVER)
    )

def test_launch_determine_party_with_two_players(): 
    fake_cards = ["K♣", "Q♠", "Q♥", "J♦", "A♣", "10♠", "9♥", "8♦", "J♣"]
    (PartyDriver(FakeMultiDrawCards(fake_cards))
                .add_players(["Steve", "Natacha"])
                .launch_party()
                .is_this_players_can_be_a_winner(["Steve"], PhasePoker.DRAW)
                .is_this_players_can_be_a_winner(["Steve_Natacha"], PhasePoker.FLOP)
                .is_this_players_can_be_a_winner(["Natacha"], PhasePoker.TURN)
                .is_this_players_can_be_a_winner(["Steve"], PhasePoker.RIVER)
        )

def test_launch_random_party_with_ten_players(): 
    (PartyDriver(MultiDrawCards())
                .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                .launch_party()
                .is_this_players_can_be_a_winner(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"], PhasePoker.DRAW)
                .is_this_players_can_be_a_winner(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"], PhasePoker.FLOP)
                .is_this_players_can_be_a_winner(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"], PhasePoker.TURN)
                .is_this_players_can_be_a_winner(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"], PhasePoker.RIVER)
        )

def test_launch_determine_party_with_ten_players(): 
    fake_cards = ["A♣", "K♠", "Q♥", "J♦", "10♣", "9♦", "8♥", "7♦", "6♣", "5♠", "4♥", "3♦", "2♣", "A♠", "K♥", "Q♦", "J♣", "10♠", "9♥", "8♥", "10♦", "10♥", "7♠", "J♦", "8♦"]
    (PartyDriver(FakeMultiDrawCards(fake_cards))
                .add_players(["Steve","Natacha","Tony","Thor","Bruce","Clint","Carol","T'Challa","Steven","Wanda"])
                .launch_party()
                .is_this_players_can_be_a_winner(["Thor"], PhasePoker.DRAW)
                .is_this_players_can_be_a_winner(["T'Challa"], PhasePoker.FLOP)
                .is_this_players_can_be_a_winner(["T'Challa"], PhasePoker.TURN)
                .is_this_players_can_be_a_winner(["Clint"], PhasePoker.RIVER)
        )

class PartyDriver: 
    def __init__(self, multi_draw_cards):
        self.party = Party(multi_draw_cards)
                
        self.players = []
        self.winners = {}

    def add_players(self, players_name):
        self.party.add_players(players_name)
        return self

    def launch_party(self):
        self.winners = self.party.launch_party()
        return self

    def is_this_players_can_be_a_winner(self, players_name, phase):
        winners_phase = self.winners[phase]
        is_winner = False
        for player_name in players_name : 
            if "_" in player_name : 
                all_players = player_name.split("_")
                is_winner = all_players == winners_phase
            else : 
                is_winner = player_name in winners_phase
            if is_winner == True: 
                break
        assert (is_winner == True)
        return self 