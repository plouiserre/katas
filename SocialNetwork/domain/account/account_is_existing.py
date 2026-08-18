class AccountIsExisting : 
    def __init__(self, accounts):
        self.accounts = accounts

    def check_existence(self, account_name): 
        is_existing = False 
        for account in self.accounts :
            if account.name == account_name : 
                is_existing = True
                break
        return is_existing