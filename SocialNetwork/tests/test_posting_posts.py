import datetime
from SocialNetwork.adapters.driven.wall.memory_wall_repository import MemoryWallRepository
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
    assert(len(all_messages) == 4)

def test_three_friends_post():
    posting_driver = PostingDriver(start_date)
    all_messages = (posting_driver
                    .add_posts("Harry", "Some one want to go eat some Pizza?")
                    .add_posts("Ron", "Yes me!!!")
                    .add_posts("Hermione", "Harry, Ron go back to study for the exams!!!!")
                    .add_posts("Harry", "Hermione be nice we do not stop to study")
                    .add_posts("Ron", "Stop to be boring!!!!")
                    .check_messages())
    assert(len(all_messages) == 5)

class PostingDriver() :
    def __init__(self, start_date):
        wall_repository = MemoryWallRepository()
        self.clock = FakeClock(start_date)
        self.wall_service = WallService(wall_repository, self.clock)

    def add_posts(self, account_name, post):       
        self.wall_service.post_messages(account_name, post)
        return self    

    def check_messages(self):
        all_messages = {}
        all_messages = self.wall_service.get_all_messages_from_all_accounts()
        return all_messages