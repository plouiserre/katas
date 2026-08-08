from SocialNetwork.domain.models.account import Account
from SocialNetwork.domain.ports.inbound.following_port import FollowingPort

class FollowingService(FollowingPort) : 
    def __init__(self):
        pass

    def account_follows_some_one(self, account : Account, following_account : Account) : 
        account.following_accounts.append(following_account)

    def see_followers_from_account(self, account : Account) -> list[Account] : 
        return account.following_accounts