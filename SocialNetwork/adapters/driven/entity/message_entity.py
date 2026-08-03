from __future__ import annotations
from dataclasses import dataclass

from SocialNetwork.adapters.driven.entity.author_entity import AuthorEntity
from SocialNetwork.domain.models.message import Message

@dataclass(frozen=True)
class MessageEntity :
    author : AuthorEntity
    content : str

    @staticmethod
    def create_to_entity(message : Message) -> MessageEntity:
        author = AuthorEntity.create_to_entity(message.author)
        return MessageEntity(author, message.content_message)

    @staticmethod 
    def create_to_domain(message_entity : MessageEntity) -> Message : 
        author = AuthorEntity.create_to_domain(message_entity.author)
        return Message(author, message_entity.content)

    @staticmethod
    def create_to_entity_from_message_json(author, datas):
        return MessageEntity(author, datas["content"])