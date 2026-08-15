import pytest 

from SocialNetwork.adapters.driven.account.memory_account_repository import MemoryAccountRepository
from SocialNetwork.domain.models.account import Account
from SocialNetwork.domain.account.exception.following_not_existing_exception import FollowingNotExistingException
from SocialNetwork.domain.account.following_service import FollowingService

def test_1(): 
    is_following_account = (StopFollowingDataDriver("Peter")
                                 .add_account("Alice")
                                 .add_following_account("Alice")
                                 .delete_following_account("Alice")
                                 .is_following_account("Alice"))
    assert (is_following_account == False)

def test_2(): 
    is_following_account = (StopFollowingDataDriver("Peter")
                                 .add_account("Anna")
                                 .add_account("Alice")
                                 .add_account("John")
                                 .add_following_account("Anna")
                                 .add_following_account("Alice")
                                 .add_following_account("John")
                                 .delete_following_account("Alice")
                                 .is_following_account("Alice"))
    assert (is_following_account == False)

def test_3():
      with pytest.raises(FollowingNotExistingException) :
            (StopFollowingDataDriver("Alice")
                    .add_account("Peter")
                    .add_following_account("Peter")
                    .delete_following_account("Anna"))

class StopFollowingDataDriver: 
    def __init__(self, principal_account_name):
        self.principal_account = Account.create_account(principal_account_name, []) 
        self.following = None
        self.account_repository = MemoryAccountRepository()
        self.following_service = FollowingService(self.account_repository)
        self.account_repository.add_account(Account.create_account(principal_account_name, []))                
        
    def add_account(self, account_name): 
        self.account_repository.add_account(Account.create_account(account_name, []))
        return self

    def add_following_account(self, account_name_to_follow : str):
        self.following_service.add_following_account(self.principal_account.name, account_name_to_follow)
        return self

    def delete_following_account(self, account_name_stop_to_follow : str):
        self.following_service.delete_following_account(self.principal_account.name, account_name_stop_to_follow)         
        return self

    def is_following_account(self, account_name):
        is_following = False 
        for account in self.principal_account.following_accounts : 
            if account == account_name : 
                is_following = True
        return is_following