from SocialNetwork.domain.ports.outbound.account_repository import AccountRepository

from SocialNetwork.adapters.driven.entity.account_entity import AccountEntity
from SocialNetwork.domain.models.account import Account

class MemoryAccountRepository(AccountRepository):
    def __init__(self):
        self.accounts = []

    def add_account(self, account : Account):
        account_to_save = AccountEntity.create_to_entity(account)
        self.accounts.append(account_to_save)

    def get_account_by_name(self, account_name):
        account_search = None
        for account in self.accounts : 
            if account.name == account_name : 
                account_search = account
                break
        account = AccountEntity.create_to_domain(account_search)
        return account

    def get_all_accounts(self) :
        all_accounts = []
        for account_entity in self.accounts : 
            account = AccountEntity.create_to_domain(account_entity)
            all_accounts.append(account)
        return all_accounts