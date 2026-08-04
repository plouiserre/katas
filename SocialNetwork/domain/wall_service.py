from SocialNetwork.domain.models.author import Author
from SocialNetwork.domain.models.post import Post
from SocialNetwork.domain.ports.inbound.wall_port import WallPort
from SocialNetwork.domain.ports.outbound.wall_repository import WallRepository

class WallService(WallPort) :
    def __init__(self, wall_repository : WallRepository):
        self.wall_repository = wall_repository

    def post_messages(self, author_name, content_post): 
        author = Author(author_name)
        post = Post(author, content_post)
        self.wall_repository.save_posts(post)
        return self

    def get_all_messages_from_all_accounts_group_by_author(self): 
        posts_by_authors = {}
        wall = self.wall_repository.get_wall()
        for post in wall.posts : 
            if post.author not in posts_by_authors : 
                posts_by_authors[post.author] = []
            posts_by_authors[post.author].append(post)
        return posts_by_authors

    def get_all_messages_from_all_accounts(self): 
        messages = []
        wall = self.wall_repository.get_wall()
        for post_entity in wall.posts : 
            author = Author(post_entity.author.name)
            post = Post(author, post_entity.content_message)
            messages.append(post)
        return messages