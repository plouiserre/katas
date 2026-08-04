from SocialNetwork.tests.driver_test import DriverTest

def test_one_person_post_alone(): 
    posting_driver = PostingDriver()
    all_messages = (posting_driver
                    .add_posts_peter_alone()
                    .check_messages())
    assert(len(all_messages) == 1)
    assert(len(all_messages["Peter"]) == 4)

def test_three_friends_post():
    posting_driver = PostingDriver()
    all_messages = (posting_driver
                    .add_posts_harry_ron_hermione()
                    .check_messages())
    assert(len(all_messages) == 3)
    assert(len(all_messages["Harry"]) == 2)
    assert(len(all_messages["Ron"]) == 2)
    assert(len(all_messages["Hermione"]) == 1)

class PostingDriver(DriverTest) :
    def __init__(self):
        super().__init__()

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
        all_messages_by_autors = self.wall_service.get_all_messages_from_all_accounts_group_by_author()
        for author in all_messages_by_autors : 
            all_messages[author.name] = all_messages_by_autors[author]
        return all_messages