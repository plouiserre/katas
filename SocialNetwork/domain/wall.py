from SocialNetwork.domain.account import Account

class Wall :
    def __init__(self):
        self.accounts = {}

    def posts_messages(self, account_name, message): 
        if account_name not in self.accounts : 
            self.accounts[account_name] = Account(account_name)
        self.accounts[account_name].post_messages(message)
        return self

    def get_all_accounts(self): 
        return self.accounts