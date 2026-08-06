from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Account : 
    name : str
    following_accounts : list[Account]

    @staticmethod
    def create_account(account_name): 
        return Account(account_name, [])