from SocialNetwork.adapters.driving.response.wall_response import WallResponse

class CliGetAllPosts: 
    def __init__(self, wall):
        self.wall = wall

    def run_get_all_posts(self):
        posts_from_specific_user = self.wall.get_all_messages_from_all_accounts() 
        if posts_from_specific_user == {} :
            print("None message")
        else : 
            wall_response = WallResponse.to_response(posts_from_specific_user)
            for post in wall_response.posts : 
                print(post.account.name+": "+post.date_posting+": "+post.content_message)            