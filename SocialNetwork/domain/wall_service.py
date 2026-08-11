from SocialNetwork.domain.account.account_service import AccountService
from SocialNetwork.domain.models.account import Account
from SocialNetwork.domain.models.post import Post
from SocialNetwork.domain.ports.inbound.wall_port import WallPort
from SocialNetwork.domain.ports.outbound.wall_repository import WallRepository
from SocialNetwork.domain.ports.outbound.clock import Clock


class WallService(WallPort) :
    def __init__(self, account_service : AccountService, wall_repository : WallRepository, clock : Clock ):
        self.account_service = account_service
        self.wall_repository = wall_repository
        self.clock = clock

    def post_messages(self, account_name, content_post): 
        account = Account.create_account(account_name)
        self.account_service.add_account(account)
        post = Post.create_post(account, content_post, self.clock.now())
        self.wall_repository.save_posts(post)
        return self

    def get_all_messages_from_all_accounts(self): 
        messages = []
        wall = self.wall_repository.get_wall()
        for post_domain in wall.posts : 
            account = Account (post_domain.account.name, [])
            post = Post.create_post(account, post_domain.content_message, post_domain.date_posting)
            messages.append(post)
        return messages