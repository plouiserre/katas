class Search() : 
    def __init__(self):
        pass

    def all_messages_from_specific_accounts(self, all_messages, account_name):
        messages = []
        for message in all_messages :
            if message.author.name == account_name : 
                messages.append(message)
        return messages