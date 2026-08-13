from __future__ import annotations
from dataclasses import dataclass

from SocialNetwork.domain.models.account import Account

@dataclass(frozen=True)
class AccountEntity :
    name : str
    following_accounts : list[str]

    @staticmethod
    def create_to_entity(account : Account):
        return AccountEntity(account.name, account.following_accounts)

    @staticmethod
    def create_to_domain(account_entity : AccountEntity):
        return Account.create_account(account_entity.name, account_entity.following_accounts)

    @staticmethod
    def create_to_entity_from_message_json(datas):
        return AccountEntity(datas["account_name"])

    
    @staticmethod
    def create_to_entity_from_message_json2(data):
        return AccountEntity(data["account_name"], [])

    @staticmethod
    def create_to_entity_from_accounts_json(datas):
        all_accounts = []
        for account in datas : 
            account_entity = AccountEntity.create_to_entity_from_message_json2(account)
            all_accounts.append(account_entity)
        return all_accounts

    @staticmethod
    def to_dict(account: AccountEntity) -> dict:
            return {"account_name": account.name, "following_accounts" : account.following_accounts}