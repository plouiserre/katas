from __future__ import annotations
from dataclasses import dataclass
from SocialNetwork.domain.models.account import Account


@dataclass(frozen=True)
class AccountResponse : 
    name : str

    @staticmethod
    def to_response(account : Account) -> AccountResponse:
        return AccountResponse(account.name)