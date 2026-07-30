class CliGetAllMessages: 
    def __init__(self, wall):
        self.wall = wall

    def run_get_all_messages(self):
        all_messages = self.wall.get_all_messages_from_all_accounts() 
        if all_messages == {} :
            print("None message")
        else : 
            for account_name in all_messages : 
                for message in all_messages[account_name]:
                    print(account_name+": "+message)  