from SocialNetwork.adapters.driven.account.memory_account_repository import MemoryAccountRepository
from SocialNetwork.domain.models.account import Account
from SocialNetwork.domain.account.account_service import AccountService
from SocialNetwork.domain.account.following_service import FollowingService

def test_get_all_accounts_that_peter_follows(): 
    following_accounts = (FollowingDataDriver("Peter")
                            .add_account("Anna")
                            .add_account("John")
                            .add_account("Alice")
                            .add_following_account("Anna")
                            .add_following_account("John")
                            .add_following_account("Alice")
                            .get_all_followings_accounts())
    assert("Anna" == following_accounts[0])
    assert("John" == following_accounts[1])
    assert("Alice" == following_accounts[2])


class FollowingDataDriver(): 
    def __init__(self, account_name_principal):
        self.account_principal = Account.create_account(account_name_principal, [])
        memory_account_repository = MemoryAccountRepository()
        memory_account_repository.add_account(self.account_principal)
        self.following_service = FollowingService(memory_account_repository)
        self.account_service = AccountService(memory_account_repository, self.following_service)

    def add_account(self, account_name): 
        self.account_service.add_account(account_name)
        return self
    
    def add_following_account(self, account_name_to_follow : str):
        self.account_service.follow_new_account(self.account_principal.name, account_name_to_follow)
        return self

    def get_all_followings_accounts(self) : 
        return self.account_service.get_all_following_accounts(self.account_principal.name)