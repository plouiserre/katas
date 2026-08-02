from dataclasses import dataclass

from SocialNetwork.adapters.driven.entity.author_entity import AuthorEntity
from SocialNetwork.domain.models.message import Message

@dataclass(frozen=True)
class MessageEntity :
    author : AuthorEntity
    content : str

    @staticmethod
    def create_from_domain(message : Message):
        author = AuthorEntity.create_from_domain(message.author)
        return MessageEntity(author, message.content_message)