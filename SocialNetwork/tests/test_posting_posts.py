import datetime
from SocialNetwork.tests.driver_test import DriverTest

start_date = datetime.datetime(2026,8,4,17,12,36)    

def test_one_person_post_alone(): 
    posting_driver = PostingDriver(start_date)
    all_messages = (posting_driver
                    .add_posts_peter_alone()
                    .check_messages())
    assert(len(all_messages) == 4)

def test_three_friends_post():
    posting_driver = PostingDriver(start_date)
    all_messages = (posting_driver
                    .add_posts_harry_ron_hermione()
                    .check_messages())
    assert(len(all_messages) == 5)

class PostingDriver(DriverTest) :
    def __init__(self, start_date):
        super().__init__(start_date)

    def add_posts(self, account_name, post):       
        return super().add_posts(account_name, post)

    def add_posts_harry_ron_hermione(self):
        return super().add_posts_harry_ron_hermione()

    def add_posts_peter_alone(self):
        return super().add_posts_peter_alone()

    def assert_tests_with_peter_alone(self, all_messages):
        pass

    def assert_tests_with_harry_ron_hermione(self, all_messages):
        pass

    #TODO factorize with reading_all_posts read_all_messages
    def check_messages(self):
        all_messages = {}
        all_messages = self.wall_service.get_all_messages_from_all_accounts()
        return all_messages