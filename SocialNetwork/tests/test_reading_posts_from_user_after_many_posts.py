from SocialNetwork.domain.search_service import SearchService
from SocialNetwork.tests.driver_test import DriverTest

def test_one_person_post_alone(): 
    search_driver = SearchDriver()

    all_messages = (search_driver
                    .posts_messages_peter_alone()
                    .search_message("Peter"))
    
    assert(len(all_messages) == 4)
    assert(all_messages[0] == "Hello every body")
    assert(all_messages[1] == "Some one is here")
    assert(all_messages[2] == "I will enjoy this meal!!!")
    assert(all_messages[3] == "Why my soccer team is bad?")

def test_three_friends_post():
    search_driver = SearchDriver()

    all_messages_harry = (search_driver
                    .posts_messages_harry_ron_hermione()
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

class SearchDriver(DriverTest): 
    def __init__(self):
        super().__init__()
        self.search_service = SearchService(self.wall)

    def post_message(self, account_name :str , message : str): 
        return super().post_message(account_name, message)

    def posts_messages_harry_ron_hermione(self):
        return super().posts_messages_harry_ron_hermione()

    def posts_messages_peter_alone(self):
        return super().posts_messages_peter_alone()
        
    def search_message(self, account_name):
        return self.search_service.load_wall_and_run_search_posts_from_specific_user(account_name)