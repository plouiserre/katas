from SocialNetwork.adapters.driven.account.json_account_repository import JsonAccountRepository
from SocialNetwork.domain.account.account_service import AccountService
from SocialNetwork.domain.account.following_service import FollowingService

class AccountContext():
    def __init__(self):
        json_account_repository = JsonAccountRepository()
        self.account_service = AccountService(json_account_repository)
        self.following_service = FollowingService(json_account_repository)

    def get_following_service(self) -> AccountService: 
        return self.account_service

account_context = AccountContext()

def get_account_context() -> AccountContext:
    return account_context