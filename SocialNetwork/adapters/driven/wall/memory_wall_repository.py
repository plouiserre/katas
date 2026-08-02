from SocialNetwork.domain.ports.outbound.wall_repository import WallRepository

from SocialNetwork.adapters.driven.entity.message_entity import MessageEntity
from SocialNetwork.domain.models.message import Message

class MemoryWallRepository(WallRepository): 
    def __init__(self):
        super().__init__()
        self.posts : list[MessageEntity] = []

    def save_posts(self, message : Message):
        message_to_save = MessageEntity.create_from_domain(message)
        self.posts.append(message_to_save)

    def get_all_posts_from_wall(self) -> list[Message]:
        all_posts = []
        for post_memory in self.posts : 
            post = Message(post_memory.author, post_memory.content)
            all_posts.append(post)
        return all_posts