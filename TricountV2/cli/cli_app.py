from TricountV2.cli.cli_command import CliCommand
from TricountV2.business.trip import Trip

class cliApp :
    def __init__(self):
        self.trip = Trip()
    
    def run(self): 
        while True : 
            raw = input("> ")
            cli_command = CliCommand(raw)
            command, arguments = cli_command.find_command_and_arguments()
            if raw == "stop":
                break
            elif command == "activity": 
                if(len(arguments) != 4):
                    print("activité incomplète")
                self.trip.add_activity(arguments[0], arguments[1], arguments[2], arguments[3])
#             command, arguments = cli_command.find_command_and_arguments()
#             if raw == "stop":
#                 break
#             elif command == "search":
#                 cli_search = CliSearch(arguments, search)
#                 cli_search.run_search_command()
#             elif command == "get_all_messages" : 
#                 cli_get_all_posts = CliGetAllPosts(wall)
#                 cli_get_all_posts.run_get_all_posts()
#             elif command == "posts_messages" : 
#                 wall.post_messages(arguments[0], arguments[1])
#                 print("message posté")
#             elif command == "search_account": 
#                 cli_search_account = CliSearchAccount(account)
#                 cli_search_account.run_search_account(arguments[0])
#             elif command == "add_account" : 
#                 account.add_account(arguments[0])
#                 print("compte créé")
#             elif command == "delete_following": 
#                 account.delete_follow_account(arguments[0], arguments[1])
#                 print(arguments[1]+" ne follow plus "+arguments[0])
#             elif command == "add_following" : 
#                 account.follow_new_account(arguments[0], arguments[1])
#                 print(arguments[0]+" suit "+arguments[1])
#             elif command == "all_following": 
#                 cli_all_following = CliGetAllFollowing(account)
#                 cli_all_following.run_get_all_following_for_specific_account(arguments[0])
#             else : 
#                 print("commande inconnu")