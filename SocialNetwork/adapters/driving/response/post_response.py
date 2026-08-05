from __future__ import annotations
from SocialNetwork.adapters.driving.response.author_response import AuthorResponse
from SocialNetwork.domain.models.post import Post

from dataclasses import dataclass

@dataclass(frozen=True)
class PostResponse : 
    author : AuthorResponse
    content_message : str
    date_posting : str

    @staticmethod
    def to_response(post : Post):
        date = post.strftime.date_posting("%d/%m/%y %H:%M:%S")
        return PostResponse(AuthorResponse.to_response(post.author), post.content_message, date)
