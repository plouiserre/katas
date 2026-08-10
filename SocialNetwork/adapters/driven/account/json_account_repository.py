import json

from SocialNetwork.adapters.driven.entity.account_entity import AccountEntity
from SocialNetwork.domain.models.account import Account
from SocialNetwork.domain.ports.outbound.account_repository import AccountRepository

class JsonAccountRepository(AccountRepository):
    def __init__(self):
        super().__init__()
        self.path = "SocialNetwork/data/accounts.json"

    def add_account(self, account : Account):
        accounts_json = ""
        accounts_entity_existing = self.__get_all_accounts_saved()
        if accounts_entity_existing != None : 
            accounts_entity_existing.append(AccountEntity.create_to_entity(account))
            accounts_json = json.dumps([AccountEntity.to_dict(a) for a in accounts_entity_existing])
        else : 
            new_account = [AccountEntity.create_to_entity(account)]
            accounts_json = json.dumps([AccountEntity.to_dict(a) for a in new_account])
        with open(self.path, "w") as file : 
            file.write(accounts_json)

    def get_account_by_name(self, account_name : str):
        account_search = None
        all_accounts = self.__get_all_accounts_saved()
        for account in all_accounts : 
            if account.name == account_name : 
                account_search = account
        return account_search

    def __get_all_accounts_saved(self) -> []:
        accounts_entity = None 
        with open(self.path, "r") as file : 
            content = file.read()
            if content == '' :
                return accounts_entity
            clean_txt = content.replace("\n","")
            datas = json.loads(clean_txt)
            accounts_entity = AccountEntity.create_to_entity_from_accounts_json(datas)
        return accounts_entity    

    def get_all_accounts():
        pass