from SocialNetwork.tests.driver_test import DriverTest

def test_get_messages_from_peter_unique_user():
    reading_driver = ReadingDriver()
    all_messages = (reading_driver
                        .posts_messages_peter_alone()
                        .read_all_messages())
    reading_driver.assert_tests_with_peter_alone(all_messages)

def test_get_messages_from_three_friends_separate():
    reading_driver = ReadingDriver()
    all_messages_harry = (reading_driver
                        .posts_messages_harry_ron_hermione()
                        .read_all_messages())

    all_messages = reading_driver.read_all_messages()

    reading_driver.assert_tests_with_harry_ron_hermione(all_messages)

class ReadingDriver(DriverTest): 
    def __init__(self):
        super().__init__()

    def post_message(self, account_name :str , message : str): 
        return super().post_message(account_name, message)

    def posts_messages_peter_alone(self):
        return super().posts_messages_peter_alone()

    def posts_messages_harry_ron_hermione(self):
        return super().posts_messages_harry_ron_hermione()

    def assert_tests_with_peter_alone(self, peter_messages):
        return super().assert_tests_with_peter_alone(peter_messages)

    def assert_tests_with_harry_ron_hermione(self, all_messages):
        return super().assert_tests_with_harry_ron_hermione(all_messages)

    def read_all_messages(self): 
        messages = self.wall.get_all_messages_from_all_accounts()
        return messages