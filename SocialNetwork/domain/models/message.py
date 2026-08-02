from SocialNetwork.domain.models.author import Author

from dataclasses import dataclass

@dataclass(frozen=True)
class Message : 
    author : Author
    content_message : str
