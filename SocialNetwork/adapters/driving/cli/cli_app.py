from SocialNetwork.adapters.driving.cli.cli_command import CliCommand
from SocialNetwork.adapters.driving.cli.cli_get_all_posts import CliGetAllPosts
from SocialNetwork.adapters.driving.cli.cli_search import CliSearch
from SocialNetwork.adapters.driving.cli.cli_search_account import CliSearchAccount
from SocialNetwork.domain.ports.inbound.account_port import AccountPort
from SocialNetwork.domain.ports.inbound.search_port import SearchServicePort
from SocialNetwork.domain.ports.inbound.wall_port import WallPort

class cliApp : 
    def __init__(self):
        pass

    def run(self, account : AccountPort, search : SearchServicePort, wall : WallPort) -> None : 
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
                cli_get_all_posts = CliGetAllPosts(wall)
                cli_get_all_posts.run_get_all_posts()
            elif command == "posts_messages" : 
                wall.post_messages(arguments[0], arguments[1])
                print("message posté")
            elif command == "search_account": 
                cli_search_account = CliSearchAccount(account)
                cli_search_account.run_search_account(arguments[0])
            elif command == "add_account" : 
                account.add_account(arguments[0])
                print("compte créé")
            elif command == "delete_following": 
                account.delete_follow_account(arguments[0], arguments[1])
                print(arguments[1]+" ne follow plus "+arguments[0])
            elif command == "add_following" : 
                account.follow_new_account(arguments[0], arguments[1])
                print(arguments[0]+" suit "+arguments[1])
            else : 
                print("commande inconnu")