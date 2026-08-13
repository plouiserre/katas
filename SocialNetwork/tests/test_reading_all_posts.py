import datetime

from SocialNetwork.adapters.driven.account.memory_account_repository import MemoryAccountRepository
from SocialNetwork.adapters.driven.wall.memory_wall_repository import MemoryWallRepository
from SocialNetwork.domain.account.account_service import AccountService
from SocialNetwork.domain.account.following_service import FollowingService
from SocialNetwork.domain.models.post import Post
from SocialNetwork.domain.wall_service import WallService
from SocialNetwork.tests.fake_clock import FakeClock

start_date = datetime.datetime(2026,8,4,17,12,36)    

def test_get_messages_from_peter_unique_user():
    reading_driver = ReadingDriver(start_date)
    all_posts = (reading_driver
                        .add_posts("Peter", "Hello every body")
                        .add_posts("Peter", "Some one is here")
                        .add_posts("Peter", "I will enjoy this meal!!!")
                        .add_posts("Peter", "Why my soccer team is bad?")
                        .read_all_posts())

    assert(len(all_posts) == 4)
    
    assert(all_posts[0] == Post.create_post("Peter","Hello every body", datetime.datetime(2026, 8, 4, 17, 12, 36)))
    assert(all_posts[1] == Post.create_post("Peter","Some one is here", datetime.datetime(2026, 8, 4, 17, 13, 36)))
    assert(all_posts[2] == Post.create_post("Peter","I will enjoy this meal!!!", datetime.datetime(2026, 8, 4, 17, 15, 36)))
    assert(all_posts[3] == Post.create_post("Peter","Why my soccer team is bad?", datetime.datetime(2026, 8, 4, 17, 18, 36)))

def test_get_messages_from_three_friends_separate():
    reading_driver = ReadingDriver(start_date)
    all_messages = (reading_driver
                        .add_posts("Harry", "Some one want to go eat some Pizza?")
                        .add_posts("Ron", "Yes me!!!")
                        .add_posts("Hermione", "Harry, Ron go back to study for the exams!!!!")
                        .add_posts("Harry", "Hermione be nice we do not stop to study")
                        .add_posts("Ron", "Stop to be boring!!!!")
                        .read_all_posts())

    assert(len(all_messages) == 5)
        
    assert(all_messages[0] == Post.create_post("Harry","Some one want to go eat some Pizza?", datetime.datetime(2026, 8, 4, 17, 12, 36)))
    assert(all_messages[1] == Post.create_post("Ron","Yes me!!!", datetime.datetime(2026, 8, 4, 17, 13, 36)))
    assert(all_messages[2] == Post.create_post("Hermione","Harry, Ron go back to study for the exams!!!!", datetime.datetime(2026, 8, 4, 17, 15, 36)))
    assert(all_messages[3] == Post.create_post("Harry","Hermione be nice we do not stop to study", datetime.datetime(2026, 8, 4, 17, 18, 36)))
    assert(all_messages[4] == Post.create_post("Ron","Stop to be boring!!!!", datetime.datetime(2026, 8, 4, 17, 22, 36)))        

class ReadingDriver(): 
    def __init__(self, start_date):
        account_repository = MemoryAccountRepository()
        following_service = FollowingService(account_repository)
        self.account_service = AccountService(account_repository, following_service)
        wall_repository = MemoryWallRepository()
        self.clock = FakeClock(start_date)
        self.wall_service = WallService(self.account_service, wall_repository, self.clock)

    def add_posts(self, account_name :str , post : str): 
        self.wall_service.post_messages(account_name, post)
        return self      

    def read_all_posts(self): 
        messages = self.wall_service.get_all_messages_from_all_accounts()
        return messages