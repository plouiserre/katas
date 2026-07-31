class Account :
    def __init__(self, account_name, messages):
        self.name = account_name
        self.messages = messages

    def post_messages(self, message): 
        self.messages.append(message)