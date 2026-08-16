class CliGetAllFollowing: 
    def __init__(self, account_service):
        self.account_service = account_service

    def run_get_all_following_for_specific_account(self, account_name : str):
        following_accounts = self.account_service.get_all_following_accounts(account_name) 
        if following_accounts == [] :
            print("Aucune personne suivie")
        else : 
            print("Personne(s) suivie(s) de "+account_name)
            for following_account in following_accounts : 
                print(following_account)            