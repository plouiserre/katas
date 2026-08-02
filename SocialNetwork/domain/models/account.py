from SocialNetwork.domain.models.message import Message

class Account :
    def __init__(self, account_name, messages : list[Message]):
        self.name = account_name
        self.messages = messages

    def post_messages(self, message : Message): 
        self.messages.append(message)