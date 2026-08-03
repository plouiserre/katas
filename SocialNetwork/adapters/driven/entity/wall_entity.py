from __future__ import annotations
from dataclasses import dataclass

from SocialNetwork.adapters.driven.entity.author_entity import AuthorEntity
from SocialNetwork.adapters.driven.entity.message_entity import MessageEntity
from SocialNetwork.domain.models.wall import Wall

@dataclass(frozen=True)
class WallEntity : 
    messages : list[MessageEntity]

    @staticmethod
    def create_to_entity(wall : Wall) -> WallEntity:
        messages = []
        for message in wall.messages : 
            m = MessageEntity.create_to_entity(message)
            messages.append(m)
        return WallEntity(messages)

    @staticmethod
    def create_to_domain(wall_entity : WallEntity) -> Wall : 
        messages = []
        for message in wall_entity.messages : 
            m = MessageEntity.create_to_domain(message)
            messages.append(m)
        return Wall(messages)

    @staticmethod
    def create_to_entity_from_wall_json(datas):
        all_messages = []
        for message in datas["messages"] : 
            author = AuthorEntity.create_to_entity_from_message_json(message)
            message_entity = MessageEntity.create_to_entity_from_message_json(author, message)
            all_messages.append(message_entity)
        wall_entity = WallEntity(all_messages)
        return wall_entity