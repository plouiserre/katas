class Search() : 
    def __init__(self):
        pass

    def all_messages_from_specific_accounts(self, all_posts, account_name):
        posts = []
        for post in all_posts :
            if post.account.name == account_name : 
                posts.append(post)
        return posts