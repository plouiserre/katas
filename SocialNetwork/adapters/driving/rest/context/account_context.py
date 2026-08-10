from SocialNetwork.domain.following_service import FollowingService

class AccountContext():
    def __init__(self):
        self.following_service = FollowingService()

    def get_following_service(self) -> FollowingService: 
        return self.following_service

account_context = AccountContext()

def get_account_context() -> AccountContext:
    return account_context