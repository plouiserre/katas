from SocialNetwork.domain.models.account import Account

class Following() : 
    def __init__(self, all_accounts):
        self.all_accounts = all_accounts

    def account_follows_some_one(self, account : Account, following_account_name : str) : 
        for other_account in self.all_accounts :
            if other_account.name == following_account_name :
                account.following_accounts.append(other_account)

    def see_followers_from_account(self, account : Account) -> list[Account] : 
        return account.following_accounts