from SocialNetwork.domain.wall import Wall
from SocialNetwork.adapters.driven.wall.memory_wall_repository import MemoryWallRepository

#TMP because I need it until I develop the data part
class WallContext : 
    def __init__(self):
        wall_repository = MemoryWallRepository()
        self.wall = Wall(wall_repository)

    def get_wall(self): 
        return self.wall

_wall_context = WallContext()

def get_wall_context() -> WallContext: 
    return _wall_context