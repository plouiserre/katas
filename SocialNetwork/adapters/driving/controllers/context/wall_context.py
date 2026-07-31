from SocialNetwork.domain.wall import Wall

#TMP because I need it until I develop the data part
class WallContext : 
    def __init__(self):
        self.wall = Wall()

    def get_wall(self): 
        return self.wall

_wall_context = WallContext()

def get_wall_context() -> WallContext: 
    return _wall_context