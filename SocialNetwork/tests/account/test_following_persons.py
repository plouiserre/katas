import pytest

from SocialNetwork.domain.account.exception.following_not_existing_exception import FollowingNotExistingException
from SocialNetwork.domain.account.following import Following
from SocialNetwork.domain.models.account import Account


def test_peter_follows_alice():
    following_persons = (FollowingDriver("Peter")
                         .add_account("Alice")
                         .add_account("Luke")
                         .add_account("Mary")
                         .follows_someone("Alice")
                         .see_following_persons())
    assert(len(following_persons) == 1)
    assert(following_persons[0] == "Alice")

def test_alice_follows_peter_and_luke():
    following_persons = (FollowingDriver("Alice")
                            .add_account("Peter")
                            .add_account("Luke")
                            .add_account("Mary")
                            .follows_someone("Peter")
                            .follows_someone("Luke")
                            .see_following_persons())
    assert(len(following_persons) == 2)
    assert(following_persons[0] == "Peter")
    assert(following_persons[1] == "Luke")

def test_add_following_someone_non_existent():
    with pytest.raises(FollowingNotExistingException) :
        (FollowingDriver("Alice")
                .add_account("Peter")
                .add_account("Luke")
                .add_account("Mary")
                .follows_someone_non_existent("Paul"))


class FollowingDriver(): 
    def __init__(self, main_account_name):
        self.main_account = Account.create_account(main_account_name, [])
        self.others_accounts = []

    def add_account(self, account_name): 
        self.others_accounts.append(Account.create_account(account_name, []))
        return self

    def follows_someone(self, account_to_follow_name):
        all_accounts = self.others_accounts
        all_accounts.append(self.main_account)
        self.following_service = Following(all_accounts)
        self.following_service.account_follows_some_one(self.main_account, account_to_follow_name)
        return self

    def follows_someone_non_existent(self, account_to_follow_name):
            all_accounts = self.others_accounts
            all_accounts.append(self.main_account)
            self.following_service = Following(all_accounts)
            self.following_service.account_follows_some_one(self.main_account, account_to_follow_name)
            return self

    def see_following_persons(self): 
        return self.following_service.see_followers_from_account(self.main_account)