from __future__ import annotations
from dataclasses import dataclass

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