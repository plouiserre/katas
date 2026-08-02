from abc import ABC, abstractmethod
class WallPort(ABC):
    @abstractmethod
    def post_messages(self, account_name, message): 
        pass

    @abstractmethod
    def get_all_messages_from_account(self, account_name): 
        pass

    @abstractmethod
    def get_all_messages_from_all_accounts_group_by_author(self): 
        pass

    @abstractmethod
    def get_all_messages_from_all_accounts(self):
        pass

    @abstractmethod
    def get_all_accounts(self): 
        pass
