import datetime
from SocialNetwork.tests.driver_test import DriverTest

start_date = datetime.datetime(2026,8,4,17,12,36)    

def test_get_messages_from_peter_unique_user():
    # scenario(
    #     message("17h12","salut","peter"),
    #     message("17h14","hello","alice"),                
    # )
    reading_driver = ReadingDriver(start_date)
    all_messages = (reading_driver
                        .add_posts_peter_alone()
                        .read_all_posts())
    reading_driver.assert_tests_with_peter_alone(all_messages)

def test_get_messages_from_three_friends_separate():
    reading_driver = ReadingDriver(start_date)
    all_messages = (reading_driver
                        .add_posts_harry_ron_hermione()
                        .read_all_posts())
    reading_driver.assert_tests_with_harry_ron_hermione(all_messages)

class ReadingDriver(DriverTest): 
    def __init__(self, start_date):
        super().__init__(start_date)

    def add_posts(self, account_name :str , message : str): 
        return super().add_posts(account_name, message)

    def add_posts_peter_alone(self):
        return super().add_posts_peter_alone()

    def add_posts_harry_ron_hermione(self):
        return super().add_posts_harry_ron_hermione()

    def assert_tests_with_peter_alone(self, peter_messages):
        return super().assert_tests_with_peter_alone(peter_messages)

    def assert_tests_with_harry_ron_hermione(self, all_messages):
        return super().assert_tests_with_harry_ron_hermione(all_messages)

    def read_all_posts(self): 
        messages = self.wall_service.get_all_messages_from_all_accounts()
        return messages