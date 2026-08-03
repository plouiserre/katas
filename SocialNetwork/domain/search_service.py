from SocialNetwork.domain.ports.inbound.search_port import SearchServicePort
from SocialNetwork.domain.search import Search
from SocialNetwork.domain.wall_service import WallService

class SearchService(SearchServicePort) : 
    def __init__(self, wall_service : WallService):
        self.wall_service = wall_service
        self.search = Search()

    def load_wall_and_run_search_posts_from_specific_user(self, account_name) -> list[str] :
        all_messages = self.wall_service.get_all_messages_from_all_accounts()
        return self.search.all_messages_from_specific_accounts(all_messages, account_name)