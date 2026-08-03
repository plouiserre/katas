from dataclasses import dataclass

from SocialNetwork.domain.models.post import Post

@dataclass(frozen=True)
class Wall : 
    posts : list[Post]