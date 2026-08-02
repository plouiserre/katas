from SocialNetwork.domain.models.author import Author
from SocialNetwork.domain.models.message import Message
from SocialNetwork.domain.search import Search

def test_get_messages_from_peter_unique_user():
    all_accounts = [Message(Author("Peter"), "Hello every body"), Message(Author("Peter"), "Some one is here"),Message(Author("Peter"),  "I will enjoy this meal!!!"), 
                               Message(Author("Peter"), "Why my soccer team is bad?")]
    reading_driver = ReadingDriver()

    all_messages_peter = reading_driver.read_all_messages_from_specific_user(all_accounts, "Peter")
    assert(len(all_messages_peter) == 4)
    assert(all_messages_peter[0].content_message == "Hello every body")
    assert(all_messages_peter[1].content_message == "Some one is here")
    assert(all_messages_peter[2].content_message == "I will enjoy this meal!!!")
    assert(all_messages_peter[3].content_message == "Why my soccer team is bad?")

def test_get_messages_from_three_friends_separate():
    all_accounts = [Message(Author("Harry"), "Some one want to go eat some Pizza?"), Message(Author("Harry"),"Hermione be nice we do not stop to study"), 
                    Message(Author("Ron"), "Yes me!!!"), Message(Author("Ron"),"Stop to be boring!!!!"), 
                    Message(Author("Hermione"),"Harry, Ron go back to study for the exams!!!!")]
    reading_driver = ReadingDriver()

    all_messages_harry = reading_driver.read_all_messages_from_specific_user(all_accounts, "Harry")
    all_messages_ron = reading_driver.read_all_messages_from_specific_user(all_accounts, "Ron")
    all_messages_hermione = reading_driver.read_all_messages_from_specific_user(all_accounts, "Hermione")
                
    assert(len(all_messages_harry) == 2)
    assert(all_messages_harry[0].content_message == "Some one want to go eat some Pizza?")
    assert(all_messages_harry[1].content_message == "Hermione be nice we do not stop to study")
    assert(len(all_messages_ron) == 2)
    assert(all_messages_ron[0].content_message == "Yes me!!!")
    assert(all_messages_ron[1].content_message == "Stop to be boring!!!!")
    assert(len(all_messages_hermione) == 1)
    assert(all_messages_hermione[0].content_message == "Harry, Ron go back to study for the exams!!!!")

class ReadingDriver : 
    def __init__(self, ):
        self.accounts = {}            

    def read_all_messages_from_specific_user(self, all_accounts, account_name): 
        search = Search()
        return search.all_messages_from_specific_accounts(all_accounts, account_name)