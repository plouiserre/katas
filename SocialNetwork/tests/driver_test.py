import datetime

from abc import ABC, abstractmethod

from SocialNetwork.adapters.driven.wall.memory_wall_repository import MemoryWallRepository
from SocialNetwork.domain.models.author import Author
from SocialNetwork.domain.models.post import Post
from SocialNetwork.domain.wall_service import WallService
from SocialNetwork.tests.fake_clock import FakeClock


class DriverTest(ABC):
    def __init__(self, start_date):
            wall_repository = MemoryWallRepository()
            self.clock = FakeClock(start_date)
            self.wall_service = WallService(wall_repository, self.clock)
    
    @abstractmethod 
    def add_posts(self, account_name, message):       
        self.wall_service.post_messages(account_name, message)
        return self

    @abstractmethod
    def add_posts_peter_alone(self): 
        (self.add_posts("Peter", "Hello every body")
         .add_posts("Peter", "Some one is here")
         .add_posts("Peter", "I will enjoy this meal!!!")
         .add_posts("Peter", "Why my soccer team is bad?"))
        return self

    @abstractmethod
    def add_posts_harry_ron_hermione(self):
        (self.add_posts("Harry", "Some one want to go eat some Pizza?")
        .add_posts("Ron", "Yes me!!!")
        .add_posts("Hermione", "Harry, Ron go back to study for the exams!!!!")
        .add_posts("Harry", "Hermione be nice we do not stop to study")
        .add_posts("Ron", "Stop to be boring!!!!"))
        return self

    @abstractmethod
    def assert_tests_with_peter_alone(self, all_posts) :
        assert(len(all_posts) == 4)

        assert(all_posts[0] == Post(Author("Peter" , []),"Hello every body", datetime.datetime(2026, 8, 4, 17, 12, 36)))
        assert(all_posts[1] == Post(Author("Peter" , []),"Some one is here", datetime.datetime(2026, 8, 4, 17, 13, 36)))
        assert(all_posts[2] == Post(Author("Peter" , []),"I will enjoy this meal!!!", datetime.datetime(2026, 8, 4, 17, 15, 36)))
        assert(all_posts[3] == Post(Author("Peter" , []),"Why my soccer team is bad?", datetime.datetime(2026, 8, 4, 17, 18, 36)))

    @abstractmethod
    def assert_tests_with_harry_ron_hermione(self, all_posts) : 
        assert(len(all_posts) == 5)
    
        assert(all_posts[0] == Post(Author("Harry" , []),"Some one want to go eat some Pizza?", datetime.datetime(2026, 8, 4, 17, 12, 36)))
        assert(all_posts[1] == Post(Author("Ron" , []),"Yes me!!!", datetime.datetime(2026, 8, 4, 17, 13, 36)))
        assert(all_posts[2] == Post(Author("Hermione" , []),"Harry, Ron go back to study for the exams!!!!", datetime.datetime(2026, 8, 4, 17, 15, 36)))
        assert(all_posts[3] == Post(Author("Harry" , []),"Hermione be nice we do not stop to study", datetime.datetime(2026, 8, 4, 17, 18, 36)))
        assert(all_posts[4] == Post(Author("Ron" , []),"Stop to be boring!!!!", datetime.datetime(2026, 8, 4, 17, 22, 36)))        