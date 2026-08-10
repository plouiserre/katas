from abc import ABC, abstractmethod
from SocialNetwork.domain.models.account import Account

class AccountRepository(ABC):
    @abstractmethod
    def add_account(account : Account):
        pass 

    @abstractmethod
    def get_account_by_name(account_name : str):
        pass

    @abstractmethod
    def get_all_accounts():
        pass