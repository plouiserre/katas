from SocialNetwork.domain.account.Account_is_Existing import AccountIsExisting
from SocialNetwork.domain.models.account import Account

def test_check_alice_account_is_created():
    is_existing = (AccountExistingDriver()
                    .add_account(Account.create_account("Peter"))
                    .add_account(Account.create_account("Alice"))
                    .add_account(Account.create_account("Luke"))
                    .add_account(Account.create_account("John"))
                    .is_account_existing("Alice"))
    assert(is_existing == True)

def test_check_paul_account_is_not_created():
    is_existing = (AccountExistingDriver()
                    .add_account(Account.create_account("Peter"))
                    .add_account(Account.create_account("Alice"))
                    .add_account(Account.create_account("Luke"))
                    .add_account(Account.create_account("John"))
                    .is_account_existing("Paul"))
    assert(is_existing == False)

class AccountExistingDriver:
    def __init__(self):
        self.accounts = []
        
    def add_account(self, account : Account):
        self.accounts.append(account)
        return self 

    def is_account_existing(self, account_name):
        account_is_existing = AccountIsExisting(self.accounts)
        return account_is_existing.check_existence(account_name)