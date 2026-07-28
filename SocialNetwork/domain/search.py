class Search : 
    def __init__(self, all_accounts):
        self.accounts = all_accounts

    def all_messages_from_specific_accounts(self, account_name):
        messages = []
        for key_account_name in self.accounts :
            if key_account_name == account_name : 
                for message in self.accounts[key_account_name].messages :
                    messages.append(message)
        return messages