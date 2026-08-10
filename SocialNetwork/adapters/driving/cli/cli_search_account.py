from SocialNetwork.adapters.driving.response.account_response import AccountResponse
from SocialNetwork.domain.models.account import Account
from SocialNetwork.domain.ports.inbound.account_port import AccountPort

class CliSearchAccount: 
    def __init__(self, account_service : AccountPort):
        self.account_service = account_service

    def run_search_account(self, account_name)  :
        account = self.account_service.search_account(account_name)
        if account == None : 
            print("Aucun compte trouvé")
        else : 
            print("Compte de "+account.name+" trouvé")