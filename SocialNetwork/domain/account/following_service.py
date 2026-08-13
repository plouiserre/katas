from SocialNetwork.domain.account.following import Following
from SocialNetwork.domain.ports.outbound.account_repository import AccountRepository

class FollowingService : 
    def __init__(self, account_repository : AccountRepository):
        self.accout_repository = account_repository
        self.accounts = []
        
    def add_following_account(self, main_account_name : str, new_following_account_name : str):
        self.__get_all_accounts()
        main_account = self.__get_account(main_account_name)
        following = Following(self.accounts)
        following.account_follows_some_one(main_account, new_following_account_name)
        self.accout_repository.update_account(main_account)
        
    def __get_all_accounts(self): 
        self.accounts = self.accout_repository.get_all_accounts()

    def __get_account(self, account_name : str): 
        account_search = None
        for account in self.accounts : 
            if account.name == account_name : 
                account_search = account
                break
        return account_search