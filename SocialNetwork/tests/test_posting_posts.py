import datetime
from SocialNetwork.adapters.driven.account.memory_account_repository import MemoryAccountRepository
from SocialNetwork.adapters.driven.wall.memory_wall_repository import MemoryWallRepository
from SocialNetwork.domain.account.account_service import AccountService
from SocialNetwork.domain.wall_service import WallService
from SocialNetwork.tests.fake_clock import FakeClock


start_date = datetime.datetime(2026,8,4,17,12,36)    

def test_one_person_post_alone(): 
    posting_driver = PostingDriver(start_date)
    all_messages = (posting_driver
                    .add_posts("Peter", "Hello every body")
                    .add_posts("Peter", "Some one is here")
                    .add_posts("Peter", "I will enjoy this meal!!!")
                    .add_posts("Peter", "Why my soccer team is bad?")
                    .check_messages())
    
    all_accounts_created = (posting_driver
                            .count_accounts_created())
    
    assert(len(all_messages) == 4)
    assert(all_accounts_created == 1)

def test_three_friends_post():
    posting_driver = PostingDriver(start_date)
    all_messages = (posting_driver
                    .add_posts("Harry", "Some one want to go eat some Pizza?")
                    .add_posts("Ron", "Yes me!!!")
                    .add_posts("Hermione", "Harry, Ron go back to study for the exams!!!!")
                    .add_posts("Harry", "Hermione be nice we do not stop to study")
                    .add_posts("Ron", "Stop to be boring!!!!")
                    .check_messages())
    
    all_accounts_created = (posting_driver
                            .count_accounts_created())
    
    assert(len(all_messages) == 5)
    assert(all_accounts_created == 3)

class PostingDriver() :
    def __init__(self, start_date):
        account_repository = MemoryAccountRepository()
        self.account_service = AccountService(account_repository)
        wall_repository = MemoryWallRepository()
        self.clock = FakeClock(start_date)
        self.wall_service = WallService(self.account_service, wall_repository, self.clock)

    def add_posts(self, account_name, post):       
        self.wall_service.post_messages(account_name, post)
        return self    

    def check_messages(self):
        all_messages = {}
        all_messages = self.wall_service.get_all_messages_from_all_accounts()
        return all_messages

    def count_accounts_created(self): 
        all_accounts = self.account_service.get_all_accounts()
        return len(all_accounts)