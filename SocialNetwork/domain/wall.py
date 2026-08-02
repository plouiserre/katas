from SocialNetwork.domain.models.account import Account
from SocialNetwork.domain.models.message import Message
from SocialNetwork.domain.ports.inbound.wall_port import WallPort
from SocialNetwork.domain.ports.outbound.wall_repository import WallRepository

class Wall(WallPort) :
    def __init__(self, wall_repository : WallRepository):
        self.accounts = {}
        self.wall_repository = wall_repository

    def post_messages(self, account_name, content_message): 
        if account_name not in self.accounts : 
            self.accounts[account_name] = Account(account_name, [])
        message = Message(account_name, content_message)
        self.wall_repository.save_posts(message)
        return self

    def get_all_messages_from_account(self, account_name): 
        messages = []
        for key_account_name in self.accounts : 
            if key_account_name == account_name :
                for message in self.accounts[key_account_name].messages : 
                    messages.append(message)
        return messages

    def get_all_messages_from_all_accounts(self): 
        messages = {}
        for account_name in self.accounts : 
            messages[account_name] = self.accounts[account_name].messages
        return messages

    def get_all_accounts(self): 
        return self.accounts