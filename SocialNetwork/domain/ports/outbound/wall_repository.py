from abc import ABC, abstractmethod

class WallRepository(ABC) : 
    @abstractmethod
    def save_posts():
        pass

    @abstractmethod
    def get_wall():
        pass