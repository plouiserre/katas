import datetime

from SocialNetwork.adapters.driven.account.memory_account_repository import MemoryAccountRepository
from SocialNetwork.adapters.driven.wall.memory_wall_repository import MemoryWallRepository
from SocialNetwork.domain.account.account_service import AccountService
from SocialNetwork.domain.models.account import Account
from SocialNetwork.domain.models.post import Post
from SocialNetwork.domain.search_service import SearchService
from SocialNetwork.domain.wall_service import WallService
from SocialNetwork.tests.fake_clock import FakeClock

start_date = datetime.datetime(2026,8,4,17,12,36)    

def test_one_person_post_alone(): 
    search_driver = SearchDriver(start_date)

    all_posts_peter = (search_driver
                    .add_posts("Peter", "Hello every body")
                    .add_posts("Peter", "Some one is here")
                    .add_posts("Peter", "I will enjoy this meal!!!")
                    .add_posts("Peter", "Why my soccer team is bad?")
                    .search_post("Peter"))
    
    assert(len(all_posts_peter) == 4)
    
    assert(all_posts_peter[0] == Post.create_post("Peter","Hello every body", datetime.datetime(2026, 8, 4, 17, 12, 36)))
    assert(all_posts_peter[1] == Post.create_post("Peter","Some one is here", datetime.datetime(2026, 8, 4, 17, 13, 36)))
    assert(all_posts_peter[2] == Post.create_post("Peter","I will enjoy this meal!!!", datetime.datetime(2026, 8, 4, 17, 15, 36)))
    assert(all_posts_peter[3] == Post.create_post("Peter","Why my soccer team is bad?", datetime.datetime(2026, 8, 4, 17, 18, 36)))

def test_three_friends_post_search_harry():
    search_driver = SearchDriver(start_date)

    all_posts_harry = (search_driver
                    .add_posts("Harry", "Some one want to go eat some Pizza?")
                    .add_posts("Ron", "Yes me!!!")
                    .add_posts("Hermione", "Harry, Ron go back to study for the exams!!!!")
                    .add_posts("Harry", "Hermione be nice we do not stop to study")
                    .add_posts("Ron", "Stop to be boring!!!!")
                    .search_post("Harry"))
    
    assert(all_posts_harry[0] == Post.create_post("Harry","Some one want to go eat some Pizza?", datetime.datetime(2026, 8, 4, 17, 12, 36)))
    assert(all_posts_harry[1] == Post.create_post("Harry","Hermione be nice we do not stop to study", datetime.datetime(2026, 8, 4, 17, 18, 36))) 

def test_three_friends_post_search_ron():
    search_driver = SearchDriver(start_date)

    all_posts_ron = (search_driver
                    .add_posts("Harry", "Some one want to go eat some Pizza?")
                    .add_posts("Ron", "Yes me!!!")
                    .add_posts("Hermione", "Harry, Ron go back to study for the exams!!!!")
                    .add_posts("Harry", "Hermione be nice we do not stop to study")
                    .add_posts("Ron", "Stop to be boring!!!!")
                    .search_post("Ron"))
    
    assert(all_posts_ron[0] == Post.create_post("Ron","Yes me!!!", datetime.datetime(2026, 8, 4, 17, 13, 36)))
    assert(all_posts_ron[1] == Post.create_post("Ron","Stop to be boring!!!!", datetime.datetime(2026, 8, 4, 17, 22, 36)))        

def test_three_friends_post_search_hermione():
    search_driver = SearchDriver(start_date)

    all_posts_hermione = (search_driver
                    .add_posts("Harry", "Some one want to go eat some Pizza?")
                    .add_posts("Ron", "Yes me!!!")
                    .add_posts("Hermione", "Harry, Ron go back to study for the exams!!!!")
                    .add_posts("Harry", "Hermione be nice we do not stop to study")
                    .add_posts("Ron", "Stop to be boring!!!!")
                    .search_post("Hermione"))
    
    assert(all_posts_hermione[0] == Post("Hermione","Harry, Ron go back to study for the exams!!!!", datetime.datetime(2026, 8, 4, 17, 15, 36)))
    
class SearchDriver(): 
    def __init__(self, start_date):
        account_repository = MemoryAccountRepository()
        self.account_service = AccountService(account_repository)
        wall_repository = MemoryWallRepository()
        self.clock = FakeClock(start_date)
        self.wall_service = WallService(self.account_service, wall_repository, self.clock)
        self.search_service = SearchService(self.wall_service)

    def add_posts(self, account_name :str , post : str): 
        self.wall_service.post_messages(account_name, post)
        return self    
        
    def search_post(self, account_name):
        return self.search_service.load_wall_and_run_search_posts_from_specific_user(account_name)