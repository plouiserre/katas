from SocialNetwork.domain.account import Account
from SocialNetwork.domain.wall import Wall

def test_1(): 
    posting_driver = PostingDriver()
    all_messages = (posting_driver
                    .posts_message("Peter", "Hello every body")
                    .posts_message("Peter", "Some one is here")
                    .posts_message("Peter", "I will enjoy this meal!!!")
                    .posts_message("Peter", "Why my soccer team is bad?")
                    .check_messages())
    assert(len(all_messages) == 1)
    assert(len(all_messages["Peter"]) == 4)

def test_2():
    posting_driver = PostingDriver()
    all_messages = (posting_driver
                    .posts_message("Harry", "Some one want to go eat some Pizza?")
                    .posts_message("Ron", "Yes me!!!")
                    .posts_message("Hermione", "Harry, Ron go back to study for the exams!!!!")
                    .posts_message("Harry", "Hermione be nice we do not stop to study")
                    .posts_message("Ron", "Stop to be boring!!!!")
                    .check_messages())
    assert(len(all_messages) == 3)
    assert(len(all_messages["Harry"]) == 2)
    assert(len(all_messages["Ron"]) == 2)
    assert(len(all_messages["Hermione"]) == 1)

class PostingDriver :
    def __init__(self):
        self.accounts = {}
        self.wall = Wall()

    def posts_message(self, account_name, message):       
        self.wall.posts_messages(account_name, message)
        return self
    
    def check_messages(self):
        all_messages = {}
        for account_name in self.wall.accounts : 
            all_messages[account_name] = self.wall.accounts[account_name].messages
        return all_messages