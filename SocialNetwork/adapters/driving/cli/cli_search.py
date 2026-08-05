from SocialNetwork.adapters.driving.response.wall_response import WallResponse

class CliSearch: 
    def __init__(self, arguments, search_service):
        self.arguments = arguments 
        self.search_service = search_service

    def run_search_command(self): 
        if len(self.arguments) == 1 : 
            account_name = self.arguments[0]
            posts_from_specific_user =  self.search_service.load_wall_and_run_search_posts_from_specific_user(account_name)
            if posts_from_specific_user == [] : 
                print("none message from "+account_name)
            else : 
                print ("messages de "+account_name)
                wall_response = WallResponse.to_response(posts_from_specific_user)
                for post in wall_response.posts : 
                    print(post.date_posting+": "+post.content_message)
        else : 
            print("Commande invalide")