from SocialNetwork.domain.account import Account

def test_1(): 
    posting_driver = PostingDriver()
    all_messages = (posting_driver
                    .posts_message("Peter", "Hello every body")
                    .posts_message("Peter", "Some one is here")
                    .posts_message("Peter", "I will enjoy this meal!!!")
                    .posts_message("Peter", "Why my soccer team is bad?")
                    .retrieve_all_messages())
    assert(len(all_messages) == 1)
    assert(len(all_messages["Peter"]) == 4)
    assert("Hello every body" == all_messages["Peter"][0])
    assert("Some one is here" == all_messages["Peter"][1])
    assert("I will enjoy this meal!!!" == all_messages["Peter"][2])
    assert("Why my soccer team is bad?" == all_messages["Peter"][3])

def test_2():
    posting_driver = PostingDriver()
    all_messages = (posting_driver
                    .posts_message("Harry", "Some one want to go eat some Pizza?")
                    .posts_message("Ron", "Yes me!!!")
                    .posts_message("Hermione", "Harry, Ron go back to study for the exams!!!!")
                    .posts_message("Harry", "Hermione be nice we do not stop to study")
                    .posts_message("Ron", "Stop to be boring!!!!")
                    .retrieve_all_messages()
    )
    assert(len(all_messages) == 3)
    assert(len(all_messages["Harry"]) == 2)
    assert("Some one want to go eat some Pizza?" == all_messages["Harry"][0])
    assert("Hermione be nice we do not stop to study" == all_messages["Harry"][1])
    assert(len(all_messages["Ron"]) == 2)
    assert("Yes me!!!" == all_messages["Ron"][0])
    assert("Stop to be boring!!!!" == all_messages["Ron"][1])
    assert(len(all_messages["Hermione"]) == 1)
    assert("Harry, Ron go back to study for the exams!!!!" == all_messages["Hermione"][0])  

class PostingDriver :
    def __init__(self):
        self.messages = {}

    def posts_message(self, account_name, message): 
        if account_name not in self.messages : 
            self.messages[account_name] = []
        self.messages[account_name].append(message)
        return self
    
    def retrieve_all_messages(self):
        return self.messages   