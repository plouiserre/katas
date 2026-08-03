import json

from SocialNetwork.domain.ports.outbound.wall_repository import WallRepository
from SocialNetwork.adapters.driven.entity.message_entity import MessageEntity
from SocialNetwork.domain.models.message import Message

class JsonWallRepository(WallRepository): 
    def __init__(self):
        super().__init__()

    def get_all_posts_from_wall() -> list[Message]:
        pass

    # def get_all_contacts(self) -> Iterator[Contact]:
    #         all_contacts = []
    #         with open("BirthdayGreetings/data/contacts.json", "r") as file : 
    #             content = file.read()
    #             all_contacts = json_to_contacts(content)
    #         return all_contacts

    def save_posts(self, post : MessageEntity):
        post_json = json.dumps(post.__dict__, default=lambda o: o.__dict__, indent=4 )
        with open("SocialNetwork/data/wall.json", "a") as file :
            file.write(post_json)
        pass