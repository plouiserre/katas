from abc import ABC, abstractmethod

from SocialNetwork.domain.wall import Wall

class DriverTest(ABC):
    def __init__(self):
            self.wall = Wall()
    
    @abstractmethod 
    def post_message(self, account_name, message):       
        self.wall.post_messages(account_name, message)
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