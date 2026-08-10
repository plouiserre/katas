from SocialNetwork.domain.account.account_service import AccountService

class AccountContext():
    def __init__(self):
        self.account_service = AccountService()

    def get_following_service(self) -> AccountService: 
        return self.account_service

account_context = AccountContext()

def get_account_context() -> AccountContext:
    return account_context