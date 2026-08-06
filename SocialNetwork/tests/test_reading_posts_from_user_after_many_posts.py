import datetime

from SocialNetwork.domain.models.author import Author
from SocialNetwork.domain.models.post import Post
from SocialNetwork.domain.search_service import SearchService
from SocialNetwork.tests.driver_test import DriverTest

start_date = datetime.datetime(2026,8,4,17,12,36)    

def test_one_person_post_alone(): 
    search_driver = SearchDriver(start_date)

    all_messages = (search_driver
                    .add_posts_peter_alone()
                    .search_post("Peter"))
    
    search_driver.assert_tests_with_peter_alone(all_messages)

def test_three_friends_post_search_harry():
    search_driver = SearchDriver(start_date)

    all_messages_harry = (search_driver
                    .add_posts_harry_ron_hermione()
                    .search_post("Harry"))
    
    assert(all_messages_harry[0] == Post(Author("Harry" , []),"Some one want to go eat some Pizza?", datetime.datetime(2026, 8, 4, 17, 12, 36)))
    assert(all_messages_harry[1] == Post(Author("Harry" , []),"Hermione be nice we do not stop to study", datetime.datetime(2026, 8, 4, 17, 18, 36))) 

def test_three_friends_post_search_ron():
    search_driver = SearchDriver(start_date)

    all_messages_ron = (search_driver
                    .add_posts_harry_ron_hermione()
                    .search_post("Ron"))
    
    assert(all_messages_ron[0] == Post(Author("Ron" , []),"Yes me!!!", datetime.datetime(2026, 8, 4, 17, 13, 36)))
    assert(all_messages_ron[1] == Post(Author("Ron" , []),"Stop to be boring!!!!", datetime.datetime(2026, 8, 4, 17, 22, 36)))        

def test_three_friends_post_search_hermione():
    search_driver = SearchDriver(start_date)

    all_messages_hermione = (search_driver
                    .add_posts_harry_ron_hermione()
                    .search_post("Hermione"))
    
    assert(all_messages_hermione[0] == Post(Author("Hermione" , []),"Harry, Ron go back to study for the exams!!!!", datetime.datetime(2026, 8, 4, 17, 15, 36)))
    
class SearchDriver(DriverTest): 
    def __init__(self, start_date):
        super().__init__(start_date)
        self.search_service = SearchService(self.wall_service)

    def add_posts(self, account_name :str , message : str): 
        return super().add_posts(account_name, message)

    def add_posts_harry_ron_hermione(self):
        return super().add_posts_harry_ron_hermione()

    def add_posts_peter_alone(self):
        return super().add_posts_peter_alone()

    def assert_tests_with_harry_ron_hermione(self, all_messages):
        return super().assert_tests_with_harry_ron_hermione(all_messages)

    def assert_tests_with_peter_alone(self, all_messages):
        return super().assert_tests_with_peter_alone(all_messages)
        
    def search_post(self, account_name):
        return self.search_service.load_wall_and_run_search_posts_from_specific_user(account_name)