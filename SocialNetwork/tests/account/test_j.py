import pytest 

from SocialNetwork.domain.models.account import Account
from SocialNetwork.domain.account.exception.following_not_existing_exception import FollowingNotExistingException

def test_1(): 
    is_following_account = (StopFollowingDriver()
                                 .create_account("Peter")
                                 .add_following_account("Alice")
                                 .delete_following_account("Alice")
                                 .is_following_account("Alice"))
    assert (is_following_account == False)

def test_2(): 
    is_following_account = (StopFollowingDriver()
                                 .create_account("Peter")
                                 .add_following_account("Anna")
                                 .add_following_account("Alice")
                                 .add_following_account("John")
                                 .delete_following_account("Alice")
                                 .is_following_account("Alice"))
    assert (is_following_account == False)

def test_3():
      with pytest.raises(FollowingNotExistingException) :
            (StopFollowingDriver()
                    .create_account("Alice")
                    .add_following_account("Peter")
                    .delete_following_account("Anna"))

class StopFollowingDriver: 
    def __init__(self):
        self.principal_account = None
        
    def create_account(self, account_name): 
        self.principal_account = Account.create_account(account_name, [])
        return self 

    def add_following_account(self, account_name_to_follow):
        self.principal_account.following_accounts.append(account_name_to_follow)
        return self

    def delete_following_account(self, account_name_stop_to_follow):
        following_person_to_delete = None
        for account_name in self.principal_account.following_accounts : 
            if account_name == account_name_stop_to_follow : 
                following_person_to_delete = account_name
                break
        if following_person_to_delete == None : 
            raise FollowingNotExistingException(self.principal_account.name+" do not follow "+account_name_stop_to_follow)
        self.principal_account.following_accounts.remove(following_person_to_delete)                
        return self

    def is_following_account(self, account_name):
        is_following = False 
        for account in self.principal_account.following_accounts : 
            if account == account_name : 
                is_following = True
        return is_following