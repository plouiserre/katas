from SocialNetwork.adapters.driving.cli.cli_command import CliCommand
from SocialNetwork.adapters.driving.cli.cli_get_all_messages import CliGetAllMessages
from SocialNetwork.adapters.driving.cli.cli_search import CliSearch
from SocialNetwork.domain.search_service import SearchServicePort
from SocialNetwork.domain.wall_service import WallPort

class cliApp : 
    def __init__(self):
        pass

    def run(self, search : SearchServicePort, wall : WallPort) -> None : 
        while True : 
            raw = input("> ")
            cli_command = CliCommand(raw)
            command, arguments = cli_command.find_command_and_arguments()
            if raw == "stop":
                break
            elif command == "search":
                cli_search = CliSearch(arguments, search)
                cli_search.run_search_command()
            elif command == "get_all_messages" : 
                cli_get_all_messages = CliGetAllMessages(wall)
                cli_get_all_messages.run_get_all_messages()
            elif command == "posts_messages" : 
                wall.post_messages(arguments[0], arguments[1])
                print("message posté")
            else : 
                print("commande inconnu")