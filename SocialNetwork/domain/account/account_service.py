from SocialNetwork.domain.account.account_is_existing import AccountIsExisting
from SocialNetwork.domain.models.account import Account

class AccountService : 
    def __init__(self, account_repository, following_service):        
        self.account_repository = account_repository
        self.following_service = following_service

    def add_account(self, new_account_name): 
        all_accounts = self.get_all_accounts()
        account_is_existing = AccountIsExisting(all_accounts)
        is_existing = account_is_existing.check_existence(new_account_name)
        if is_existing == False :
            account = Account.create_account(new_account_name, [])
            self.account_repository.add_account(account)

    def get_all_accounts(self): 
        return self.account_repository.get_all_accounts()

    def search_account(self, account_name): 
        account = self.account_repository.get_account_by_name(account_name)
        return account

    def follow_new_account(self, account_name, follow_account_name):
        self.following_service.add_following_account(account_name, follow_account_name)