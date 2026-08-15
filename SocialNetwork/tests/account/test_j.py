import pytest 

from SocialNetwork.domain.models.account import Account
from SocialNetwork.domain.account.exception.following_not_existing_exception import FollowingNotExistingException
from SocialNetwork.domain.account.following import Following

def test_1(): 
    is_following_account = (StopFollowingDriver("Peter")
                                 .add_account("Alice")
                                 .add_following_account("Alice")
                                 .delete_following_account("Alice")
                                 .is_following_account("Alice"))
    assert (is_following_account == False)

def test_2(): 
    is_following_account = (StopFollowingDriver("Peter")
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
            (StopFollowingDriver("Alice")
                    .add_account("Peter")
                    .add_following_account("Peter")
                    .delete_following_account("Anna"))

class StopFollowingDriver: 
    def __init__(self, principal_account_name):
        self.principal_account = Account.create_account(principal_account_name, []) 
        self.following = None
        self.others_accounts = [self.principal_account]
        
    def add_account(self, account_name): 
        self.others_accounts.append(Account.create_account(account_name, []))
        return self

    def add_following_account(self, account_name_to_follow):
        all_accounts = self.others_accounts
        all_accounts.append(self.principal_account)
        self.following_service = Following(all_accounts)
        self.following_service.account_follows_some_one(self.principal_account, account_name_to_follow)
        return self

    def delete_following_account(self, account_name_stop_to_follow):
        self.following_service.delete_following_account(self.principal_account, account_name_stop_to_follow)         
        return self

    def is_following_account(self, account_name):
        is_following = False 
        for account in self.principal_account.following_accounts : 
            if account == account_name : 
                is_following = True
        return is_following