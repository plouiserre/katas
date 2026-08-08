from SocialNetwork.domain.models.account import Account

from abc import ABC, abstractmethod

class FollowingPort(ABC): 
    @abstractmethod
    def account_follows_some_one(self, account : Account, following_account : Account) : 
        pass

    @abstractmethod
    def see_followers_from_account(self, account : Account) -> list[Account] : 
        pass