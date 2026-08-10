from SocialNetwork.domain.account.NoOneIsAddedException import NoOneIsAddedException
from SocialNetwork.domain.models.account import Account

class Following() : 
    def __init__(self, all_accounts):
        self.all_accounts = all_accounts

    def account_follows_some_one(self, account : Account, following_account_name : str) : 
        is_somone_added = False
        for other_account in self.all_accounts :
            if other_account.name == following_account_name :
                account.following_accounts.append(other_account)
                is_somone_added = True
        if is_somone_added == False : 
            raise NoOneIsAddedException(following_account_name+" is unknown and cannot be added in "+account.name+" followings.")

    def see_followers_from_account(self, account : Account) -> list[Account] : 
        return account.following_accounts