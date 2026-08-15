from SocialNetwork.domain.account.exception.following_not_existing_exception import FollowingNotExistingException
from SocialNetwork.domain.models.account import Account

class Following() : 
    def __init__(self, all_accounts):
        self.all_accounts = all_accounts

    def account_follows_some_one(self, account : Account, following_account_name : str) : 
        is_somone_added = False
        for other_account in self.all_accounts :
            if other_account.name == following_account_name :
                account.following_accounts.append(other_account.name)
                is_somone_added = True
        if is_somone_added == False : 
            raise FollowingNotExistingException(following_account_name+" is unknown and cannot be added in "+account.name+" followings.")

    def see_followers_from_account(self, account : Account) -> list[Account] : 
        return account.following_accounts

    def delete_following_account(self, account : Account, account_name_stop_to_follow : str): 
        following_person_to_delete = None
        for account_name in account.following_accounts : 
            if account_name == account_name_stop_to_follow : 
                following_person_to_delete = account_name
                break
        if following_person_to_delete == None : 
            raise FollowingNotExistingException(account.name+" do not follow "+account_name_stop_to_follow)
        account.following_accounts.remove(following_person_to_delete)     