from SocialNetwork.domain.account import Account
from SocialNetwork.domain.wall import Wall

def test_one_person_post_alone(): 
    posting_driver = PostingDriver()
    all_messages = (posting_driver
                    .post_message("Peter", "Hello every body")
                    .post_message("Peter", "Some one is here")
                    .post_message("Peter", "I will enjoy this meal!!!")
                    .post_message("Peter", "Why my soccer team is bad?")
                    .check_messages())
    assert(len(all_messages) == 1)
    assert(len(all_messages["Peter"]) == 4)

def test_three_friends_post():
    posting_driver = PostingDriver()
    all_messages = (posting_driver
                    .post_message("Harry", "Some one want to go eat some Pizza?")
                    .post_message("Ron", "Yes me!!!")
                    .post_message("Hermione", "Harry, Ron go back to study for the exams!!!!")
                    .post_message("Harry", "Hermione be nice we do not stop to study")
                    .post_message("Ron", "Stop to be boring!!!!")
                    .check_messages())
    assert(len(all_messages) == 3)
    assert(len(all_messages["Harry"]) == 2)
    assert(len(all_messages["Ron"]) == 2)
    assert(len(all_messages["Hermione"]) == 1)

class PostingDriver :
    def __init__(self):
        self.wall = Wall()

    def post_message(self, account_name, message):       
        self.wall.post_messages(account_name, message)
        return self
    
    def check_messages(self):
        all_messages = {}
        for account_name in self.wall.get_all_accounts() : 
            all_messages[account_name] = self.wall.get_messages_from_accounts(account_name)
        return all_messages