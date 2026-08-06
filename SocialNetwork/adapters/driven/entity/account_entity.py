from __future__ import annotations
from dataclasses import dataclass

from SocialNetwork.domain.models.account import Account

@dataclass(frozen=True)
class AccountEntity :
    name : str

    @staticmethod
    def create_to_entity(author : Account):
        return AccountEntity(author.name)

    @staticmethod
    def create_to_domain(author_entity : AccountEntity):
        return Account(author_entity.name, [])

    @staticmethod
    def create_to_entity_from_message_json(datas):
        return AccountEntity(datas["author"]["name"])