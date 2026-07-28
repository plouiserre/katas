from SocialNetwork.domain.search import SearchPort
from SocialNetwork.domain.wall import WallPort

class cliApp : 
    def __init__(self):
        pass

    def run(self, search : SearchPort, wall : WallPort) -> None : 
        while True : 
            raw = input("> ")
            command, _, arguments = raw.partition(" ")
            if raw == "stop":
                break
            elif command == "search":
                messages_from_specific_user =  search.all_messages_from_specific_accounts(arguments[0])
                print ("messages de "+arguments[0])
                for message in messages_from_specific_user : 
                    print(message + "\n")
            elif command == "get_all_messages" : 
                all_messages = wall.get_all_messages_from_all_accounts()                  
                for account_name in all_messages : 
                    for message in all_messages[account_name]:
                        print(account_name+": "+message)           
            elif command == "posts_messages" : 
                wall.post_messages(arguments[0], arguments[1])