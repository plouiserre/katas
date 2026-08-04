from abc import ABC, abstractmethod

from SocialNetwork.adapters.driven.wall.memory_wall_repository import MemoryWallRepository
from SocialNetwork.domain.models.author import Author
from SocialNetwork.domain.models.post import Post
from SocialNetwork.domain.wall_service import WallService


class DriverTest(ABC):
    def __init__(self):
            wall_repository = MemoryWallRepository()
            self.wall_service = WallService(wall_repository)
    
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
    def assert_tests_with_peter_alone(self, all_messages) :
        peter_posts = all_messages["Peter"]
        assert(len(all_messages) == 1)

        assert(len(peter_posts) == 4)

        assert(peter_posts[0] == Post(Author("Peter"),"Hello every body"))
        assert(peter_posts[1] == Post(Author("Peter"),"Some one is here"))
        assert(peter_posts[2] == Post(Author("Peter"),"I will enjoy this meal!!!"))
        assert(peter_posts[3] == Post(Author("Peter"),"Why my soccer team is bad?"))

    @abstractmethod
    def assert_tests_with_harry_ron_hermione(self, all_posts) : 
        all_posts_harry = all_posts["Harry"]
        all_posts_ron = all_posts["Ron"]
        all_posts_hermione = all_posts["Hermione"]
    
        assert(len(all_posts) == 3)
    
        assert(len(all_posts_harry) == 2)
        assert(all_posts_harry[0] == Post(Author("Harry"),"Some one want to go eat some Pizza?"))
        assert(all_posts_harry[1] == Post(Author("Harry"),"Hermione be nice we do not stop to study"))
        assert(len(all_posts_ron) == 2)
        assert(all_posts_ron[0] == Post(Author("Ron"),"Yes me!!!"))
        assert(all_posts_ron[1] == Post(Author("Ron"),"Stop to be boring!!!!"))
        assert(len(all_posts_hermione) == 1)
        assert(all_posts_hermione[0] == Post(Author("Hermione"),"Harry, Ron go back to study for the exams!!!!"))