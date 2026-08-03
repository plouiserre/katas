from abc import ABC, abstractmethod

from SocialNetwork.adapters.driven.wall.memory_wall_repository import MemoryWallRepository
from SocialNetwork.domain.models.author import Author
from SocialNetwork.domain.models.message import Message
from SocialNetwork.domain.wall_service import WallService


class DriverTest(ABC):
    def __init__(self):
            wall_repository = MemoryWallRepository()
            self.wall_service = WallService(wall_repository)
    
    @abstractmethod 
    def post_message(self, account_name, message):       
        self.wall_service.post_messages(account_name, message)
        return self

    @abstractmethod
    def posts_messages_peter_alone(self): 
        (self.post_message("Peter", "Hello every body")
         .post_message("Peter", "Some one is here")
         .post_message("Peter", "I will enjoy this meal!!!")
         .post_message("Peter", "Why my soccer team is bad?"))
        return self

    @abstractmethod
    def posts_messages_harry_ron_hermione(self):
        (self.post_message("Harry", "Some one want to go eat some Pizza?")
        .post_message("Ron", "Yes me!!!")
        .post_message("Hermione", "Harry, Ron go back to study for the exams!!!!")
        .post_message("Harry", "Hermione be nice we do not stop to study")
        .post_message("Ron", "Stop to be boring!!!!"))
        return self

    @abstractmethod
    def assert_tests_with_peter_alone(self, all_messages) :
        peter_messages = all_messages["Peter"]
        assert(len(all_messages) == 1)

        assert(len(peter_messages) == 4)

        assert(peter_messages[0] == Message(Author("Peter"),"Hello every body"))
        assert(peter_messages[1] == Message(Author("Peter"),"Some one is here"))
        assert(peter_messages[2] == Message(Author("Peter"),"I will enjoy this meal!!!"))
        assert(peter_messages[3] == Message(Author("Peter"),"Why my soccer team is bad?"))

    @abstractmethod
    def assert_tests_with_harry_ron_hermione(self, all_messages) : 
        all_messages_harry = all_messages["Harry"]
        all_messages_ron = all_messages["Ron"]
        all_messages_hermione = all_messages["Hermione"]
    
        assert(len(all_messages) == 3)
    
        assert(len(all_messages_harry) == 2)
        assert(all_messages_harry[0] == Message(Author("Harry"),"Some one want to go eat some Pizza?"))
        assert(all_messages_harry[1] == Message(Author("Harry"),"Hermione be nice we do not stop to study"))
        assert(len(all_messages_ron) == 2)
        assert(all_messages_ron[0] == Message(Author("Ron"),"Yes me!!!"))
        assert(all_messages_ron[1] == Message(Author("Ron"),"Stop to be boring!!!!"))
        assert(len(all_messages_hermione) == 1)
        assert(all_messages_hermione[0] == Message(Author("Hermione"),"Harry, Ron go back to study for the exams!!!!"))