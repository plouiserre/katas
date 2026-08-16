from abc import ABC, abstractmethod

class AccountPort(ABC): 
    @abstractmethod
    def add_account(self, account_name): 
        pass
    
    @abstractmethod
    def get_all_accounts(self): 
        pass

    @abstractmethod
    def search_account(self, account_name): 
        pass

    @abstractmethod
    def follow_new_account(self, account_name, follow_account_name):
        pass

    @abstractmethod
    def delete_follow_account(self, account_name, flollow_account_name): 
        pass