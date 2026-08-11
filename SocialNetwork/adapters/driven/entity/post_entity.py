from __future__ import annotations
import datetime
from dataclasses import dataclass

from SocialNetwork.domain.models.post import Post

@dataclass(frozen=True)
class PostEntity :
    account_name : str
    content : str
    date_posting : datetime

    @staticmethod
    def create_to_entity(post : Post) -> PostEntity:
        return PostEntity(post.account_name, post.content_message, post.date_posting)

    @staticmethod 
    def create_to_domain(post_entity : PostEntity) -> Post : 
        return Post.create_post(post_entity.account_name, post_entity.content, post_entity.date_posting)

    @staticmethod
    def create_to_entity_from_message_json(datas):
        date_posting = datetime.datetime.fromisoformat(datas["date_posting"])
        return PostEntity(datas["account_name"], datas["content"], date_posting)