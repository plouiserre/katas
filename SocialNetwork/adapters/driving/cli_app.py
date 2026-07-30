from SocialNetwork.domain.search_service import SearchServicePort
from SocialNetwork.domain.wall import WallPort

class cliApp : 
    def __init__(self):
        pass

    def run(self, search : SearchServicePort, wall : WallPort) -> None : 
        while True : 
            raw = input("> ")
            command, arguments = self.__get_commands_and_arguments(raw)
            if raw == "stop":
                break
            elif command == "search":
                if len(arguments) > 1 : 
                    messages_from_specific_user =  search.load_wall_and_run_search_posts_from_specific_user(arguments[0])
                    if messages_from_specific_user == [] : 
                        print("none message from "+arguments[0])
                    else : 
                        print ("messages de "+arguments[0])
                        for message in messages_from_specific_user : 
                            print(message + "\n")
                else : 
                    print("Commande invalide")
            elif command == "get_all_messages" : 
                all_messages = wall.get_all_messages_from_all_accounts() 
                if all_messages == {} :
                    print("None message")
                else : 
                    for account_name in all_messages : 
                        for message in all_messages[account_name]:
                            print(account_name+": "+message)           
            elif command == "posts_messages" : 
                wall.post_messages(arguments[0], arguments[1])
                print("message posté")


    def __get_commands_and_arguments(self, cli_command : str) -> tuple[str, list[str]] :
        indexs  = self.__find_quotation_in_command(cli_command)
        if len(indexs) > 1 : 
            message_to_post = cli_command[indexs[0]+1:indexs[1]]
            cli_command_without_big_argument = cli_command.replace(message_to_post, "").replace("\"", "").strip()
            elements_cli_command = cli_command_without_big_argument.split(" ")
            args = [elements_cli_command[1], message_to_post]
            return elements_cli_command[0], args
        else : 
            args = cli_command.split(" ")
            if len(args) > 1 : 
                return args[0], [args[1]]
            else : 
                return cli_command, []

    def __find_quotation_in_command(self, cli_command : str) -> list[int] :
        indexs = []
        for index , caracter in enumerate(cli_command) : 
            if caracter == "\"": 
                indexs.append(index)
        return indexs