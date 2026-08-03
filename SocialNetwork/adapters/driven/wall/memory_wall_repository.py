from SocialNetwork.domain.ports.outbound.wall_repository import WallRepository

from SocialNetwork.adapters.driven.entity.post_entity import PostEntity
from SocialNetwork.adapters.driven.entity.wall_entity import WallEntity
from SocialNetwork.domain.models.post import Post
from SocialNetwork.domain.models.wall import Wall

class MemoryWallRepository(WallRepository): 
    def __init__(self):
        super().__init__()
        self.wall = WallEntity([])
        
    def save_posts(self, post : Post):
        post_to_save = PostEntity.create_to_entity(post)
        self.wall.posts.append(post_to_save)

    def get_wall(self) -> Wall:
        wall_domain = WallEntity.create_to_domain(self.wall)
        return wall_domain