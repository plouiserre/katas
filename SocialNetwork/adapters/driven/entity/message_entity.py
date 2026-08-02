from dataclasses import dataclass

from SocialNetwork.domain.models.message import Message

@dataclass(frozen=True)
class MessageEntity :
    author_name : str
    content : str

    @staticmethod
    def create_from_domain(message : Message):
        return MessageEntity(message.author_name, message.content_message)