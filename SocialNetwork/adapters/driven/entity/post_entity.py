from __future__ import annotations
import datetime
from dataclasses import dataclass

from SocialNetwork.adapters.driven.entity.account_entity import AccountEntity
from SocialNetwork.domain.models.post import Post

@dataclass(frozen=True)
class PostEntity :
    account : AccountEntity
    content : str
    date_posting : datetime

    @staticmethod
    def create_to_entity(post : Post) -> PostEntity:
        account = AccountEntity.create_to_entity(post.account)
        return PostEntity(account, post.content_message, post.date_posting)

    @staticmethod 
    def create_to_domain(post_entity : PostEntity) -> Post : 
        account = AccountEntity.create_to_domain(post_entity.account)
        return Post.create_post(account, post_entity.content, post_entity.date_posting)

    @staticmethod
    def create_to_entity_from_message_json(account, datas):
        date_posting = datetime.datetime.fromisoformat(datas["date_posting"])
        return PostEntity(account, datas["content"], date_posting)