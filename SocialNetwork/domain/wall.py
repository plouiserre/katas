from SocialNetwork.domain.account import Account

class Wall :
    def __init__(self, accounts):
        self.accounts = accounts

    def post_messages(self, account_name, message): 
        if account_name not in self.accounts : 
            self.accounts[account_name] = Account(account_name, [])
        self.accounts[account_name].post_messages(message)
        return self

    def get_all_messages_from_account(self, account_name): 
        messages = []
        for key_account_name in self.accounts : 
            if key_account_name == account_name :
                for message in self.accounts[key_account_name].messages : 
                    messages.append(message)
        return messages

    def get_all_accounts(self): 
        return self.accounts

    def get_messages_from_accounts(self, account_name): 
        return self.accounts[account_name].messages

    def get_all_accounts(self): 
        return self.accounts