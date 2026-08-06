from __future__ import annotations
from dataclasses import dataclass

from SocialNetwork.domain.models.account import Account

@dataclass(frozen=True)
class AccountEntity :
    name : str

    @staticmethod
    def create_to_entity(account : Account):
        return AccountEntity(account.name)

    @staticmethod
    def create_to_domain(account_entity : AccountEntity):
        return Account(account_entity.name, [])

    @staticmethod
    def create_to_entity_from_message_json(datas):
        return AccountEntity(datas["account"]["name"])