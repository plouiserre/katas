class Account :
    def __init__(self, account_name):
        self.name = account_name
        self.messages = []

    def post_messages(self, message): 
        self.messages.append(message)