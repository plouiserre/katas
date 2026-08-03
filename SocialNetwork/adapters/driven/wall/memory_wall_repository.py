from SocialNetwork.domain.ports.outbound.wall_repository import WallRepository

from SocialNetwork.adapters.driven.entity.message_entity import MessageEntity
from SocialNetwork.adapters.driven.entity.wall_entity import WallEntity
from SocialNetwork.domain.models.message import Message
from SocialNetwork.domain.models.wall import Wall

class MemoryWallRepository(WallRepository): 
    def __init__(self):
        super().__init__()
        self.wall = WallEntity([])
        
    def save_posts(self, message : Message):
        message_to_save = MessageEntity.create_to_entity(message)
        self.wall.messages.append(message_to_save)

    def get_wall(self) -> Wall:
        wall_domain = WallEntity.create_to_domain(self.wall)
        return wall_domain