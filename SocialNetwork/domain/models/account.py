from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Account : 
    name : str
    following_accounts : list[str]

    @staticmethod
    def create_account(account_name, followings_accounts_name): 
        return Account(account_name, followings_accounts_name)