from __future__ import annotations
from dataclasses import dataclass

from SocialNetwork.adapters.driving.response.post_response import PostResponse
from SocialNetwork.domain.models.wall import Wall

@dataclass(frozen=True)
class WallResponse : 
    posts : list[PostResponse]

    @staticmethod
    def to_response(wall : Wall): 
        posts_response = []
        for post in wall.posts : 
            post_response = PostResponse.to_response(post)
            posts_response.append(post_response)
        return WallResponse(posts_response)