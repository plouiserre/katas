from SocialNetwork.domain.account import Account
from SocialNetwork.domain.wall import Wall

def test_one_person_post_alone(): 
    search_driver = SearchDriver()
    all_messages = (search_driver
                    .post_message("Peter", "Hello every body")
                    .post_message("Peter", "Some one is here")
                    .post_message("Peter", "I will enjoy this meal!!!")
                    .post_message("Peter", "Why my soccer team is bad?")
                    .search_message("Peter"))
    assert(len(all_messages) == 4)
    assert(all_messages[0] == "Hello every body")
    assert(all_messages[1] == "Some one is here")
    assert(all_messages[2] == "I will enjoy this meal!!!")
    assert(all_messages[3] == "Why my soccer team is bad?")

def test_three_friends_post():
    search_driver = SearchDriver()
    all_messages_harry = (search_driver
                    .post_message("Harry", "Some one want to go eat some Pizza?")
                    .post_message("Ron", "Yes me!!!")
                    .post_message("Hermione", "Harry, Ron go back to study for the exams!!!!")
                    .post_message("Harry", "Hermione be nice we do not stop to study")
                    .post_message("Ron", "Stop to be boring!!!!")
                    .search_message("Harry"))
    all_messages_ron = search_driver.search_message("Ron")
    all_messages_hermione = search_driver.search_message("Hermione")
    assert(len(all_messages_harry) == 2)
    assert(all_messages_harry[0] == "Some one want to go eat some Pizza?")
    assert(all_messages_harry[1] == "Hermione be nice we do not stop to study")
    assert(len(all_messages_ron) == 2)
    assert(all_messages_ron[0] == "Yes me!!!")
    assert(all_messages_ron[1] == "Stop to be boring!!!!")
    assert(len(all_messages_hermione) == 1)
    assert(all_messages_hermione[0] == "Harry, Ron go back to study for the exams!!!!")

class SearchDriver: 
    def __init__(self):
        self.wall = Wall()

    def post_message(self, account_name :str , message : str): 
        self.wall.post_messages(account_name, message)
        return self

    def search_message(self, account_name):
        all_accounts = self.wall.get_all_accounts()
        messages = []
        for key_account_name in all_accounts : 
            if key_account_name == account_name :
                messages = all_accounts[key_account_name].messages
                break
        return messages