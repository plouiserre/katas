from SocialNetwork.domain.models.author import Author
from SocialNetwork.domain.models.message import Message
from SocialNetwork.domain.ports.inbound.wall_port import WallPort
from SocialNetwork.domain.ports.outbound.wall_repository import WallRepository

class WallService(WallPort) :
    def __init__(self, wall_repository : WallRepository):
        self.wall_repository = wall_repository

    def post_messages(self, author_name, content_message): 
        author = Author(author_name)
        message = Message(author, content_message)
        self.wall_repository.save_posts(message)
        return self

    def get_all_messages_from_all_accounts_group_by_author(self): 
        messages_by_authors = {}
        wall = self.wall_repository.get_wall()
        for message in wall.messages : 
            if message.author not in messages_by_authors : 
                messages_by_authors[message.author] = []
            messages_by_authors[message.author].append(message)
        return messages_by_authors

    def get_all_messages_from_all_accounts(self): 
        messages = []
        wall = self.wall_repository.get_wall()
        for message in wall.messages : 
            author = Author(message.author.name)
            message = Message(author, message.content_message)
            messages.append(message)
        return messages