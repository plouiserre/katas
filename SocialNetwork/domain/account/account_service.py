from SocialNetwork.domain.models.account import Account

class AccountService : 
    def __init__(self, account_repository):        
        self.account_repository = account_repository

    def add_account(self, account_name): 
        account = Account.create_account(account_name)
        self.account_repository.add_account(account)

    def get_all_accounts(self): 
        return self.account_repository.get_all_accounts()

    def search_account(self, account_name): 
            account = self.account_repository.get_account_by_name(account_name)
            return account