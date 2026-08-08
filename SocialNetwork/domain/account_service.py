from SocialNetwork.domain.models.account import Account

class AccountService : 
    def __init__(self):
        self.accounts = []

    def add_account(self, account_name): 
        self.accounts.append(Account.create_account(account_name))

    def get_all_accounts(self): 
        return self.accounts