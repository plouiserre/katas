from SocialNetwork.domain.models.account import Account

class AccountService : 
    def __init__(self):
        self.__accounts = []

    def add_account(self, account_name): 
        self.__accounts.append(Account.create_account(account_name))

    def get_all_accounts(self): 
        return self.__accounts

    def search_account(self, account_name): 
            for account in self.__accounts : 
                if account.name == account_name : 
                    return account
            return None