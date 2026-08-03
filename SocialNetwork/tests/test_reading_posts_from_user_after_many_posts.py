from SocialNetwork.domain.search_service import SearchService
from SocialNetwork.tests.driver_test import DriverTest

def test_one_person_post_alone(): 
    search_driver = SearchDriver()

    all_messages = (search_driver
                    .posts_messages_peter_alone()
                    .search_message("Peter"))
    
    all_messages_asserting = { "Peter" : all_messages}            
    search_driver.assert_tests_with_peter_alone(all_messages_asserting)

def test_three_friends_post():
    search_driver = SearchDriver()

    all_messages_harry = (search_driver
                    .posts_messages_harry_ron_hermione()
                    .search_message("Harry"))
    
    all_messages_ron = search_driver.search_message("Ron")
    all_messages_hermione = search_driver.search_message("Hermione")
    
    all_messages = {"Harry" : all_messages_harry, "Ron" : all_messages_ron, "Hermione" : all_messages_hermione}
    search_driver.assert_tests_with_harry_ron_hermione(all_messages)

class SearchDriver(DriverTest): 
    def __init__(self):
        super().__init__()
        self.search_service = SearchService(self.wall_service)

    def post_message(self, account_name :str , message : str): 
        return super().post_message(account_name, message)

    def posts_messages_harry_ron_hermione(self):
        return super().posts_messages_harry_ron_hermione()

    def posts_messages_peter_alone(self):
        return super().posts_messages_peter_alone()

    def assert_tests_with_harry_ron_hermione(self, all_messages):
        return super().assert_tests_with_harry_ron_hermione(all_messages)

    def assert_tests_with_peter_alone(self, all_messages):
        return super().assert_tests_with_peter_alone(all_messages)
        
    def search_message(self, account_name):
        return self.search_service.load_wall_and_run_search_posts_from_specific_user(account_name)