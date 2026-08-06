from __future__ import annotations
from SocialNetwork.adapters.driving.response.account_response import AccountResponse
from SocialNetwork.domain.models.post import Post

from dataclasses import dataclass

@dataclass(frozen=True)
class PostResponse : 
    account : AccountResponse
    content_message : str
    date_posting : str

    @staticmethod
    def to_response(post : Post):
        date = post.date_posting.strftime("%d/%m/%y %H:%M:%S")
        return PostResponse(AccountResponse.to_response(post.account), post.content_message, date)
