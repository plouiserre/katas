from SocialNetwork.domain.account_service import AccountService

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

class AccountCreatingDriver: 
    def __init__(self):
        self.account_service = AccountService() 

    def create_account(self, account_name): 
        self.account_service.add_account(account_name)
        return self

    def get_all_accounts_created(self): 
        return self.account_service.get_all_accounts()