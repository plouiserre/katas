from SocialNetwork.domain.search_service import SearchService
from SocialNetwork.adapters.driving.controllers.context.wall_context import get_wall_context

class SearchContext : 
    def __init__(self):
        wall_context  = get_wall_context()
        self.search_service = SearchService(wall_context.get_wall_service())

    def get_search_service(self) : 
        return self.search_service

_search_context = SearchContext()

def get_search_context() -> SearchContext : 
    return _search_context