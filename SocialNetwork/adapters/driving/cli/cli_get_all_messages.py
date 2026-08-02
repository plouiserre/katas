class CliGetAllMessages: 
    def __init__(self, wall):
        self.wall = wall

    def run_get_all_messages(self):
        all_messages = self.wall.get_all_messages_from_all_accounts() 
        if all_messages == {} :
            print("None message")
        else : 
            for message in all_messages : 
                    print(message.author.name+": "+message.content_message)  