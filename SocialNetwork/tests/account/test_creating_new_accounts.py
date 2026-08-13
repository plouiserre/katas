from SocialNetwork.adapters.driven.account.memory_account_repository import MemoryAccountRepository
from SocialNetwork.domain.account.account_service import AccountService
from SocialNetwork.domain.account.following_service import FollowingService
from SocialNetwork.domain.models.account import Account

def test_create_harry_account(): 
    all_accounts_created = (AccountCreatingDriver()
                            .create_account("Harry")
                            .get_all_accounts_created())                            
    assert(1 == len(all_accounts_created))
    assert("Harry" == all_accounts_created[0].name)
    assert([] == all_accounts_created[0].following_accounts)

def test_create_harry_ron_accounts(): 
    all_accounts_created = (AccountCreatingDriver()
                            .create_account("Harry")
                            .create_account("Ron")
                            .get_all_accounts_created())                            
    assert(2 == len(all_accounts_created))
    assert("Harry" == all_accounts_created[0].name)
    assert([] == all_accounts_created[0].following_accounts)
    assert("Ron" == all_accounts_created[1].name)
    assert([] == all_accounts_created[1].following_accounts)

def test_create_harry_ron_accounts_only_one_time(): 
        all_accounts_created = (AccountCreatingDriver()
                                    .create_account("Harry")
                                    .create_account("Ron")                                    
                                    .create_account("Ron")
                                    .create_account("Harry")
                                    .get_all_accounts_created())                            
        assert(2 == len(all_accounts_created))
        assert("Harry" == all_accounts_created[0].name)
        assert([] == all_accounts_created[0].following_accounts)
        assert("Ron" == all_accounts_created[1].name)
        assert([] == all_accounts_created[1].following_accounts)

class AccountCreatingDriver: 
    def __init__(self):
        memory_account_repository = MemoryAccountRepository()
        following_service = FollowingService(memory_account_repository)
        self.account_service = AccountService(memory_account_repository, following_service) 

    def create_account(self, new_account_name): 
        self.account_service.add_account(new_account_name)
        return self

    def get_all_accounts_created(self): 
        return self.account_service.get_all_accounts()