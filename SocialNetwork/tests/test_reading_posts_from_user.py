from SocialNetwork.domain.models.author import Author
from SocialNetwork.domain.models.post import Post
from SocialNetwork.domain.search import Search

def test_get_messages_from_peter_unique_user():
    all_accounts = [Post(Author("Peter"), "Hello every body"), Post(Author("Peter"), "Some one is here"),Post(Author("Peter"),  "I will enjoy this meal!!!"), 
                               Post(Author("Peter"), "Why my soccer team is bad?")]
    reading_driver = ReadingDriver()

    all_posts_peter = reading_driver.read_all_messages_from_specific_user(all_accounts, "Peter")
    assert(len(all_posts_peter) == 4)
    assert(all_posts_peter[0].content_message == "Hello every body")
    assert(all_posts_peter[1].content_message == "Some one is here")
    assert(all_posts_peter[2].content_message == "I will enjoy this meal!!!")
    assert(all_posts_peter[3].content_message == "Why my soccer team is bad?")

def test_get_messages_from_three_friends_separate():
    all_accounts = [Post(Author("Harry"), "Some one want to go eat some Pizza?"), Post(Author("Harry"),"Hermione be nice we do not stop to study"), 
                    Post(Author("Ron"), "Yes me!!!"), Post(Author("Ron"),"Stop to be boring!!!!"), 
                    Post(Author("Hermione"),"Harry, Ron go back to study for the exams!!!!")]
    reading_driver = ReadingDriver()

    all_posts_harry = reading_driver.read_all_messages_from_specific_user(all_accounts, "Harry")
    all_posts_ron = reading_driver.read_all_messages_from_specific_user(all_accounts, "Ron")
    all_posts_hermione = reading_driver.read_all_messages_from_specific_user(all_accounts, "Hermione")
                
    assert(len(all_posts_harry) == 2)
    assert(all_posts_harry[0].content_message == "Some one want to go eat some Pizza?")
    assert(all_posts_harry[1].content_message == "Hermione be nice we do not stop to study")
    assert(len(all_posts_ron) == 2)
    assert(all_posts_ron[0].content_message == "Yes me!!!")
    assert(all_posts_ron[1].content_message == "Stop to be boring!!!!")
    assert(len(all_posts_hermione) == 1)
    assert(all_posts_hermione[0].content_message == "Harry, Ron go back to study for the exams!!!!")

class ReadingDriver : 
    def __init__(self, ):
        self.accounts = {}            

    def read_all_messages_from_specific_user(self, all_accounts, account_name): 
        search = Search()
        return search.all_messages_from_specific_accounts(all_accounts, account_name)