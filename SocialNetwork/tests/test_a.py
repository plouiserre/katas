from SocialNetwork.domain.account import Account

def test_1(): 
    posting_driver = PostingDriver()
    all_messages = (posting_driver
                    .posts_message("Peter", "Hello every body")
                    .posts_message("Peter", "Some one is here")
                    .posts_message("Peter", "I will enjoy this meal!!!")
                    .posts_message("Peter", "Why my soccer team is bad?")
                    .check_messages(["Peter"]))
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
                    .check_messages(["Harry", "Ron", "Hermione"]))
    assert(len(all_messages) == 3)
    assert(len(all_messages["Harry"]) == 2)
    assert(len(all_messages["Ron"]) == 2)
    assert(len(all_messages["Hermione"]) == 1)

class PostingDriver :
    def __init__(self):
        self.accounts = {}

    def posts_message(self, account_name, message):       
        if account_name not in self.accounts : 
            self.accounts[account_name] = Account(account_name)
        self.accounts[account_name].messages.append(message)
        return self
    
    def check_messages(self, accounts_name):
        all_messages = {}
        for account_name in accounts_name : 
            all_messages[account_name] = self.accounts[account_name].messages
        return all_messages