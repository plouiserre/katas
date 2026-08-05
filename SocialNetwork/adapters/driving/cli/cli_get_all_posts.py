class CliGetAllPosts: 
    def __init__(self, wall):
        self.wall = wall

    def run_get_all_posts(self):
        all_posts = self.wall.get_all_messages_from_all_accounts() 
        if all_posts == {} :
            print("None message")
        else : 
            for post in all_posts : 
                    date_posting = post.date_posting.strftime("%d/%m/%y %H:%M:%S")
                    print(post.author.name+": "+date_posting+" "+post.content_message)  