class CliSearch: 
    def __init__(self, arguments, search_service):
        self.arguments = arguments 
        self.search_service = search_service

    def run_search_command(self): 
        if len(self.arguments) == 1 : 
            account_name = self.arguments[0]
            messages_from_specific_user =  self.search_service.load_wall_and_run_search_posts_from_specific_user(account_name)
            if messages_from_specific_user == [] : 
                print("none message from "+account_name)
            else : 
                print ("messages de "+account_name)
                for message in messages_from_specific_user : 
                    print(message.content_message)
        else : 
            print("Commande invalide")