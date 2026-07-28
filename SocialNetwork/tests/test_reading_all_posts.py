from SocialNetwork.domain.account import Account
from SocialNetwork.domain.wall import Wall

def test_get_messages_from_peter_unique_user():
    all_accounts = {"Peter" : Account("Peter", ["Hello every body", "Some one is here", "I will enjoy this meal!!!", "Why my soccer team is bad?"])}
    reading_driver = ReadingDriver()
    reading_driver.add_all_posts_for_init(all_accounts)
    
    all_messages = reading_driver.read_all_messages()
    assert(len(all_messages) == 1)
    assert(len(all_messages["Peter"]) == 4)
    assert(all_messages["Peter"][0] == "Hello every body")
    assert(all_messages["Peter"][1] == "Some one is here")
    assert(all_messages["Peter"][2] == "I will enjoy this meal!!!")
    assert(all_messages["Peter"][3] == "Why my soccer team is bad?")

def test_get_messages_from_three_friends_separate():
    all_accounts = {"Harry" : Account("Harry", ["Some one want to go eat some Pizza?", "Hermione be nice we do not stop to study"]), 
                    "Ron" : Account("Ron", ["Yes me!!!", "Stop to be boring!!!!"]), 
                    "Hermione" : Account("Hermione", ["Harry, Ron go back to study for the exams!!!!"])}
    reading_driver = ReadingDriver()
    reading_driver.add_all_posts_for_init(all_accounts)

    all_messages = reading_driver.read_all_messages()

    all_messages_harry = all_messages["Harry"]
    all_messages_ron = all_messages["Ron"]
    all_messages_hermione = all_messages["Hermione"]

    assert(len(all_messages) == 3)

    assert(len(all_messages_harry) == 2)
    assert(all_messages_harry[0] == "Some one want to go eat some Pizza?")
    assert(all_messages_harry[1] == "Hermione be nice we do not stop to study")
    assert(len(all_messages_ron) == 2)
    assert(all_messages_ron[0] == "Yes me!!!")
    assert(all_messages_ron[1] == "Stop to be boring!!!!")
    assert(len(all_messages_hermione) == 1)
    assert(all_messages_hermione[0] == "Harry, Ron go back to study for the exams!!!!")

class ReadingDriver : 
    def __init__(self):
        self.wall = Wall() 

    def add_all_posts_for_init(self, all_accounts):
        for key_account_name in all_accounts : 
            account = all_accounts[key_account_name]
            for message in account.messages :                 
                self.wall.post_messages(key_account_name, message)

    def read_all_messages(self): 
        messages = self.wall.get_all_messages_from_all_accounts()
        return messages