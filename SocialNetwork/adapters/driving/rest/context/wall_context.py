from SocialNetwork.adapters.driving.rest.context.account_context import get_account_context
from SocialNetwork.adapters.driven.wall.json_wall_repository import JsonWallRepository
from SocialNetwork.adapters.driven.system_clock import SystemClock
from SocialNetwork.domain.wall_service import WallService

class WallContext : 
    def __init__(self):
        account_service = get_account_context().account_service
        wall_repository = JsonWallRepository()
        system_clock = SystemClock()
        self.wall_service = WallService(account_service, wall_repository, system_clock)

    def get_wall_service(self): 
        return self.wall_service

_wall_context = WallContext()

def get_wall_context() -> WallContext: 
    return _wall_context