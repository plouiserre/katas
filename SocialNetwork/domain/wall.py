from SocialNetwork.domain.models.account import Account
from SocialNetwork.domain.models.author import Author
from SocialNetwork.domain.models.message import Message
from SocialNetwork.domain.ports.inbound.wall_port import WallPort
from SocialNetwork.domain.ports.outbound.wall_repository import WallRepository

class Wall(WallPort) :
    def __init__(self, wall_repository : WallRepository):
        self.wall_repository = wall_repository

    def post_messages(self, author_name, content_message): 
        author = Author(author_name)
        message = Message(author, content_message)
        self.wall_repository.save_posts(message)
        return self

    #TODO trier le tout
    def get_all_messages_from_account(self, account_name): 
        messages = []
        for key_account_name in self.accounts : 
            if key_account_name == account_name :
                for message in self.accounts[key_account_name].messages : 
                    messages.append(message)
        return messages

    def get_all_messages_from_all_accounts_group_by_author(self): 
        messages_by_authors = {}
        messages_entity = self.wall_repository.get_all_posts_from_wall()
        for message_entity in messages_entity : 
            author = Author(message_entity.author.name)
            message = Message(author, message_entity.content_message)
            if author not in messages_by_authors : 
                messages_by_authors[author] = []
            messages_by_authors[author].append(message)
        return messages_by_authors

    def get_all_messages_from_all_accounts(self): 
        messages = []
        messages_entity = self.wall_repository.get_all_posts_from_wall()
        for message_entity in messages_entity : 
            author = Author(message_entity.author.name)
            message = Message(author, message_entity.content_message)
            messages.append(message)
        return messages

    def get_all_accounts(self): 
        return self.accounts