from SocialNetwork.domain.account import Account
def test_1():
    all_accounts = {"Peter" : Account("Peter", ["Hello every body", "Some one is here", "I will enjoy this meal!!!", "Why my soccer team is bad?"])}
    reading_driver = ReadingDriver(all_accounts)
    all_messages_peter = reading_driver.read_all_messages_from("Peter")
    assert(len(all_messages_peter) == 1)
    assert(len(all_messages_peter["Peter"]) == 4)
    assert(all_messages_peter["Peter"][0] == "Hello every body")
    assert(all_messages_peter["Peter"][1] == "Some one is here")
    assert(all_messages_peter["Peter"][2] == "I will enjoy this meal!!!")
    assert(all_messages_peter["Peter"][3] == "Why my soccer team is bad?")

def test_2():
    all_accounts = {"Harry" : Account("Harry", ["Some one want to go eat some Pizza?", "Hermione be nice we do not stop to study"]), 
                    "Ron" : Account("Ron", ["Yes me!!!", "Stop to be boring!!!!"]), 
                    "Hermione" : Account("Hermione", ["Harry, Ron go back to study for the exams!!!!"])}
    reading_driver = ReadingDriver(all_accounts)

    all_messages_harry = reading_driver.read_all_messages_from("Peter")
    all_messages_ron = reading_driver.read_all_messages_from("Peter")
    all_messages_hermione = reading_driver.read_all_messages_from("Peter")
                
    assert(len(all_messages_harry["Harry"]) == 2)
    assert(all_messages_harry["Harry"][0] == "Some one want to go eat some Pizza?")
    assert(all_messages_harry["Harry"][1] == "Hermione be nice we do not stop to study")
    assert(len(all_messages_ron["Ron"]) == 2)
    assert(all_messages_ron["Ron"][0] == "Yes me!!!")
    assert(all_messages_ron["Ron"][1] == "Stop to be boring!!!!")
    assert(len(all_messages_hermione["Hermione"]) == 1)
    assert(all_messages_hermione["Hermione"][0] == "Harry, Ron go back to study for the exams!!!!")

class ReadingDriver : 
    def __init__(self, all_accounts):
        self.accounts = all_accounts

    def read_all_messages_from(self, account_name): 
        messages = {}
        for account_name in self.accounts : 
            messages[account_name] = self.accounts[account_name].messages
        return messages