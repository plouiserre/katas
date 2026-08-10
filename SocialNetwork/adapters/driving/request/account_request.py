from dataclasses import dataclass

@dataclass(frozen=True)
class AccountRequest : 
    account_name : str