from dataclasses import dataclass

from SocialNetwork.domain.models.message import Message

@dataclass(frozen=True)
class Wall : 
    messages : list[Message]