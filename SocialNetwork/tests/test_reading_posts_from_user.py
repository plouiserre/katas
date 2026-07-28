from SocialNetwork.domain.account import Account
from SocialNetwork.domain.search import Search

def test_get_messages_from_peter_unique_user():
    all_accounts = {"Peter" : Account("Peter", ["Hello every body", "Some one is here", "I will enjoy this meal!!!", "Why my soccer team is bad?"])}
    reading_driver = ReadingDriver(all_accounts)
    all_messages_peter = reading_driver.read_all_messages_from_specific_user("Peter")
    assert(len(all_messages_peter) == 4)
    assert(all_messages_peter[0] == "Hello every body")
    assert(all_messages_peter[1] == "Some one is here")
    assert(all_messages_peter[2] == "I will enjoy this meal!!!")
    assert(all_messages_peter[3] == "Why my soccer team is bad?")

def test_get_messages_from_three_friends_separate():
    all_accounts = {"Harry" : Account("Harry", ["Some one want to go eat some Pizza?", "Hermione be nice we do not stop to study"]), 
                    "Ron" : Account("Ron", ["Yes me!!!", "Stop to be boring!!!!"]), 
                    "Hermione" : Account("Hermione", ["Harry, Ron go back to study for the exams!!!!"])}
    reading_driver = ReadingDriver(all_accounts)

    all_messages_harry = reading_driver.read_all_messages_from_specific_user("Harry")
    all_messages_ron = reading_driver.read_all_messages_from_specific_user("Ron")
    all_messages_hermione = reading_driver.read_all_messages_from_specific_user("Hermione")
                
    assert(len(all_messages_harry) == 2)
    assert(all_messages_harry[0] == "Some one want to go eat some Pizza?")
    assert(all_messages_harry[1] == "Hermione be nice we do not stop to study")
    assert(len(all_messages_ron) == 2)
    assert(all_messages_ron[0] == "Yes me!!!")
    assert(all_messages_ron[1] == "Stop to be boring!!!!")
    assert(len(all_messages_hermione) == 1)
    assert(all_messages_hermione[0] == "Harry, Ron go back to study for the exams!!!!")

class ReadingDriver : 
    def __init__(self, all_accounts):
        self.accounts = all_accounts              

    def read_all_messages_from_specific_user(self, account_name): 
        search = Search(self.accounts)
        return search.all_messages_from_specific_accounts(account_name)