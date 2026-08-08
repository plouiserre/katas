from SocialNetwork.domain.account_service import AccountService

def test_1(): 
    account_search = (AccountReadingDriver()
                        .create_account("Peter")
                        .create_account("Paul")
                        .create_account("Alice")
                        .create_account("Luke")
                        .create_account("Mary")
                        .search_account("Alice"))
    assert("Alice" == account_search.name)
    assert([] == account_search.following_accounts)

class AccountReadingDriver: 
    def __init__(self):
        self.account_service = AccountService()

    def create_account(self, account_name):
        self.account_service.add_account(account_name)
        return self

    def search_account(self, account_name): 
        return self.account_service.search_account(account_name)