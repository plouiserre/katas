import pytest

from SocialNetwork.adapters.driven.account.memory_account_repository import MemoryAccountRepository
from SocialNetwork.domain.account.account_service import AccountService
from SocialNetwork.domain.account.exception.following_not_existing_exception import FollowingNotExistingException
from SocialNetwork.domain.account.following_service import FollowingService
from SocialNetwork.domain.models.account import Account

def test_peter_follows_alice_from_datas():
    following_persons = (FollowingDataDriver("Peter")
                         .add_account("Alice")
                         .add_account("Luke")
                         .add_account("Mary")
                         .follows_someone("Alice")
                         .see_following_persons())
    assert(len(following_persons) == 1)
    assert(following_persons[0] == "Alice")

def test_alice_follows_peter_and_luke_from_datas():
    following_persons = (FollowingDataDriver("Alice")
                            .add_account("Peter")
                            .add_account("Luke")
                            .add_account("Mary")
                            .follows_someone("Peter")
                            .follows_someone("Luke")
                            .see_following_persons())
    assert(len(following_persons) == 2)
    assert(following_persons[0] == "Peter")
    assert(following_persons[1] == "Luke")

def test_add_following_someone_non_existent_in_the_datas():
    with pytest.raises(FollowingNotExistingException) :
        (FollowingDataDriver("Alice")
                .add_account("Peter")
                .add_account("Luke")
                .add_account("Mary")
                .follows_someone_non_existent("Paul"))


class FollowingDataDriver(): 
    def __init__(self, main_account_name):
        self.account_repository = MemoryAccountRepository()
        self.following_service = FollowingService(self.account_repository)
        self.account_service = AccountService(self.account_repository, self.following_service) 
        self.main_account_name = main_account_name
        self.account_repository.add_account(Account.create_account(main_account_name, []))

    def add_account(self, account_name): 
        self.account_repository.add_account(Account.create_account(account_name, []))
        return self

    def follows_someone(self, account_to_follow_name):
        self.following_service.add_following_account(self.main_account_name, account_to_follow_name)
        return self

    def follows_someone_non_existent(self, account_to_follow_name):
            self.following_service.add_following_account(self.main_account_name, account_to_follow_name)
            return self

    def see_following_persons(self): 
        account_to_compare =  self.account_service.search_account(self.main_account_name)
        following_accounts = account_to_compare.following_accounts
        return following_accounts