from SocialNetwork.domain.wall_service import WallService
from SocialNetwork.adapters.driven.wall.memory_wall_repository import MemoryWallRepository

class WallContext : 
    def __init__(self):
        wall_repository = MemoryWallRepository()
        self.wall_service = WallService(wall_repository)

    def get_wall_service(self): 
        return self.wall_service

_wall_context = WallContext()

def get_wall_context() -> WallContext: 
    return _wall_context