from SocialNetwork.tests.driver_test import DriverTest

def test_one_person_post_alone(): 
    posting_driver = PostingDriver()
    all_messages = (posting_driver
                    .posts_messages_peter_alone()
                    .check_messages())
    assert(len(all_messages) == 1)
    assert(len(all_messages["Peter"]) == 4)

def test_three_friends_post():
    posting_driver = PostingDriver()
    all_messages = (posting_driver
                    .posts_messages_harry_ron_hermione()
                    .check_messages())
    assert(len(all_messages) == 3)
    assert(len(all_messages["Harry"]) == 2)
    assert(len(all_messages["Ron"]) == 2)
    assert(len(all_messages["Hermione"]) == 1)

class PostingDriver(DriverTest) :
    def __init__(self):
        super().__init__()

    def post_message(self, account_name, message):       
        return super().post_message(account_name, message)

    def posts_messages_harry_ron_hermione(self):
        return super().posts_messages_harry_ron_hermione()

    def posts_messages_peter_alone(self):
        return super().posts_messages_peter_alone()

    def assert_tests_with_peter_alone(self, all_messages):
        pass

    def assert_tests_with_harry_ron_hermione(self, all_messages):
        pass

    #TODO revoir ca !!!!!
    def check_messages(self):
        all_messages = {}
        for account_name in self.wall.get_all_accounts() : 
            all_messages[account_name] = self.wall.get_all_messages_from_account(account_name)
        return all_messages