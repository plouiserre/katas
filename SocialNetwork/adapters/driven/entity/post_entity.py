from __future__ import annotations
import datetime
from dataclasses import dataclass

from SocialNetwork.adapters.driven.entity.author_entity import AuthorEntity
from SocialNetwork.domain.models.post import Post

@dataclass(frozen=True)
class PostEntity :
    author : AuthorEntity
    content : str
    date_posting : datetime

    @staticmethod
    def create_to_entity(post : Post) -> PostEntity:
        author = AuthorEntity.create_to_entity(post.author)
        return PostEntity(author, post.content_message, post.date_posting)

    @staticmethod 
    def create_to_domain(post_entity : PostEntity) -> Post : 
        author = AuthorEntity.create_to_domain(post_entity.author)
        return Post(author, post_entity.content, post_entity.date_posting)

    @staticmethod
    def create_to_entity_from_message_json(author, datas):
        date_posting = datetime.datetime.fromisoformat(datas["date_posting"])
        return PostEntity(author, datas["content"], date_posting)