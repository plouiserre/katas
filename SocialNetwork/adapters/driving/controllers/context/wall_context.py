from SocialNetwork.domain.wall_service import WallService
from SocialNetwork.adapters.driven.wall.json_wall_repository import JsonWallRepository

class WallContext : 
    def __init__(self):
        wall_repository = JsonWallRepository()
        self.wall_service = WallService(wall_repository)

    def get_wall_service(self): 
        return self.wall_service

_wall_context = WallContext()

def get_wall_context() -> WallContext: 
    return _wall_context