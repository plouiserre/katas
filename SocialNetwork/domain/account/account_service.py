from SocialNetwork.domain.account.account_is_existing import AccountIsExisting
from SocialNetwork.domain.models.account import Account

class AccountService : 
    def __init__(self, account_repository):        
        self.account_repository = account_repository

    def add_account(self, new_account): 
        all_accounts = self.get_all_accounts()
        account_is_existing = AccountIsExisting(all_accounts)
        is_existing = account_is_existing.check_existence(new_account.name)
        if is_existing == False :
            account = Account.create_account(new_account.name, [])
            self.account_repository.add_account(account)

    def get_all_accounts(self): 
        return self.account_repository.get_all_accounts()

    def search_account(self, account_name): 
            account = self.account_repository.get_account_by_name(account_name)
            return account