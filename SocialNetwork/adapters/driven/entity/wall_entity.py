from __future__ import annotations
from dataclasses import dataclass

from SocialNetwork.adapters.driven.entity.account_entity import AccountEntity
from SocialNetwork.adapters.driven.entity.post_entity import PostEntity
from SocialNetwork.domain.models.wall import Wall

@dataclass(frozen=True)
class WallEntity : 
    posts : list[PostEntity]

    @staticmethod
    def create_to_entity(wall : Wall) -> WallEntity:
        posts = []
        for post in wall.posts : 
            p = PostEntity.create_to_entity(post)
            posts.append(p)
        return WallEntity(posts)

    @staticmethod
    def create_to_domain(wall_entity : WallEntity) -> Wall : 
        posts = []
        for post in wall_entity.posts : 
            p = PostEntity.create_to_domain(post)
            posts.append(p)
        return Wall(posts)

    @staticmethod
    def create_to_entity_from_wall_json(datas):
        all_posts = []
        for post in datas["posts"] : 
            account = AccountEntity.create_to_entity_from_message_json(post)
            post_entity = PostEntity.create_to_entity_from_message_json(account, post)
            all_posts.append(post_entity)
        wall_entity = WallEntity(all_posts)
        return wall_entity