from Tricount_EventStorming.participant import Participant, CREDITOR, DEBTOR
from Tricount_EventStorming.refund import Refund


def test_with_only_one_refund_generous_friend(): 
    participant = Participant("Pompée", -10, DEBTOR)
    generous_friends = [Participant("César", 20, CREDITOR),Participant("Crassus", 100, CREDITOR)]
    refunds = participant.paid_generous_friends(generous_friends)
    
    refunds_expected = [Refund("Pompée", "César", 10)]
    assert(refunds_expected == refunds)

def test_with_only_two_refund_generous_friend(): 
    participant = Participant("Pompée", -120, DEBTOR)
    generous_friends = [Participant("César", 20, CREDITOR),Participant("Crassus", 100, CREDITOR)]
    refunds = participant.paid_generous_friends(generous_friends)
    
    refunds_expected = [Refund("Pompée", "César", 20), Refund("Pompée", "Crassus", 100)]
    assert(refunds_expected == refunds)
