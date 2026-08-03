from fastapi import FastAPI
from SocialNetwork.adapters.driven.wall.json_wall_repository import JsonWallRepository
from SocialNetwork.adapters.driven.wall.memory_wall_repository import MemoryWallRepository
from SocialNetwork.adapters.driving.cli.cli_app import cliApp
from SocialNetwork.adapters.driving.controllers import wall_controllers, search_controllers
from SocialNetwork.domain.search_service import SearchService
from SocialNetwork.domain.wall_service import WallService

# app = cliApp()
# # wall_repository = MemoryWallRepository()
# wall_repository = JsonWallRepository()
# wall_service = WallService(wall_repository)
# search_service = SearchService(wall_service)
# app.run(search_service, wall_service)

app = FastAPI()

app.include_router(search_controllers.router)
app.include_router(wall_controllers.router)

@app.get("/")
async def root():
    return {"Welcome in my RS :)"}