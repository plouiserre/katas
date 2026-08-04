import json

from SocialNetwork.adapters.driven.entity.post_entity import PostEntity
from SocialNetwork.adapters.driven.entity.wall_entity import WallEntity
from SocialNetwork.domain.models.post import Post
from SocialNetwork.domain.models.wall import Wall
from SocialNetwork.domain.ports.outbound.wall_repository import WallRepository

class JsonWallRepository(WallRepository): 
    def __init__(self):
        super().__init__()
        self.path = "SocialNetwork/data/wall.json"

    def get_all_posts_from_wall() -> list[Post]:
        pass

    def get_wall(self):
        wall_entity = self.__get_wall_entity()
        return WallEntity.create_to_domain(wall_entity)

    def save_posts(self, post : Post):
        wall_json = ""
        wall_entity_existing = self.__get_wall_entity()
        if wall_entity_existing != None : 
            wall_entity_existing.posts.append(PostEntity.create_to_entity(post))
            wall_json = json.dumps(wall_entity_existing.__dict__, default=lambda o: o.__dict__, indent=4 )
        else : 
            new_wall = WallEntity([PostEntity.create_to_entity(post)])
            wall_json = json.dumps(new_wall.__dict__, default=lambda o: o.__dict__, indent=4 )
        with open(self.path, "w") as file :
            file.write(wall_json)

    def __get_wall_entity(self) -> Wall:
        wall_entity = None 
        with open(self.path, "r") as file : 
            content = file.read()
            if content == '' :
                return wall_entity
            clean_txt = content.replace("\n","")
            datas = json.loads(clean_txt)
            wall_entity = WallEntity.create_to_entity_from_wall_json(datas)
        return wall_entity